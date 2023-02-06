#!/usr/bin/env python3

import rospy
from duckietown_msgs.msg import Twist2DStamped

pub = rospy.Publisher("/lilduckie/car_cmd_switch_node/cmd",Twist2DStamped,queue_size=10)

def circle():
    rospy.init_node("circle")
    rate = rospy.Rate(1)

    cmd = Twist2DStamped()
    cmd.v = 2.5
    cmd.omega = -8
    cmd.header.stamp = rospy.Time.now()

    pub.publish(cmd)

    rate.sleep(5)

def stop():

    cmd = Twist2DStamped()
    cmd.v = 0.0
    cmd.omega = 0.0
    cmd.header.stamp = rospy.Time.now()

    pub.publish(cmd)

def idek(): # My duckie was ignoring the first few commands I was sending so I used this to make sure it got all of the commands
    rospy.init_node("circle")
    rate = rospy.Rate(1)

    cmd = Twist2DStamped()
    cmd.v = 0.0
    cmd.omega = 0.0
    cmd.header.stamp = rospy.Time.now()
    for i in range(0,10):
        pub.publish(cmd)
        rate.sleep()
try:
    idek()
    circle()
except rospy.ROSInterruptException:
    pass
finally:
    stop()