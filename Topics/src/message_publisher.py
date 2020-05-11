
#!/usr/bin/env python
import rospy
import Complex 
import random 
from topics.msg 
from random 

# initialize node
rospy.init_node('message_publisher') 

# register topic / topic name /message type /queue size
pub = rospy.Publisher(    
  'complex',              
  Complex,                
  queue_size=3            #
)

# rate set 2
rate = rospy.Rate(2) 

while not rospy.is_shutdown(): 
  msg = Complex()           
  msg.real = random()       
  msg.imaginary = random()  

# publishing
  pub.publish(msg)  

#sleep at rate
  rate.sleep()      