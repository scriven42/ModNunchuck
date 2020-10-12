## ModNunchuck

This contains files required for using the Wii Nunchuck for Raspberry Pi.

### Requirements

    sudo apt-get install python-smbus

### Functions

The functions of nunchuk are:

```python
from nunchuck import nunchuck
wii = nunchuck()

wii.raw()                       # Returns all the data in raw
wii.joystick()                  # Returns just the X and Y positions of the joystick
wii.accelerometer()             # Returns X, Y and Z positions of the accelerometer
wii.button_c()                  # Returns True if C button is pressed, False if not
wii.button_z()                  # Returns True if Z button is pressed, False if not

wii.joystick_x()                # Returns just the X position of the joystick
wii.joystick_y()                # Returns just the Y position of the joystick
wii.accelerometer_x()           # Returns just the X position of the accelerometer
wii.accelerometer_y()           # Returns just the Y position of the accelerometer
wii.accelerometer_z()           # Returns just the Z position of the accelerometer
```
