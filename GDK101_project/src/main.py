from machine import I2C,Pin
import ssd1306
import fun
import time
import consts
import connection

rst = Pin(16, Pin.OUT)
rst.value(1)

scl = Pin(15, Pin.OUT, Pin.PULL_UP)
sda = Pin(4, Pin.OUT, Pin.PULL_UP)

i2c = I2C(scl=scl, sda=sda)

lcd = ssd1306.SSD1306_I2C(128, 64, i2c)
# fun.RESET_DEVICE(i2c,consts.GDK101_ADDR, consts.RESET_SENZOR, lcd)
#RESET DISPLAY
# lcd.fill(0)
# lcd.show()
# fun.MEASURE(i2c, lcd, consts.GDK101_ADDR, 0, consts.READ_MEASURING_VALUE_TEN_MIN)

# fun.DISPLAY_VERSION(i2c, lcd, consts.GDK101_ADDR, 500)
def gdk101():
    while True:
        location = 0
        status = i2c.readfrom_mem(consts.GDK101_ADDR, consts.READ_STATUS, 2)
        if(status[1]==1):
            fun.DISPLAY_TEXT(lcd, "detectet vibrations...",location)
            location += 128*consts.LETTER_SIZE +1 #count new line
        if(status[0]==0):
            fun.DISPLAY_TEXT(lcd, "senzor is starting...",location)
            time.sleep(10)
            continue
        else:
            if(status[1]is not 1):
                location = 0# reset display
                lcd.fill(0)
            fun.MEASURE(i2c, lcd,consts.GDK101_ADDR, location, consts.READ_MEASURING_VALUE_ONE_MIN)
        time.sleep(60)

connection.connect()

    # gdk101()