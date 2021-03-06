#!/usr/bin/env python
import rospy

rospy.init_node('my_first_node')
print('Started the node')
rospy.spin()
rospy.shutdown()
