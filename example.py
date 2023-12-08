try:
    from Helper import *
    from time import sleep

    fed = Helper() # create an instance of the Helper class

    #Remove any methods you don't want/need. This helper example has a list of the current methods that are functional.

    fed.wifi_connect() #Connect to Wi-Fi

    fed.test_comms() # Ensures you have network connectivity to the outside world.
    
    fed.led_on('red') #Turn on RGB LED to Red
    fed.led_on('green') #Turn on RGB LED to green
    fed.led_on('yellow') #Turn on RGB LED to yellow
    fed.led_on('blue') #Turn on RGB LED to Blue
    fed.led_off() #Turn off RGB LED
    print(f'Current battery voltage is {fed.battery_voltage()} volts if not connected to USB') #Provides battery voltage if plugged in, otherwise it returns USB power.
    print(f'USB connection status:{fed.usb_detect()}') #provides if USB is plugged in or not.
    fed.set_rtc_ntp()  #Sets the RTC via NTP time and also provides that time.
    

    
except KeyboardInterrupt:  #if you interrupt your program with a control + c this will ensure the LED and Wi-Fi are turned off.
    print("Shutting it down.")
    
finally:
    fed.led_off()
    fed.wifi_disconnect()
