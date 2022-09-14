#!/usr/bin/env pybricks-micropython
from pybricks.hubs import EV3Brick
from pybricks.ev3devices import (Motor, TouchSensor, ColorSensor,
                                 InfraredSensor, UltrasonicSensor, GyroSensor)
from pybricks.parameters import Port, Stop, Direction, Button, Color
from pybricks.tools import wait, StopWatch, DataLog
from pybricks.robotics import DriveBase
from pybricks.media.ev3dev import SoundFile, ImageFile


# This program requires LEGO EV3 MicroPython v2.0 or higher.
# Click "Open user guide" on the EV3 extension tab for more information.


# Create your objects here.
ev3 = EV3Brick()
motorBack = Motor(Port.B)
motorLeft = Motor(Port.A)
motorRight = Motor(Port.D)

# Write your program here.
ev3.speaker.beep()

i = 0
while(i < 10):
    motorBack.run_target(500,100)
    motorLeft.run_target(-500,100)
    motorRight.run_target(-500,100)
    i+=1
