# ros_itchat
##ros_wechat微信个人ROS互动
*可以通过微信聊天的形式和机器人互动，任何人给登录者微信发消息都可以控制ROS机器人并得到回复
1.打开 首先打开一个终端，运行roscore启动ros节点管理器
2.快捷打开，切换到 ros_wechat.py 文件所在目录，python ros_wechat.py打开
3.通过微信扫吗登录微信网页版，当提示 start autoreplay就可以在微信群里和ROS机器人互动了。
4.修改控制关键词 chroskey+关键词  例如：roskeyR，就可以通过“R前进”，“R后退”来和机器人互动。
5.输入roskey可以获取当前控制指令关键词
##ros_wechatroom微信群ROS互动
*可以通过在某个群中的聊天来和机器人互动
1.打开 首先打开一个终端，运行roscore启动ros节点管理器
2.快捷打开，切换到 ros_wechatroom.py 文件所在目录，python ros_wechatroom.py打开
3.通过微信扫吗登录微信网页版，当提示 start autoreplay就可以在微信群里和ROS机器人互动了。
4.修改控制关键词 chroskey+关键词  例如：roskeyR，就可以通过“R前进”，“R后退”来和机器人互动。
5.修改所在群聊，chchatroom+群聊名 就可以从一个群切换到另一个群
6.输入roskey可以获取当前控制指令关键词


