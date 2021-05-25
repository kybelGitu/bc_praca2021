#FIND DEVICE BY ADDR
def DETECT_DEVICE(_i2c, device_addr):
    _is_present = False
    _i2c_peripheries = _i2c.scan()
    for _i2c_periphery in _i2c_peripheries:    
      if (_i2c_periphery == device_addr):
        _is_present = True
    return _is_present