from pybricks.hubs import PrimeHub
from pybricks.pupdevices import Motor, ColorSensor, UltrasonicSensor, ForceSensor
from pybricks.parameters import Button, Color, Direction, Port, Side, Stop
from pybricks.robotics import DriveBase
from pybricks.tools import wait, StopWatch

def run(drive_base, left_arm, right_arm, left_eye, right_eye, gyro):
    gyro.reset_heading(0)
    # Drive forward by 500mm (half a meter).
    drive_base.straight(450)
    drive_base.turn(-30)
    drive_base.straight(300)
    drive_base.turn(-60)
    drive_base.straight(385)
    drive_base.turn(43)
    drive_base.straight(185)
    drive_base.straight(-172)
    drive_base.turn(35)
    drive_base.straight(-110)
    drive_base.turn(17)
    drive_base.straight(120)
    drive_base.straight(-90)
    drive_base.turn(85)
    #robot is now at -90 degrees
    drive_base.straight(-400)
    drive_base.turn(-90)
    #robot is now at 0 degrees
    drive_base.straight(200)

    drive_base.stop()
