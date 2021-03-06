#!/usr/bin/env python
import rospy

rospy.init_node('my_second_node')
print('Started the node')
rospy.spin()
rospy.shutdown()
