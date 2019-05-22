#!/usr/bin/env python
import rospy
import sys,tty,termios,select
from std_msgs.msg import String
if __name__ == '__main__':
    rospy.init_node("keyboardinpnode")
    keypub=rospy.Publisher("mkeys",String,queue_size=1)
    rate=rospy.Rate(100)
    fd=sys.stdin.fileno()
    old_attr=termios.tcgetattr(fd)
    tty.setcbreak(fd)
    print("Publishing Keys")
    try:
        while not rospy.is_shutdown():
            if select.select([sys.stdin],[],[],0)[0]==[sys.stdin]:
                keypub.publish(sys.stdin.read(1))
            rate.sleep()
    finally:
        print("setting original attrs")
        termios.tcsetattr(fd,termios.TCSADRAIN,old_attr)