#!/usr/bin/env python3
import rospy
import os
from std_msgs.msg import String
from service_1.srv import Talker, TalkerResponse, AddTwoInts, AddTwoIntsResponse
import multiprocessing

def handle_add_two_ints(req):
    rospy.set_param('gain', 10)
    y = rospy.get_param('gain')
    x = y * (req.a + req.b)
    print("Returning [%s * (%s + %s) = %s]"%(y, req.a, req.b, x))
    return AddTwoIntsResponse(x)

def talker():
    pub = rospy.Publisher('chatter', String, queue_size=10)
    rate = rospy.Rate(100)
    while not rospy.is_shutdown():
        hello_str = "hello world %s" % rospy.get_time()
        rospy.loginfo(hello_str)
        pub.publish(hello_str)
        rate.sleep()

def handle_talker(req):
    if str(req.req) == 'on':
        p.start()
        return TalkerResponse("Toggle activated")
    else:
        p.terminate()
        return TalkerResponse("Toggle deactivated")

def talker_server():
    rospy.init_node('talker_server', disable_signals=True)
    s = rospy.Service('talker', Talker, handle_talker)
    v = rospy.Service('add_two_ints', AddTwoInts, handle_add_two_ints)
    print("Ready to publish ROS topic or perform gain * (x + y)")
    rospy.spin()


if __name__ == '__main__':
    try:
        global p 
        p = multiprocessing.Process(target=talker)
        talker_server()
    except rospy.ROSInterruptException:
        pass
