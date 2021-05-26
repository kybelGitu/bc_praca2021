from machine import I2C, Pin
import time
import consts

#FIND DEVICE BY ADDR
def DETECT_DEVICE(_i2c, device_addr):
    _is_present = False
    _i2c_peripheries = _i2c.scan() 
    time.sleep(1) # after scan need some time, otherwise OSError: [Errno 110] ETIMEDOUT
    for _i2c_periphery in _i2c_peripheries:    
      if (_i2c_periphery == device_addr):
        _is_present = True
    return _is_present

#INPUT: I2C, DEVICE_ADDR, COMMAND
#RETURN: DATA FROM I2C
# EXCEPTION IS GENERATED IF NO DEVICE WAS FOU ND
# DETECT DEVICE
# SEND DATA TO DEVICE
# READ DATA
def DATA_TRANSFER(_i2c,  device_addr, command):
    # data = _i2c.readfrom_mem(0X18, 0XB1, 2)
    data = _i2c.readfrom_mem(device_addr, command, 2)
    if not DETECT_DEVICE(_i2c, device_addr):
        raise Exception('device with addr {} not found: '.format(device_addr))
    else:
        data = _i2c.readfrom_mem(device_addr, command, 2)
    return data

#def RESET_DEVICE(_i2c, device_addr):

def DISPLAY_VERSION(_i2c, lcd, device_addr, location):
    #test if location is not out od bounds
    if(location < 0 or location > consts.MAX_LOCATION):
        raise Exception('location {} is out of bounds: '.format(location))
    data = _i2c.readfrom_mem(device_addr, consts.READ_FIRMWARE_VERSION, 2)
    version = "version: "+str(data[0]) + '.' + str(data[1])
    print(version)
    #coordinates is calculated by int division and reminder
    column = location % consts.DISPLAY_WIDTH
    line = location // consts.DISPLAY_WIDTH
    DISPLAY_TEXT(lcd, version, column, line)


def DISPLAY_TEXT(lcd, text, x_pos, y_pos):
    y_pos = y_pos - consts.LETTER_SIZE  if (y_pos + consts.LETTER_SIZE  > consts.DISPLAY_HEIGTH ) else y_pos 
    textLengthPixels = len(text)*consts.LETTER_SIZE
    x_pos = x_pos - textLengthPixels  if (x_pos + textLengthPixels  > consts.DISPLAY_WIDTH ) else x_pos 
    #text is too wide
    if(x_pos < 0):
        x_pos = 0
    lcd.text(text, x_pos, y_pos)
    lcd.show()
    time.sleep(2)



