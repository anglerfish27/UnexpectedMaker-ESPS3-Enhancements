try:
    class Helper():
        """My own custom class for getting an ESP connected and read for use"""
        def __init__(self):
            import gc
            import neopixel
            import tinys3
            import ntptime
            from machine import Pin
            self.pixel = neopixel.NeoPixel(Pin(tinys3.RGB_DATA), 1)
            self.colors = "None"
            self.wifi_alive_counter = 0  # 0 = Not Connected 1 = Connected
   

        @micropython.native
        def led_off(self):
            """RBG LED is turned 'off'."""
            self.pixel[0] = (0, 0, 0, 0)
            self.pixel.write()

        def led_on(self,colors):
            """Turn LED ON"""
            import tinys3
            tinys3.set_pixel_power(True)
            
            if colors == 'red':
                self.pixel[0] = ( 255, 0, 0, .5)
                self.pixel.write()
            elif colors == 'yellow':
                self.pixel[0] = ( 255, 128, 0, .5)
                self.pixel.write()
            elif colors == 'green':
                self.pixel[0] = ( 0, 255, 0, .5)
                self.pixel.write()
            
        @micropython.native
        def wifi_connect(self):
            """Connect to local Wi-Fi using secrets.py credentials"""
            import network
            from secrets import WIFI_SSID
            from secrets import WIFI_PASSWORD
            
            network.MODE_11N
            network.WLAN.PM_NONE
            wlan = network.WLAN(network.STA_IF)
            wlan.active(True)
            if not wlan.isconnected():
                print('Connecting to WiFi...')
                wlan.connect(WIFI_SSID, WIFI_PASSWORD)
            while not wlan.isconnected():
                self.wifi_alive_counter = 0
                pass
            print('WiFi Connected! Network Details:')
            print(wlan.ifconfig())
            self.wifi_alive_counter = 1
        
        @micropython.native        
        def test_comms(self):
            """Simple connection web test to verify connectivty by getting status code"""
            import urequests
            from time import sleep
            
            print("Verifying Wi-Fi outbound connection.")
            try:
                if (urequests.get('https://www.cnn.com').status_code) == 200:  
                    print("Internet connectivity is established and working!")
                    self.wifi_alive_counter = 1
                    self.led_on('green')
                    sleep(.5)
                    self.led_off()
                    sleep(.5)
                    self.led_on('green')
                    sleep(.5)
                    self.led_off()
                    sleep(.5)
                    self.led_on('green')
                    sleep(.5)
                    self.led_off()
            except:
                self.wifi_alive_counter = 0
                self.led_on('red')
                sleep(1)
                self.led_off()
                sleep(1)
                self.led_on('red')
                sleep(1)
                self.led_off()
                sleep(1)
                self.led_off()
                print("Cannot reach the internet, retry connecting.")

    

        
        def get_battery_voltage(self):
            """Self explanatory"""
            import tinys3
            
            x = tinys3.get_battery_voltage()
            return x
    
        def get_vbus_present(self):
            """Detect if VBUS (5V) power source is present"""
            import tinys3
            x = tinys3.get_vbus_present()
            return x
    
        def rtc(self):
            """Method to set internal RTC using NTP"""
            from machine import RTC
            from time import gmtime
            
            if self.wifi_alive_counter == 1:
                tm = gmtime()
                rtc = RTC() #Now holds RTC Time (YYYY,MM,DD,HH,MM,SS,subseconds)TUPLE
                rtc.datetime((tm[0], tm[1], tm[2], tm[6] + 1, tm[3], tm[4], tm[5], 0))
                print("RTC Set!")
                print("**********************")
                print("Date: "f'{tm[1]:02d}',"/",f'{tm[2]:02d}',"/",f'{tm[0]:04d}')
                print("Time: "f'{tm[3]:02d}',":",f'{tm[4]:02d}',":",f'{tm[5]:02d}')
                print("**********************")
            else:
                print("You must first be connected to the internet to get NTP RTC time")
                print("Use reconnect() method to try and connect to the web again.")

except KeyboardInterrupt:
    print("Shutting it down.")
    tinys3.set_pixel_power(False)
