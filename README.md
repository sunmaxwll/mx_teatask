启动步骤 

1.启动语音 

roslaunch voice_bringup voice_bringup.launch 

4.启动端茶任务 

roslaunch mx_fetchtea mx_fetchtea.launch 

5.通过rviz pose estimate设定机器人定位初始点，然后遥控机器人知道粒子云收敛 

6.指定厨房位置，通过启动的rviz，通过publish point来选取一个点，rviz上会显示Kitchen文字在rviz里 

对麦克风说话：出去 

机器人反应：到机器人指定的厨房位置 

对麦克风说话：回家 

机器人反应：到机器人指定的机器人原点位置 

修改：阳光明媚 2018.05.20 

感谢原作者spark机器人与ROS小课堂整合的语音识别系统。 

