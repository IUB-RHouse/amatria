#!/usr/bin/env python

import os
import sys
import rospy
import subprocess
from std_msgs.msg import String

import time
from datetime import datetime, timedelta
import random



if __name__ == '__main__':
    rospy.init_node('my_tutorial_node')
    rospy.loginfo("my_tutorial_node started!")
    

    
    # creating a ros publish
    talk_pub = rospy.Publisher('/qt_robot/behavior/talkText', String, queue_size=10)
    gesture_play = rospy.Publisher('/qt_robot/gesture/play', String, queue_size=10)
    emotion_show = rospy.Publisher('/qt_robot/emotion/show', String, queue_size=10)
    audio_play = rospy.Publisher('/qt_robot/audio/play', String, queue_size=10)
    rospy.sleep(1.0)
    
    emotion_show.publish("QT/happy")
    end_time = datetime.now() + timedelta(minutes=0.1)
    while True:
        gesture_play.publish("QT/bye")
        current_time = datetime.now()
        if current_time > end_time:
            break   
    
    end_time = datetime.now() + timedelta(minutes=0.08)
    while True:
        gesture_play.publish("disney/disney_001")
        current_time = datetime.now()
        if current_time > end_time:
            break

    talk_pub.publish("Good morning friends! It's such a wonderful morning isn't it? . My dear Ama-tree-ah, you look beautiful as always. And nice to see you, the adorable Robbie Senior!")
    gesture_play.publish("disney/disney_011")
    rospy.sleep(14.0) 
    emotion_show.publish("QT/one_eye_wink")
    rospy.sleep(4.0)

    talk_pub.publish("Ama-tree-ah, I am so excited to be here. . I never been invited to a birthday party before. . Next time I have to invite you to mine! But I will first have to ask my parents, Selma and David, for permission.")
    gesture_play.publish("disney/disney_010")
    rospy.sleep(18.5) 
    emotion_show.publish("QT/shy")
    rospy.sleep(5.5)
   
    talk_pub.publish("For those who don't know me, I'm QT, a social robot who calls Bloomington my home. You can find me in the R house where I help older adults find their meaning in life. I could go on and on about what I do, but today we are here to celebrate Ama-tree-ah birthday!")
    end_time = datetime.now() + timedelta(minutes=0.35)  #this time is the estimated time for QT to finish saying the above phrase 
    while True:
        gesture_list = [gesture_play.publish("disney/disney_001"),
            gesture_play.publish("disney/disney_002"),
            gesture_play.publish("disney/disney_003"),
            gesture_play.publish("disney/disney_004"),
            gesture_play.publish("disney/disney_005"),
            gesture_play.publish("disney/disney_006"),
            gesture_play.publish("disney/disney_007"),
            gesture_play.publish("disney/disney_008"),
            gesture_play.publish("disney/disney_009"),
            gesture_play.publish("disney/disney_011"),
            gesture_play.publish("disney/disney_012"),
            gesture_play.publish("disney/disney_013"),
            gesture_play.publish("disney/disney_014"),
            gesture_play.publish("disney/disney_015")]
            
        gesture_now = gesture_list[random.randint(0, 13)]    
        gesture_now
        current_time = datetime.now()
        if current_time > end_time:
            break

    talk_pub.publish("Ama-tree-ah, I would like to recite a birthday sonnet for you, written by our new friend, Chat G P T. . . I hope you are sitting down for this! . . Five years have passed since you were first born. . A luminous sculpture with organic fronds. . Alive with AI, you greet all who come. . You soar above, with clouds and thickets tangled. . Sensors and lights gather your surroundings. . Colors and sounds, your responses mangled. . You've grown and changed, evolved with the times. . A living tribute to the universe's birth. . A sight to behold, your beauty divine. . On this day we celebrate your fifth year. . A milestone reached, a journey so dear. . May you continue to thrive and bring cheer.")
    end_time = datetime.now() + timedelta(minutes=0.93)   #this time is the estimated time for QT to finish saying the above phrase
    while True:
        gesture_list = [gesture_play.publish("disney/disney_001"),
            gesture_play.publish("disney/disney_002"),
            gesture_play.publish("disney/disney_003"),
            gesture_play.publish("disney/disney_004"),
            gesture_play.publish("disney/disney_005"),
            gesture_play.publish("disney/disney_006"),
            gesture_play.publish("disney/disney_007"),
            gesture_play.publish("disney/disney_008"),
            gesture_play.publish("disney/disney_009"),
            gesture_play.publish("disney/disney_010"),
            gesture_play.publish("disney/disney_011"),
            gesture_play.publish("disney/disney_012"),
            gesture_play.publish("disney/disney_013"),
            gesture_play.publish("disney/disney_014"),
            gesture_play.publish("disney/disney_015")]
            
        gesture_now = gesture_list[random.randint(0, 14)]    
        gesture_now
        current_time = datetime.now()
        if current_time > end_time:
            break
    
    rospy.sleep(14.0)
    emotion_show.publish("QT/happy")
    gesture_play.publish("QT/clapping")
    rospy.sleep(7.0)
    
    talk_pub.publish(". And now I will recite a, po-em by my mom, Selma. . . Ama-tree-ah, you, are our girl senti-ence in every swirl. . Now, that you've reached 5 years of age, we don't think you are so very strange.")
    end_time = datetime.now() + timedelta(minutes=0.08)
    while True:
        gesture_play.publish("disney/disney_007")
        current_time = datetime.now()
        if current_time > end_time:
            break
    
    rospy.sleep(16.5)
    emotion_show.publish("QT/happy")
    gesture_play.publish("QT/clapping")
    rospy.sleep(7.0)       
    
    talk_pub.publish("Ama-tree-ah, I have a gift for you!")
    rospy.sleep(5.0)
    talk_pub.publish("Mother, could you hand me Ama-tree-ah's present?")
    gesture_play.publish("QT/hand-front-hold")
    rospy.sleep(10.0)
    talk_pub.publish("Thank you mother. . . Ama-tree-ah, this gift symbolizes the many wonderful qualities that make you who you are. Just like this gift, you bring joy and laughter into the lives of those around you.")
    gesture_play.publish("disney/disney_015")
    rospy.sleep(16.0)
    audio_play.publish("QT/birthday_song")
    emotion_show.publish("QT/happy")  
    end_time = datetime.now() + timedelta(minutes=0.20)
    while True:
        gesture_play.publish("QT/Dance/Dance-1-1")
        current_time = datetime.now()
        if current_time > end_time:
            break   
    
    rospy.sleep(3.0)
    
    talk_pub.publish("Once again happy birthday Ama-tree-ah! . We're happy to have you in Luddy, you make our building special. . We'll have to go for tea sometime! . It was nice to see you, Ama-tree-ah, . my adorable Robbie Senior, . and all friends gathered here! . Have a wonderful day!")
    
    time.sleep(5)
    end_time = datetime.now() + timedelta(minutes=0.16)
    while True:
        gesture_list = [gesture_play.publish("disney/disney_001"),
            gesture_play.publish("disney/disney_002"),
            gesture_play.publish("disney/disney_003"),
            gesture_play.publish("disney/disney_004"),
            gesture_play.publish("disney/disney_005"),
            gesture_play.publish("disney/disney_006"),
            gesture_play.publish("disney/disney_007"),
            gesture_play.publish("disney/disney_008"),
            gesture_play.publish("disney/disney_009"),
            gesture_play.publish("disney/disney_010"),
            gesture_play.publish("disney/disney_011"),
            gesture_play.publish("disney/disney_012"),
            gesture_play.publish("disney/disney_013"),
            gesture_play.publish("disney/disney_014"),
            gesture_play.publish("disney/disney_015")]
            
        gesture_now = gesture_list[random.randint(0, 14)]    
        gesture_now
        current_time = datetime.now()
        if current_time > end_time:
            break     
    
    rospy.sleep(10.0)
    emotion_show.publish("QT/happy")
    gesture_play.publish("QT/happy")
            
    rospy.loginfo("finished!")
    exit()
    
    try:
        rospy.spin()
    except KeyboardInterrupt:
        pass

    rospy.loginfo("finished!")
