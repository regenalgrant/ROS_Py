#!/usr/bin/env python
import rospy
import WordCount
import WordCountResponse
from ROS_Py.srv 


""" Procedure, countWords, recieves input of strings, returns words count in the string. 
splitting strings into characters."""
def count_words(request):
  return [len(request.words.split())]

""" Initializing Nodes for broadcast service """
rospy.init_node('server_service')

service = rospy.Service('word_count', WordCount, count_words)
	

#keeping node active
rospy.spin()
