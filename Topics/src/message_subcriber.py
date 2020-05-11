#!/usr/bin/env python
import rospy
import Int32
from std_msgs.msg 

# callback for receiving messages
def callback(msg): 
# print to Terminal 
  print(msg.data)   

# initialize node
rospy.init_node('topic_subscriber') 

# subscribe
sub = rospy.Subscriber('counter', Int32, callback) 

#keeping node active
rospy.spin() 