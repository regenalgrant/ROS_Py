#!/usr/bin/env python
import rospy
from ROS_py.srv import WordCount
import sys


rospy.init_node('service_client')

""" Registration / service broadcasted """
rospy.wait_for_service('word_count') 

"""Creating proxy, once service is broadcast / Service Name/ Service Type """
word_counter = rospy.ServiceProxy('word_count', WordCount)


""" Service call """
word_count = word_counter(words)

