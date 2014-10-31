#!/usr/bin/python
# -*- coding: utf-8 -*-

from threading import Thread
from time import sleep

class Timer:
	def __init__(self, function, *args):
		self.action = {"timer1":{"function":function, "working":True, "args":args}}
		self.killed = False
		Thread(target = self.thread).start()

	def __add__(self, function, *args, **kwargs):
		no = "timer"+str(len(self.action)+1)
		self.action[no]={"function":function,
		"working":True, "args":args}
		for i in kwargs:
			self.action[no][i] = kwargs[i]

	def start(self, action):
		self.action[action]["working"] = True

	def stop(self, action):
		self.action[action]["working"] = False

	def switch(self, action):
		self.action[action]["working"] = not self.action[action]["working"]

	def state(self, action):
		return self.action[action]["working"]

	def end(self):
		self.killed = True

	def thread(self):
		while not self.killed:
			sleep(0.75)
			for i in self.action:
				if self.action[i]["working"]:
					self.action[i]["function"](*self.action[i]["args"])
