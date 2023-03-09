#!/usr/bin/env pybricks-micropython

from pybricks import ev3brick as brick
from pybricks.ev3devices import (Motor, TouchSensor, ColorSensor,
                                 InfraredSensor, UltrasonicSensor, GyroSensor)
from pybricks.parameters import (Port, Stop, Direction, Button, Color,
                                 SoundFile, ImageFile, Align)
from pybricks.tools import print, wait, StopWatch
from pybricks.robotics import DriveBase

# Write your program here
brick.sound.beep()
#変数指定
x=0
left = Motor(Port.B)
right = Motor(Port.C)
arm = Motor(Port.A)
robot = DriveBase(left, right, 56, 114)
color_left = ColorSensor(Port.S1)
color_right = ColorSensor(Port.S4)
gy = GyroSensor(Port.S2)
gr = 72
grr=55
b = 25
br=11
w= 100
wr=80
grwl = (gr + w) / 2 
grwr = (grr+wr)/2
bgrl = (b + gr) / 2
bgrr = (br+grr) /2
robot.drive(50,0)
wait(3000)
while True:
    if x==5:
        right.reset_angle(0)
        left.reset_angle(0)
        while True:
            if right.angle()<=240:
                robot.drive(25,0)
            else:
                break
        arm.run(100)
        wait(1000)
        while True:
            if right.angle() >=0:
                robot.drive (-25,0)
            else:
                break
        while True:
            if right.angle() >=-260:
                robot.drive (-25,0)
            else:
                break
        x=-100
    else:
        if color_left.reflection () >= bgrl: #カラーセンサー左がグレーの場合
            if color_right.reflection () >= bgrr: #カラーセンサー右がグレーの場合
                robot.drive(25,0) #直進
            else: #カラーセンサー右が黒
                robot.drive(25,-25)
        else: #カラーセンサー左が黒
            if  color_right.reflection () >= bgrr: #カラーセンサー右がグレーの場合
                robot.drive(25,25)
            else: #カラーセンサー右が黒
                robot.drive(-50,0)
                wait(600)
                robot.drive(0,0)
                wait(1000)
                x=x+1
                if color_left.reflection() > grwl: #カラーセンサー左が白の場合
                    if color_right.reflection() > grwr: #カラーセンサー右が白の場合
                        brick.display.text("w w")
                        robot.drive(50,0)
                        wait(1300)
                        arm.run(-100)
                        wait(2500)
                        robot.drive(0,0)
                        wait(1000)
                        exit;
                    else:
                        brick.display.text("w g")
                        robot.drive(50,0)
                        wait(2300)
                        robot.drive(0,0)
                        wait(1000)
                        gy.reset_angle(0)
                        while not gy.angle() > 80:
                            robot.drive(10,100)
                            brick.display.text(gy.angle())
                            print(gy.angle())
                        robot.drive(0,0)
                        wait(1000)
                else:
                    if color_right.reflection() > grwr:#右白　左グレー
                        brick.display.text("g w")
                        robot.drive(50,0)
                        wait(2300)
                        robot.drive(0,0)
                        wait(3000)
                        gy.reset_angle(0)
                        while not gy.angle() < -80:
                            robot.drive(10,-100)
                            brick.display.text(gy.angle())
                            print(gy.angle())
                        robot.drive(0,0)
                        wait(1000)
                    else:
                        robot.drive(50,0)
                        wait(3000)