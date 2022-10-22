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
begin()
class InitRobot():

	def __init__(self, alive=True, speed=200):
		pepper_cmd.robot.setAlive(alive)
		pepper_cmd.robot.tts_service.setParameter("speed", 200)
  
class Gestures:
	def __init__(self, touched=False):
		InitRobot(speed=200)
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

	def change_pose(self, indices, values, pose, sleeping_time=0.5):

		joint_list = []
		for idx, val in zip(indices, values):
			pose[idx] = val
			joint_list.append(self.jointNames[idx])

		pepper_cmd.robot.setPosture(pose)
		

		return pose

	def monitor_touch(self, monitoring_time=20.0):

		curr_time = time.time()  # start timer

		pepper_cmd.robot.startSensorMonitor()
		print("Waiting a touch to start during {} seconds...".format(monitoring_time))
		while not self.touched and (time.time() - curr_time < monitoring_time):
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
  
		self.change_pose([7,8,10], #7 -> -20 ; 10 -> 90
							[-20*a,-90*a,120*a],
							pepper_cmd.robot.getPosture(),
							0.5)
		self.change_pose([7,8,10], #7 -> -20 ; 10 -> 90
							[-20*a,-90*a,60*a],
							pepper_cmd.robot.getPosture(),
							0.5)

		pepper_cmd.robot.green_eyes()
		return pepper_cmd.robot.getPosture()

end()