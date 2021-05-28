from machine import I2C, Pin
import time
import consts


def RESET_DEVICE(_i2c, device_addr, cmd_rst, lcd):
    result = DATA_TRANSFER(_i2c, device_addr, cmd_rst)
    # result saved in first byte of data:
    #  0 - fail  1 - pass
    if(result[0]):
        DISPLAY_TEXT(lcd, "device restarted", 0)
    else:
        DISPLAY_TEXT(lcd, "restart fail", 0)


def DISPLAY_VERSION(_i2c, lcd, device_addr, location):
    #test if location is not out od bounds
    if(location < 0 or location > consts.MAX_LOCATION):
        raise Exception('location {} is out of bounds: '.format(location))
    data = DATA_TRANSFER(_i2c, device_addr, consts.READ_FIRMWARE_VERSION)
    version = "version: "+str(data[0]) + '.' + str(data[1])
    DISPLAY_TEXT(lcd, version, location)


def MEASURE(_i2c, lcd, device_addr, location, cmd_mod):
    if(cmd_mod is not 0XB2 and cmd_mod is not 0XB3):
                raise Exception('bad command!')

    time = DATA_TRANSFER(_i2c, device_addr, consts.READ_MEASURING_TIME)
    data = DATA_TRANSFER(_i2c, device_addr, cmd_mod)
    DISPLAY_TIME(lcd, time[0], time[1],location)
    location += 128*consts.LETTER_SIZE +1 #count new line
    DISPLAY_MEASUREMENT(lcd, data[0], data[1], cmd_mod,location)


def DISPLAY_TIME(lcd, min, sec, location):
    print('min: {}, sec: {}'.format(min, sec))
    total = min*60 + sec
    days = total // (84400)#60*60*24
    hours = total // 3600
    min = min % 60
    sec = sec % 60

    text = "time:" + str(days) + "d" + str(hours) + "h" + str(min) + "m" + str(sec) + "s"
    print(text)
    DISPLAY_TEXT(lcd, text, location)

def DISPLAY_MEASUREMENT(lcd, integralPart, decimalPart, cmd_mod, location):
    interval = "10min" if ( cmd_mod is "0xb2") else "1min"
    print('integral part {} decimal part {}'.format( integralPart, decimalPart))
    value = integralPart + decimalPart/100
    text = interval + ":" + str(value) + "uSv/h"
    print(text)
    DISPLAY_TEXT(lcd, text, location)

def DISPLAY_TEXT(lcd, text, location):
    #coordinates is calculated by integral division and reminder
    x_pos = location % consts.DISPLAY_WIDTH
    y_pos = location // consts.DISPLAY_WIDTH
    y_pos = y_pos - consts.LETTER_SIZE  if (y_pos + consts.LETTER_SIZE  > consts.DISPLAY_HEIGTH ) else y_pos 
    textLengthPixels = len(text)*consts.LETTER_SIZE
    x_pos = x_pos - textLengthPixels  if (x_pos + textLengthPixels  > consts.DISPLAY_WIDTH ) else x_pos 
    #text is too wide
    if(x_pos < 0):
        x_pos = 0
    lcd.text(text, x_pos, y_pos)
    lcd.show()
    time.sleep(2)

#INPUT: I2C, DEVICE_ADDR, COMMAND
#RETURN: DATA FROM I2C
# EXCEPTION IS GENERATED IF NO DEVICE WAS FOU ND
# DETECT DEVICE
# SEND DATA TO DEVICE
# READ DATA
def DATA_TRANSFER(_i2c,  device_addr, command):
    if not DETECT_DEVICE(_i2c, device_addr):
        raise Exception('device with addr {} not found: '.format(device_addr))
    else:
        data = _i2c.readfrom_mem(device_addr, command, 2)
    return data
#FIND DEVICE BY ADDR
def DETECT_DEVICE(_i2c, device_addr):
    _is_present = False
    _i2c_peripheries = _i2c.scan() 
    time.sleep(1) # after scan need some time, otherwise OSError: [Errno 110] ETIMEDOUT
    for _i2c_periphery in _i2c_peripheries:    
      if (_i2c_periphery == device_addr):
        _is_present = True
    return _is_present