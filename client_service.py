#!/usr/bin/env python
import rospy
from ROS_py.srv import WordCount
import sys


rospy.init_node('service_client')

""" Registration """
rospy.wait_for_service('word_count') 

"""Creating proxy """
word_counter = rospy.ServiceProxy( 

# Service Name
	'word_count', 

# Service Type
  WordCount     
)