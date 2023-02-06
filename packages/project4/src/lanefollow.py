#!/usr/bin/env python3

import rospy
from duckietown_msgs.msg import LanePose
from duckietown_msgs.msg import WheelsCmdStamped

set_point = 0
prev_error = 0
delta_t = 1 # TODO find delta t
pub = rospy.Publisher("/lilduckie/wheels_driver_node/wheels_cmd",WheelsCmdStamped,queue_size=3)
default_vel = .5

def pd(d):
    global prev_error

    kp = rospy.get_param("kp")
    kd = rospy.get_param("kd")
    error = set_point - d
    value = kp*error + kd(error - prev_error)/delta_t
    prev_error = error
    return value

def callback(data):
    if rospy.get_param("pause"):
        stop()
    
    d = data.d

    u = pd(d)
    if u > 0.3:
        u = 0.3
    elif u < -0.3:
        u = -0.3
    else:
        pass
    rospy.loginfo("U: %s", u)
    publ(u)

def sub():
    rospy.Subscriber("/lilduckie/lane_filter_node/lane_pose",LanePose, callback)


def publ(u):
    global pub
    cmd = WheelsCmdStamped()

    cmd.vel_left = default_vel - u
    cmd.vel_right = default_vel + u

    pub.publish(cmd) # pub l & r vel

def stop():
    global pub
    cmd = WheelsCmdStamped()

    cmd.vel_left = 0.0
    cmd.vel_right = 0.0
    
    for i in range(0,10):
        pub.publish(cmd)
        rate.sleep()

if __name__ == '__main__':
    try:
        rospy.init_node("lanefollow")
        sub()
        rospy.spin()
    except rospy.ROSInterruptException:
        pass
    finally:
        stop()