from pybricks.hubs import PrimeHub
from pybricks.pupdevices import Motor, ColorSensor, ForceSensor
from pybricks.parameters import Button, Color, Direction, Port, Side, Stop
from pybricks.robotics import DriveBase
from pybricks.tools import wait, StopWatch, Matrix

import run0, run1, run2, run3, run4, run5

hub = PrimeHub()

# Configure the stop button combination. Now, your program stops
# if you press the center and Bluetooth buttons simultaneously.
# hub.system.set_stop_button((Button.CENTER, Button.BLUETOOTH))
hub.system.set_stop_button((Button.BLUETOOTH))

##############################################################################
# Initialize the eyes.
# check document about how to use ColorSensor
# https://docs.pybricks.com/en/latest/pupdevices/colorsensor.html
# e.g.
# color = left_eye.color()
# reflection = left_eye.reflection()
left_eye = ColorSensor(Port.A)
right_eye = ColorSensor(Port.B)

##############################################################################
# Initialize the arms.
# check document about how to use Motor
# https://docs.pybricks.com/en/latest/pupdevices/motor.html
# e.g.
# left_arm.run_angle(speed, angle_degree)
left_arm = Motor(Port.C)
right_arm = Motor(Port.D)

##############################################################################
# check document about how to use drive_base
# https://docs.pybricks.com/en/latest/robotics.html
#
# Initialize the legs.
# Initialize both motors. In this example, the motor on the
# left must turn counterclockwise to make the robot go forward.
left_leg = Motor(Port.E, Direction.COUNTERCLOCKWISE)
right_leg = Motor(Port.F)

# Initialize the drive base. In this example, the wheel diameter is 62.4mm.
# The distance between the two wheel-ground contact points is 112mm.
drive_base = DriveBase(left_leg, right_leg, wheel_diameter=62, axle_track=120)
drive_base.settings(
    300, # mm/s
    750, # mm/s2 accelerate
    150, # degree / s
    750  # turn accelaration
)
drive_base.use_gyro(True)



##############################################################################
# Make a square that is bright on the outside and faint in the middle.
ZERO = Matrix(
    [
        [  0, 100, 100, 100,   0],
        [  0, 100,   0, 100,   0],
        [  0, 100,   0, 100,   0],
        [  0, 100,   0, 100,   0],
        [  0, 100, 100, 100,   0],
    ]
)
ONE = Matrix(
    [
        [  0,   0, 100,   0,   0],
        [  0, 100, 100,   0,   0],
        [  0,   0, 100,   0,   0],
        [  0,   0, 100,   0,   0],
        [  0, 100, 100, 100,   0],
    ]
)
TWO = Matrix(
    [
        [  0, 100, 100, 100,   0],
        [  0,   0,   0, 100,   0],
        [  0, 100, 100, 100,   0],
        [  0, 100,   0,   0,   0],
        [  0, 100, 100, 100,   0],
    ]
)
THREE = Matrix(
    [
        [  0, 100, 100, 100,   0],
        [  0,   0,   0, 100,   0],
        [  0, 100, 100, 100,   0],
        [  0,   0,   0, 100,   0],
        [  0, 100, 100, 100,   0],
    ]
)
FOUR = Matrix(
    [
        [  0, 100,   0, 100,   0],
        [  0, 100,   0, 100,   0],
        [  0, 100, 100, 100,   0],
        [  0,   0,   0, 100,   0],
        [  0,   0,   0, 100,   0],
    ]
)
FIVE = Matrix(
    [
        [  0, 100, 100, 100,   0],
        [  0, 100,   0,   0,   0],
        [  0, 100, 100, 100,   0],
        [  0,   0,   0, 100,   0],
        [  0, 100, 100, 100,   0],
    ]
)
num_map = {
    0:ZERO,
    1:ONE,
    2:TWO,
    3:THREE,
    4:FOUR,
    5:FIVE
}

##############################################################################
# Main code
run = 0
while True:
    pressed = hub.buttons.pressed()
    wait_time = 50
    if Button.LEFT in pressed:
        wait_time += 150
        run -= 1
        if run < 0:
            run = 5 
    elif Button.RIGHT in pressed:
        wait_time += 150
        run += 1
        if run > 5:
            run = 0
    elif Button.CENTER in pressed:
        hub.light.on(Color.VIOLET)
        # run the code
        if run == 0:
            run0.run(drive_base, left_arm, right_arm, left_eye, right_eye, hub.imu)
        elif run == 1:
            run1.run(drive_base, left_arm, right_arm, left_eye, right_eye, hub.imu)
        elif run == 2:
            run2.run(drive_base, left_arm, right_arm, left_eye, right_eye, hub.imu)
        elif run == 3:
            run3.run(drive_base, left_arm, right_arm, left_eye, right_eye, hub.imu)
        elif run == 4:
            run4.run(drive_base, left_arm, right_arm, left_eye, right_eye, hub.imu)
        elif run == 5:
            run5.run(drive_base, left_arm, right_arm, left_eye, right_eye, hub.imu)
    hub.light.on(Color.GREEN)
    hub.display.icon(num_map[run])
    wait(wait_time)