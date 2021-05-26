from machine import I2C, Pin
import time

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
