#!/usr/bin/env python3
import rospy
import sys
from service_1.srv import Talker

def talker_client(msg):
    rospy.wait_for_service('talker')
    try:
        talk_service = rospy.ServiceProxy('talker', Talker)
        resp = talk_service(msg)
        return resp.res
    except rospy.ServiceException as e:
        print("Service call failed: %s"%e)

def usage():
    return "%s [on/off]"%sys.argv[0]

if __name__ == '__main__':
    if len(sys.argv) == 2:
        x = str(sys.argv[1])
    else:
        print(usage())
        sys.exit(1)
    print("Toggling publisher")
    print(talker_client(x))
    sys.exit(1)
