# Python Module to read the Wii Nunchuck
# Originally from mod-nunchuck.py [ https://github.com/OLIMEX/raspberrypi/ ]
# and nunchuck.py [ https://github.com/Boeeerb/Nunchuck/ ]

import smbus2
import time

# Constants
SMBUS_NUMBER = 1        # Default to i2c bus 1
ADDRESS = 0x52          # Wii Nunchuk Address
INIT_COMMAND = 0xF0
INIT_DATA = 0x55
READ_COMMAND = 0x00
READ_DATA = 6

class nunchuck:

    def __init__(self, busNum = SMBUS_NUMBER):
        self.bus = smbus2.SMBus(busNum)
        self.bus.write_byte_data(ADDRESS, INIT_COMMAND, INIT_DATA)
        time.sleep(0.1)
        return

    def read(self):
        buf = self.bus.read_i2c_block_data(ADDRESS, READ_COMMAND, READ_DATA)
        data = [0x00]*6
        for i in range(len(buf)):
            data[i] = buf[i]
        return data

    def raw(self):
        data = self.read()
        return data

    def joystick(self):
        data = self.read()
        return data[0],data[1]

    def joystick_x(self):
        data = self.read()
        return data[0]

    def joystick_y(self):
        data = self.read()
        return data[1]

    def button_c(self):
        data = self.read()
        butc = (data[5] >> 1) & 0x01
        return butc == 0

    def button_z(self):
        data = self.read()
        butz = data[5] & 0x01
        return butz == 0

    def accelerometer_x(self):
        data = self.read()
        data[2] <<= 2
        data[2] |= (data[5] >> 2) & 0x03
        return data[2]

    def accelerometer_y(self):
        data = self.read()
        data[3] <<= 2
        data[3] |= (data[5] >> 6) & 0x03
        return data[3]

    def accelerometer_z(self):
        data = self.read()
        return data[4]
