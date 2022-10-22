from pepper_cmd import *
import pepper_cmd
import os
import sys
import time
import csv
import wave
import contextlib
import math
from numpy.random import choice
def start_interaction():
    Dialogue.say("Hi,I'm pepper, touch my head to interact with me!.")
    return Gestures.head_interaction(wait_ = 10.0) # waiting for python touch_sim.py --sensor HeadMiddle

begin()
class InitRobot():

	def __init__(self, alive=True, speed=200):
		pepper_cmd.robot.setAlive(alive)
		pepper_cmd.robot.tts_service.setParameter("speed", 200)
  
class Gestures:
	def __init__(self, touched=False):
		InitRobot(speed=100)
		# joint angles should be given in radians
		# 0 -  HeadYaw,        1 -  HeadPitch
		# 2 -  LShoulderPitch, 3 -  LShoulderRoll, 4 -  LElbowYaw, 5 -  LElbowRoll, 6 -  LWristYaw
		# 7 -  RShoulderPitch, 8 -  RShoulderRoll, 9 -  RElbowYaw, 10 - RElbowRoll, 11 - RWristYaw
		# 12 - LHand,          13 - RHand, 		 14 - HipRoll, 	 15 - HipPitch,   16 - KneePitch
		self.jointNames = ["HeadYaw", "HeadPitch",
                     "LShoulderPitch", "LShoulderRoll", "LElbowYaw", "LElbowRoll", "LWristYaw",
                     "RShoulderPitch", "RShoulderRoll", "RElbowYaw", "RElbowRoll", "RWristYaw",
                     "LHand", "RHand", "HipRoll", "HipPitch", "KneePitch"]
		self.touched = touched

	def change_pose(self, indices, values, pose):
     
		for idx, val in zip(indices, values):
			pose[idx] = val
		pepper_cmd.robot.setPosture(pose)
		
		return pose

	def head_interaction(self, wait_=20.0):

		curr_time = time.time()  # start timer

		pepper_cmd.robot.startSensorMonitor()
		print("Waiting a touch to start during {} seconds...".format(wait_))
		while not self.touched and (time.time() - curr_time < wait_):
			p = pepper_cmd.robot.sensorvalue()
			self.touched = (p[3] > 0)  # head touch sensor
		pepper_cmd.robot.stopSensorMonitor()

		if self.touched:
			print("A touch is detected.")
			pose = pepper_cmd.robot.getPosture()
			self.change_pose([0, 1], [0.0, -0.5], pose, sleeping_time=1.0)
			pepper_cmd.robot.normalPosture()
			print("Pose is back to normal.")

		return self.touched

	def sayhi(self):
		a=math.pi/180
  
		self.change_pose([7,8,10], 
							[-20*a,-90*a,120*a],
							pepper_cmd.robot.getPosture())
		self.change_pose([7,8,10],
							[-20*a,-90*a,60*a],
							pepper_cmd.robot.getPosture())

		return pepper_cmd.robot.getPosture()
class Dialogue:

	def __init__(self, speed=100):
		InitRobot(speed=speed)

	def say(self, sentence, require_answer=False, sleeping_time=0.0):
		pepper_cmd.robot.say(sentence)
		if require_answer:
			return self.listen(timeout=30)
		if sleeping_time:
			time.sleep(sleeping_time)

	def listen(self, vocabulary=["Play, Indication"], timeout=30):
		answer = pepper_cmd.robot.asr(vocabulary=vocabulary, timeout=timeout)
		while not answer:
			answer = self.say(
				sentence="Sorry, I did not hear you, repeat please.", require_answer=True)
		return answer
end()