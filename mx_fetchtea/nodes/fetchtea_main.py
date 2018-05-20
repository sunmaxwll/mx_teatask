#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os
import time 
import random
import ctypes
import roslib
import rospy
import smach
import smach_ros
import threading
import thread
import string
import math
import numpy as np
from std_msgs.msg import String
from std_msgs.msg import Int32
from mx_fetchtea.srv import *
# from cv_bridge import CvBridge, CvBridgeError

class VoiceMaster():
    '''
    监听语音的主控，用于演示触发端茶，回家的功能
    '''
    def __init__(self):
        '''
        初始化
        '''        
        self.command_sub = rospy.Subscriber("/voice_system/move_topic", Int32, self.voicecommand_cb, queue_size=1)  
        self.fetchtea_client = rospy.ServiceProxy('s_fetchtea', scene)
        self.gohome_client = rospy.ServiceProxy('s_gohome', scene)
        
    def voicecommand_cb(self, asr_msg):
        command_str = asr_msg.data;
        print 'command:'
        print command_str;
        if command_str == 9:
            rospy.loginfo('send goal')
            self.call_fetchtea_service(1,'goal')
        elif command_str == 8:
            rospy.loginfo('send home')
            self.call_fetchtea_service(1,'home')
        else:
            print "invalid command"
        
    def call_fetchtea_service(self, type,param):
        '''
        自主行为服务控制
        :param type:1,表示启动;0,表示关闭
        '''
        rospy.wait_for_service('s_fetchtea')
        try:            
            p = param 
            respon = self.fetchtea_client(type, param);
            return True
        except rospy.ServiceException, e:
            print "Service call failed: %s" % e
            return False
        
if __name__ == '__main__':
    try:
        rospy.init_node('mx_fetch_tea_main', anonymous=False)
        rospy.loginfo("Init mxBot fetch tea main")   
        VoiceMaster()
        rospy.spin()
    except rospy.ROSInterruptException:
        rospy.loginfo("End mxBot fetch tea main")

