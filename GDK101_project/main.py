from machine import I2C,Pin

i2c = I2C(scl=Pin(22), sda=Pin(21))

devices = i2c.scan()

try:
    print("found device" + str(devices[0]))
except:
    print("devices not found")
