#!/usr/bin/env python3
# modnunchuck test/example app

import sys
import os
import time
from modnunchuck import nunchuck

def main():
    print("Nunchuck Test")
    nc1 = nunchuck(1)
    while True:
        time.sleep(0.2)
        os.system('clear')
        print("Analog X: {}".format(nc1.joystick_x()))
        print("Analog Y: {}".format(nc1.joystick_y()))
        print("X-axis: {}".format(nc1.accelerometer_x()))
        print("Y-axis: {}".format(nc1.accelerometer_y()))
        print("Z-axis: {}".format(nc1.accelerometer_z()))
        print("C Button: {}".format(nc1.button_c()))
        print("Z Button: {}".format(nc1.button_z()))
        print("Raw: {}".format(nc1.raw()))
        print("Joystick: {}".format(nc1.joystick()))

if __name__ == '__main__':
    main()
