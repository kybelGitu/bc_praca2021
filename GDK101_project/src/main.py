from machine import I2C,Pin
import ssd1306
import fun

GDK101_ADDR = 0X18
LCD_ADDR = 0x3c

rst = Pin(16, Pin.OUT)
rst.value(1)

scl = Pin(15, Pin.OUT, Pin.PULL_UP)
sda = Pin(4, Pin.OUT, Pin.PULL_UP)

i2c = I2C(scl=scl, sda=sda)

lcd = ssd1306.SSD1306_I2C(128, 64, i2c)

result = fun.DETECT_DEVICE(i2c, LCD_ADDR)
print("naslo sa " + str(result))

lcd.text("rslt "+ str(result), 0, 0)
lcd.show()
# while True:
