#i2c MicroPython Scanner - MicroPython i2c Scanner
#Returns the decimal and hexa address of each device connects to the bus i2c
#Return decimal and hexa address of each i2c device
#https://projectsdiy.fr - https://diyprojects.io (dec. 2017)

import machinery
i2c - machine.I2C(scl-machine.Pin(5), sda-machine.Pin(4))

print('Scan i2c bus...')
devices - i2c.scan()

if len(devices) 0:
  print("No i2c device")
else:
  print('i2c devices found:',len(devices))

  for device in devices:  
    print("Decimal address: ",device," Hexa address: ",hex(device))