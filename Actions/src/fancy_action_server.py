#! /usr/bin/env python
import rospy
import time
import actionlib
import TimerAction
import TimerGoal
import TimerResult
import TimerFeedback
from Actions.msg 

# update count used for tracking feedback
def do_timer(goal): 
	start_time = time.time() 
	update_count = 0

# waiting time if larger than 60 seconds or will be aborted / also allowing user if fuction has been aborted
if goal.time_to_wait.to_sec() > 60.0:
	result = TimerResult()
	result.time_elapsed = rospy.Duration.from_sec(time.time() - start_time) 
	result.updates_sent = update_count
	server.set_aborted(result, "Timer aborted due to too-long wait")
return

# Looping with sleep increments
while (time.time() - start_time) < goal.time_to_wait.to_sec():

#loop is a check and balance to return True
		if server.is_preempt_requested(): 
			result = TimerResult() 
			result.time_elapsed = \
				rospy.Duration.from_sec(time.time() - start_time) 
			result.updates_sent = update_count 
			server.set_preempted(result, "Timer preempted") 

			return
#incremental feedback

		feedback = TimerFeedback()
		feedback.time_elapsed = rospy.Duration.from_sec(time.time() - start_time) 
		feedback.time_remaining = goal.time_to_wait - feedback.time_elapsed 
		server.publish_feedback(feedback)
		update_count += 1

		time.sleep(1.0)
# loop exit
	result = TimerResult()
	result.time_elapsed = rospy.Duration.from_sec(time.time() - start_time) 
	result.updates_sent = update_count
	server.set_succeeded(result, "Timer completed successfully")

rospy.init_node('timer_action_server')
server = actionlib.SimpleActionServer('timer', TimerAction, do_timer, False) 
server.start()
rospy.spin()