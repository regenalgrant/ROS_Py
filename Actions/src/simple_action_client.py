#! /usr/bin/env python
import rospy
import actionlib
import TimerAction
import TimerGoal
import TimerResult
from actions.msg 


rospy.init_node('timer_action_client')

# suggesting that server block until server begins
client = actionlib.SimpleActionClient('timer', TimerAction) client.wait_for_server()

#send goal messages once 5 seconds have completed then goal will transfered
goal = TimerGoal()
goal.time_to_wait = rospy.Duration.from_sec(5.0) client.send_goal(goal)

#will recieve reault from server after time elapse
client.wait_for_result()
print('Time elapsed: %f'%(client.get_result().time_elapsed.to_sec()))