from machine import I2C,Pin
import ssd1306
import fun
import time
import consts

rst = Pin(16, Pin.OUT)
rst.value(1)

scl = Pin(15, Pin.OUT, Pin.PULL_UP)
sda = Pin(4, Pin.OUT, Pin.PULL_UP)

i2c = I2C(scl=scl, sda=sda)

lcd = ssd1306.SSD1306_I2C(128, 64, i2c)

result = fun.DATA_TRANSFER(i2c, consts.GDK101_ADDR, consts.READ_STATUS)
# print("naslo sa " + str(result))
print("naslo sa " + str(result))



# lcd.text("rslt "+ str(result), 3, 116)
# lcd.show()

fun.DISPLAY_VERSION(i2c, lcd, consts.GDK101_ADDR, 500)
# while True:
