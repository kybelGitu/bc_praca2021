from machine import I2C,Pin
import ssd1306
import fun
import time

LCD_ADDR = 0x3c
GDK101_ADDR = 0X18
RESET_SENZOR = 0XA0
READ_STATUS = 0XB0
READ_MEASURING_TIME = 0XB1
READ_MEASURING_VALUE_TEN_MIN = 0XB2
READ_MEASURING_VALUE_ONE_MIN = 0XB3
READ_FIRMWARE_VERSION = 0XB4

rst = Pin(16, Pin.OUT)
rst.value(1)

scl = Pin(15, Pin.OUT, Pin.PULL_UP)
sda = Pin(4, Pin.OUT, Pin.PULL_UP)

i2c = I2C(scl=scl, sda=sda)

lcd = ssd1306.SSD1306_I2C(128, 64, i2c)

result = fun.DATA_TRANSFER(i2c, GDK101_ADDR, READ_STATUS)
# print("naslo sa " + str(result))
print("naslo sa " + str(result))



lcd.text("rslt "+ str(result), 0, 0)
lcd.show()
# while True:
