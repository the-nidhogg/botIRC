#!/usr/bin/python
# -*- coding: utf-8 -*-
from messages import insultes



class Msg:
	def __init__(self, message):
		self.msg = message
		self.msg = self.msg.decode("cp1252")
		self.msg = self.msg.encode("utf-8")
		self.low = self.msg.lower()
		self.no_accent = self._no_accent()
		self.alphanum = ''.join([i for i in self.msg if i.isalnum() or i == ' '])
		self.is_a_command = self.msg[0] == '!'
		if self.is_a_command:
			self.command = self.msg[1:].split(' ')
		self.is_a_quit = self._is_a_quit()
		self.is_insulting = self._insulting()

	def __repr__(self):
		return self.msg

	def __getitem__(self, no):
		return self.low[no]

	def _no_accent(self, word = ''):
		if not word:
			word = self.low
		dico = {"ÀÂÄàâä":'a',"ÉÈÊËéèëê":'e', "ÌÎÏìîï":'i', "ÖÔÒòöô":'o',
			"ÜÙÛùûü":'u', "ŶŸỲỳŷÿ":'y', "çÇ":'c',"œ":"oe"}
		final = word
		for ens in dico:
			for accentuees in ens:
				final = final.replace(accentuees,dico[ens])
		return final

	def _is_a_quit(self):
		for i in ("casse-toi", "casse toi", "pars",
				"barre-toi","barre toi", "dégage", 
				"fuis", "déguerpis", "va-t-en", 
				"file", "dehors", "tu sors"):
			if i in self.low or i.replace(" toi"," tio").replace("-toi","-tio") in self.low:
				return 1
		return 0

	def _is_a_shut_up(self):
		for i in ("ta gueulle", "ta geulle", "ta guelle", "ta gelle",
			"ta gueule", "ta geule", "ta guele", "taggle","chut",
			"tais-toi","tai-toi","tais toi","tai toi"):
			if i in self.low or i.replace("ta ","at ").replace("tai","tia")\
				.replace(" toi"," tio")in self.low:
				return 1
		return 0

	def addressed_to(self, pseudo, users = []):
		if self.low[:len(pseudo)] == pseudo.lower():
			return 1
		if ",%s"%pseudo.lower() in self.low.replace(' ', ''):
			return 1
		if " %s"%pseudo.lower() in self.low:
			return 1
		if users:
			for i in users:
				if self.addressed_to(i):
					return -1
		return 0

	def _insulting(self):
		self.insulte = []
		for i in insultes.get():
			if i in self.low:
				self.insulte.append(i)
			#for j in self.low.split(' '):
				#a = self._comp(j,i)
				#if a:
		return self.insulte
