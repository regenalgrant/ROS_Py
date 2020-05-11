#!/usr/bin/env python
import rospy
import Int32 
from std_msgs.msg 

# Setup: initialize node, register topic, set rate

rospy.init_node('topic_publisher')

# register ros /int at 32/ the que size at 3
pub = rospy.Publisher( 
  'counter', 
  Int32, 
  queue_size=3 
)

#set rate two  
rate = rospy.Rate(2) 

# Loop: publish, count, sleep
count = 0
while not rospy.is_shutdown(): 
    pub.publish(count) 
    count += 1 
    rate.sleep() 