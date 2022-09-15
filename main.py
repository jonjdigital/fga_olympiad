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
motorBack = Motor(Port.A)
motorLeft = Motor(Port.B)
motorRight = Motor(Port.C)

distanceSensor = UltrasonicSensor(Port.S1)
touch = TouchSensor(Port.S2)

driver = DriveBase(motorLeft,motorRight,80,40)

# Write your program here.
ev3.speaker.beep()

# Write your program here.
ev3.speaker.beep()

while True:
    # Begin driving forward at 200 millimeters per second.
    driver.drive(-200, 0)

    # Wait until an obstacle is detected. This is done by repeatedly
    # doing nothing (waiting for 10 milliseconds) while the measured
    # distance is still greater than 300 mm.
    while distanceSensor.distance() > 300:
        wait(10)

    # Drive backward for 300 millimeters.
    driver.straight(300)

    # Turn around by 120 degrees
    driver.turn(120)