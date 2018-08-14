#!/usr/bin/env python
#coding=utf8

# license removed for brevity
import requests
import itchat
import rospy
roskey = u'ROS'
group_name = u'政校企合作业务部'

from std_msgs.msg import String
from itchat.content import *
@itchat.msg_register(TEXT,isGroupChat=True)

def wcMsg(msg): 
    global roskey
    global group_name
    tts = rospy.Publisher('/voice_system/tts_topic', String, queue_size=10)
    nlu = rospy.Publisher('/voice_system/nlu_topic', String, queue_size=10)
    rospy.init_node('weChat2ROS', anonymous=True)
    rate = rospy.Rate(10) # 10hz
    group  = itchat.get_chatrooms(update=True)	 
    for g in group:
          if g['NickName'] == group_name:#从群中找到指定的群聊
	          group_id = g['UserName']
                  msg0 = msg['Text']    
		  break

    if msg0[0:10] == u'chchatroom':  	
	group_name = msg0[10:]
	itchat.send(u'控制群聊名已修改为'+group_name ,'filehelper')
    if msg0[0:8] == u'chroskey':  	
        roskey = msg0[8:]
	itchat.send(u'控制关键词已修改为'+roskey ,'filehelper')
        
    if msg0[0:6] == u'roskey':
        itchat.send(u'当前控制关键词为'+roskey ,'filehelper')
  	  	
    l = len(roskey)
    msg1 = msg0[0:l]
    msg2 = u''
    if msg1 == roskey:
    	msg2 = msg0[l:]
    	itchat.send(u'@%s\u2005 %s' % (msg['ActualNickName'], u'您的指令“'+msg2+u'”已发送成功'), group_id)
    if msg0 == u'roskey':
	itchat.send(u'@%s\u2005 %s' % (msg['ActualNickName'], u'当前控制关键词为'+roskey), group_id)
    
    if msg2== u'前进' and msg1 == roskey: 
        itchat.send(u'ROS机器人-前进中', 'filehelper')

    if msg2== u'后退' and msg1 == roskey: 
        itchat.send(u'ROS机器人-后退中', 'filehelper')

    if msg2 == u'右转' and msg1 == roskey:
        itchat.send(u'ROS机器人-右转中', 'filehelper')

    if msg2 == u'左转' and msg1 == roskey:
        itchat.send(u'ROS机器人-左转中', 'filehelper')

    if msg2== u'停' and msg1 == roskey:
        itchat.send(u'ROS机器人-不走了', 'filehelper')

    if msg1 == roskey:
	    tts.publish(msg2)
	    nlu.publish(msg2)
	    rate.sleep()
    msg0 = u''
	    
    return


if __name__ == '__main__':
    itchat.auto_login(True)
    itchat.run()
