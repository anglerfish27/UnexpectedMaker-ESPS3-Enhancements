try:
    
    from Helper import *
    from time import sleep

    fed = Helper()
    fed.wifi_connect()
    sleep(1)
    fed.test_comms()
    
    print(f'Battery Voltage: {fed.get_battery_voltage()}V')
    print(f'Checking USB Connection: {fed.get_vbus_present()}')
    
    fed.rtc()
    
    print("testing colors wee rainbow")
    fed.led_on("green")
    sleep(2)
    fed.led_on("yellow")
    sleep(2)
    fed.led_on("red")
    sleep(2)
    print("bye")
    fed.led_off()





except KeyboardInterrupt:
    print("Shutting it down.")
    fed.led_off()
