#!/usr/bin/env python
import rospy
import Int32
from std_msgs.msg 


# initialize doubler node
rospy.init_node('doubler') 

#declare/int 32 doubled / calling broadcast
def callback(msg):
    doubled = Int32()            
    doubled.data = msg.data * 2 
    pub.publish(doubled)        

sub = rospy.Subscriber('number', Int32, callback)
pub = rospy.Publisher('doubled', Int32, queue_size=3)

rospy.spin() 