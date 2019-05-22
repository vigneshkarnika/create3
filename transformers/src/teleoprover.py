#!/usr/bin/env python
import rospy
from std_msgs.msg import String
from geometry_msgs.msg import Twist
rospy.init_node("myteleopnode")

keymaps={
    'w':[0,1,"forward"],
    'x':[0,-1,"backward"],
    'd':[1,0,"rightTurn"],
    'a':[-1,0,"leftTurn"],
    's':[0,0,"stop"]
}

def mycallback(msg):
    if len(msg.data)==0 or not keymaps.has_key(msg.data[0]):
        return
    action=keymaps[msg.data[0]]
    print(action[2])
    twist=Twist()
    twist.linear.x=action[1]
    twist.angular.z=action[0]
    pub.publish(twist)


pub=rospy.Publisher("cmd_vel_mux/input/teleop",Twist,queue_size=1)
sub = rospy.Subscriber("mkeys",String,mycallback)
rospy.spin()