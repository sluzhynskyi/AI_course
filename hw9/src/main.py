#!/usr/bin/env python
import rospy
import math
from geometry_msgs.msg import Twist
from std_msgs.msg import String
from gazebo_msgs.msg import ModelState 


def main():
    trash_hold = 0.5
    pub = rospy.Publisher('cmd_vel', Twist, queue_size=10)
    rospy.init_node('hw9', anonymous=True)
    rate = rospy.Rate(2) # 2hz
    msg = Twist()
    msg.linear.x = 0
    msg.angular.x = msg.angular.y = msg.angular.z = 0
    # while (not rospy.is_shutdown()) or math.dist([5,4], [msg.linear.x, msg.linear.y]) < 1 :
    while (not rospy.is_shutdown()) or msg.linear.x < 5 - trash_hold:
        msg.linear.x += .2
        pub.publish(msg)
        rate.sleep()
        
    while (not rospy.is_shutdown()) or msg.linear.y < 4 - trash_hold:
        msg.linear.y += .2
        pub.publish(msg)
        rate.sleep()
        

if __name__ == '__main__':
    try:
        main()
    except rospy.ROSInterruptException:
        pass