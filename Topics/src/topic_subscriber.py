#!/usr/bin/env python
import rospy
import Int32
from std_msgs.msg 

# recieving msg with callback / printing to Terminal
def callback(msg):  
  print(msg.data)   

# initialize node
rospy.init_node('topic_subscriber') 

sub = rospy.Subscriber('counter', Int32, callback) 

rospy.spin() 
