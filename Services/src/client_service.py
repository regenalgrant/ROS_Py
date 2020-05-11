#!/usr/bin/env python
import rospy
import WordCount
import sys
from ROS_py.srv 


rospy.init_node('service_client')

""" Registration / service broadcasted """
rospy.wait_for_service('word_count') 

"""Creating proxy, once service is broadcast / Service Name/ Service Type """
word_counter = rospy.ServiceProxy('word_count', WordCount)

words = ' '.join(sys.argv[1:])

""" Service call """
word_count = word_counter(words)

print words, '->', word_count.count