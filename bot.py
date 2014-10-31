#!/usr/bin/python
# -*- coding: utf8 -*-

from urllib import urlretrieve
from time import sleep, localtime, time
from random import randrange, choice

import irclib
import ircbot

from messageStyle import *
from parseWebPages import *
from timer import *
from messages import *
from ascii_art import *

# ban insultes; bataille naval
# high five = _o/\o_


class Bot(ircbot.SingleServerIRCBot):
	def __init__(self):
		self.pseudo = "Cuillere"
		#self.chan = "#testircbot"
		self.chan = "#iut_bio"
		self.master = "lain"
		self.id_master = 1675114644
		self.times_actions = {
			(00, 00, 00):lambda self:self.msg("Minuit! L'heure du criiiiiiiime!!!!"+choice(smiley.peur())if randrange(2)else""),
			(12, 00, 00):lambda self:self.msg("C'est l'heure de mangeeeeer!!!!"+choice(smiley.gentil())if randrange(2)else""),
			(16, 30, 00):lambda self:self.msg("C'est l'heure du goûteeeeeeer!!!!"+choice(smiley.gentil())if randrange(2)else""),
			(20, 00, 00):lambda self:self.msg("C'est l'heure du repas du soiiiir!!!!"+choice(smiley.gentil())if randrange(2)else"")}
		self.timer = Timer(self.timer_function)
		self.timer + self.timer_fonction2
		self.pendu = False
		self.allwords = open("allwords.txt", 'r').read().split('\n')
		self.load_id()
		self.question = ""
		self.time_to_waite_init = 600
		self.time_to_waite = self.time_to_waite_init
		ircbot.SingleServerIRCBot.__init__(self, [("irc.epiknet.org", 6667)],
			self.pseudo, "Petite cuillere en plastique, marque: monoprix")
		self.historique = []

	def load_id(self):
		print ">>> Chargement des ID"
		self.caracteristiques = {}
		with open("caracteristiques", 'r') as f:f=f.readlines()
		for i in f:
			ident = i.split(' ')[0]
			self.caracteristiques[ident] = eval(i[len(ident)+1:])
		with open("corresp", 'r') as f:self.corresp = eval(f.read())

	def save_id(self):
		print ">>> Sauvegarde des ID"
		with open("caracteristiques", 'w')as f:
			for i in self.caracteristiques:
				f.write(str(i)+' '+str(self.caracteristiques[i])+'\n')
		with open("corresp", 'w') as f:f.write(str(self.corresp))

	def timer_function(self, *args):
		"""fonction du timer: j'affiche des messages à certaines
			heures (messages contenu dans self.times_actions)"""
		heure, minute, sec = tuple(localtime()[3:6])
		if (heure, minute, sec) in self.times_actions:
			self.times_actions[(heure, minute, sec)](self)

	def timer_fonction2(self, *args):
		"""J'execute les actions cycliques"""
		# améliorer:
			#je m'ennuie:
				#proposer un truc
				#highlighter les gens
		#quand je m'ennuie:
		if not "timer_last_msg" in dir(self):
			self.timer_last_msg = time()
		elif time() - self.timer_last_msg >= self.time_to_waite:
			self.time_to_waite *= 1.5
			self.timer_last_msg = time()
			msg = choice(msgEnnui.ennui()+(msgEnnui.pendu()if not self.pendu else(msgEnnui.finPendu())))
			if msg[-1] == '?':
				self.question = msg
			self.msg(msg)

		"""partie de downgrade des counteurs"""
		# count de "casse-toi"
		if not "timer_last_down_quit" in dir(self):
			self.timer_last_down_quit = time()
		elif time() - self.timer_last_down_quit >= 600:
			for i in self.caracteristiques:
				if self.caracteristiques[i]["count_quit"]:
					self.caracteristiques[i]["count_quit"] -= 1

	def on_welcome(self, serv, ev):
		"""quand j'arrive, je:
				- dit bonjour"""
		#ameliorer:
			#si je reconnais des gens:
				#leur dire bonjour en fonction de l'affection que j'ai pour eux
		serv.join(self.chan)
		self.server = serv

	def on_pubmsg(self, serv, ev):
		"""À chaque message, si commande:
				- j'envoie à self.command()
			sinon:
				- si message de maître:
					j'envoie à self.masterMsg()
				- sinon:
					j'envoie à self.message()"""
		self.users = self.channels[self.chan].users()
		self.users.remove(self.pseudo)
		self.timer_last_msg = time()
		self.time_to_waite = self.time_to_waite_init
		msg = Msg(ev.arguments()[0])
		nick = irclib.nm_to_n(ev.source())
		identifiant = self.get_id(irclib.nm_to_h(ev.source()),nick)
		if nick == self.pseudo:return
		if msg.is_a_command:
			for i in msg.command:
				self.command(i, nick, identifiant)
		else:
			self.historique.insert(0,{"msg":msg,"nick":nick,"id":identifiant})
			(self.message(msg,nick,identifiant)if nick!=self.master and hash(identifiant)!=self.id_master else self.masterMsg(msg,nick,identifiant))

	def on_join(self, serv, ev):
		""" je dis bonjour aux personnes qui joignent le chan (je suis poli, et gentil!)"""
		#ameliorer:
			#ajouter notion d'affection (grrrrr!!!! è_é / <3 *keur!! keur!!*)
			#ajouter notion de "tiens, ça faisait longtemps/tiens, j't'ai jamais vu, toi!
			#minimum = -10000; max: 10000
		nick = irclib.nm_to_n(ev.source())
		if hash(irclib.nm_to_h(ev.source())) == self.id_master:
			self.masque = irclib.nm_to_h(ev.source())
			self.msg(choice(salutation.all()).capitalize()+choice(personnes)+choice(smiley.gentil()))
			return
		#if nick != self.pseudo:
			#self.msg(choice(salutation.gentil())+", %s !! "%(nick if nick!=self.master else"Maître")+choice(smiley.gentil()))
		else:
			identifiant = self.get_id(irclib.nm_to_h(ev.source()),nick)
			print ">>> %s a rejoin le chan %s"%(nick, self.chan)
			for i,j in enumerate(((-10000, -100),(-99, -50), (-50, -10), (100, 10000),(50, 99), (10, 50), (-9, 9))):
				if j[0]<self.caracteristiques[identifiant]["love"]<j[1]:
					msg = choice((salutation2.salut["exclamation_colere3"],salutation2.salut["exclamation_colere2"],
					salutation2.salut["exclamation_colere1"],salutation2.salut["exclamation_joie3"],
					salutation2.salut["exclamation_joie2"],salutation2.salut["exclamation_joie1"],
					salutation2.salut["exclamation_neutre"])[i])
					break
			if "%s" in msg:
				msg%=nick
			self.msg(msg)
		self.save_id()

	def on_nick(self, user, new):
		old = irclib.nm_to_n(new.source())
		nick = new.target()
		identifiant = self.get_id(irclib.nm_to_h(new.source()),nick)
		print ">>> %s changé son pseudo en %s"%(old,nick)
		if nick not in self.caracteristiques[identifiant]["other"]:
			self.caracteristiques[identifiant]["other"].append(nick)
		if self.no_AFK_anymore(old, nick):
			self.msg("Re, %s!!"%nick)
		elif self.is_AFK(old, nick):
			self.msg("A+, %s!!"%old)
		self.caracteristiques[identifiant]["nick"] = nick

	def get_id(self, ident, nick = ''):
		#identifiant = hash(ident)
		if ident in self.corresp:
			return self.corresp[ident]
		elif ident in self.caracteristiques:
			return ident
		elif nick:
			for i in self.caracteristiques:
				if self.caracteristiques[i]["main"] == nick:
					master = self.caracteristiques[self.masque]["nick"]
					self.msg("multiple ID pour unique pseudo: %s"%nick, master)
					if raw_input("Fusionner %s ? [y / n]"%nick) in " y":
						self.corresp[ident] = i
					return i
			self.add_person(nick, ident)
			self.save_id()
			return ident

	def no_AFK_anymore(self, old, new):
		"""sors de l'état "AFK"""
		old, new = old.lower(), new.lower()
		for afk in "afk","away","parti","dors","gaming","sleep","sleeping":
			if afk in old and (afk not in new or "not_"+afk+"_anymore"in new):
				return 1

	def is_AFK(self, old, new):
		"""entre dans l'état "AFK"""
		old, new = old.lower(), new.lower()
		for afk in "afk","away","parti","dors","gaming","sleep","sleeping":
			if afk not in old and afk in new:
				return 1

	def masterMsg(self, msg, nick, identifiant):
		# améliorer:
			#ajouter d'autres truc..
		print ">>> Message de Lain reçu: %s"%msg
		if self.question:
			self.answer_question(msg, nick, identifiant)
		if hash(identifiant) != self.id_master:
			self.love(identifiant, -10)
			msg("Vous n'êtes pas mon maître!!!")
		elif msg.addressed_to(self.pseudo, self.users) in (1,0) or self.search_cible(nick) == self.pseudo:
			if msg.is_a_quit:
				self.msg("Oui, maître.")
				self.quit()
		if msg.is_insulting:
				self.insulting_msg(msg, nick, identifiant)

	def message(self, msg, nick, identifiant):
		# améliorer:
			#traiter chaque message
			#traiter les messages differemment en fonction de la personne
		"""si le message me dit de partir, j'envoie le nick et l'id à told_me_to_quit()"""
		print ">>> Message de %s reçu: %s"%(nick,msg)
		if self.question:
			self.answer_question(msg, nick, identifiant)
		elif msg.addressed_to(self.pseudo, self.users) or self.search_cible(nick) == self.pseudo:
			if msg.is_a_quit:
				self.told_me_to_quit(nick, identifiant)
			if msg.is_insulting:
				self.insulting_msg(msg, nick, identifiant)

	def told_me_to_quit(self, nick, identifiant):
		"""Si le message me dit de partir:
				j'ajoute la personne au counteur de personnes qui
				me disent de partir.
				Puis, l'envoie ballader ou obéis, c'est au hasard...
			Si il me demande de partir trop souvent, j'ignore ses messages et l'insulte.
			Biensur, les personne qui me disent de dégager, je finis par ne plus les aimer..."""
		if identifiant not in self.caracteristiques:
			self.add_person(nick, identifiant)
		self.caracteristiques[identifiant]["count_quit"] += 1
		self.caracteristiques[identifiant]["total"] += 1
		msg = choice(msgNoQuit.all())
		if msg:
			msg+=''if msg=="..."else choice(smiley.desabuse()+smiley.mechant()if msg!="Nope!"else smiley.gentil())
			self.msg(msg)
			self.love(identifiant, -5)
		else:
			self.love(identifiant, -1)
			self.msg(choice(msgQuit)+choice(smiley.desabuse()))
			self.quit()

	def insulting_msg(self, msg, nick, identifiant):
		print "insultant: %s"%msg
		#print "reconnu comme: %s"%unicode([i.decode("utf-8") for i in msg.is_insulting])
		cible = ""
		for i in msg.alphanum.split(' '):
			for j in self.caracteristiques:
				if i == self.caracteristiques[j]["main"] or i in self.caracteristiques[j]["other"]:
					cible = i
					ident = j
					break
			if cible:break
		if not cible:
			cible = self.search_cible(nick)
		else:
			cible = (cible, ident)
		if cible[1]:
			if cible[0] == self.pseudo:
				self.insult_me(nick, identifiant, msg)
			else:
				msg_retour = choice(insultes.to(self.get_bad_good(identifiant, cible[1])))\
					.replace("%1", nick).replace("%2",cible[0]).replace("%3", choice(msg.is_insulting))
				self.msg(msg_retour)
				if has(identifiant) != self.id_master:
					love = insultes.get_love(self.get_bad_good(identifiant, cible[1]))
					self.love(identifiant, love[0])
					self.love(cible[1], love[1])
		print "cible: %s"%cible[0]

	def insult_me(self, nick, identifiant, msg):
		if hash(identifiant) == self.id_master:
			self.msg(choice(smiley.triste()))
		else:
			love = self.caracteristiques[identifiant]["love"]
			self.love(identifiant, -5 if love>9 else -15 if love<-9 else -10)
			insult = choice(msg.is_insulting)
			if insultes.get()[insult] == 0:
				self.msg("TOI, %s"%insulte)
			elif insultes.get()[insult] == 1:
				self.msg("C'est toi, l'%s"%insulte)

	def get_bad_good(self, id1, id2):
		return (1 if self.caracteristiques[id1]["love"]>9 else 0\
		if-9<=self.caracteristiques[id1]["love"]<=9 else-1,\
		1 if self.caracteristiques[id2]["love"]>9 else 0\
		if-9<=self.caracteristiques[id2]["love"]<=9 else-1)

	def search_cible_insulte(self, nick):
		for i in xrange(1,len(self.historique)):
			if self.historique[i]["msg"].is_insulting:
				if self.historique[i+1]["nick"]!=nick:
					return self.historique[i+1]["nick"],self.historique[i+1]["id"]
		return self.search_cible(nick)

	def search_cible(self, nick):
		for i in xrange(1,len(self.historique)):
			if self.historique[i]["nick"]!=nick:
				return self.historique[i]["nick"],self.historique[i]["id"]
		return "#inconnu",None

	def search_id(self, nick, not_id = None):
		for i in self.historique:
			if nick == self.historique[i]["main"]:
				if self.historique[i]["id"] not in not_id:
					return self.historique[i]["id"]
		for i in self.historique:
			if nick in self.historique[i]["other"]:
				if self.historique[i]["id"] not in not_id:
					return self.historique[i]["id"]

	def answer_question(self, msg, nick, identifiant):
		msg = msg.low
		msg = ''.join([msg[i] for i in range(len(msg)-1) if msg[i]!=msg[i+1]])+msg[-1]
		print "C'est une réponse à la question \"%s\""%self.question
		if self.question in msgEnnui.pendu():
			if [0 for i in reponses.positif()if i in msg]:
				print "Réponse positive"
				self.love(identifiant, 5)
				self.msg(choice(humeur.heureu()))
				self.init_pendu()
				self.pendu = True
			elif [0 for i in reponses.negatif()if i in msg]:
				print "Réponse negative"
				self.love(identifiant, 1)
		self.question = ""

	def command(self, command, nick, identifiant):
		#améliorer:
			#modifier les probabilités de faire une commande
			#en fonction de l'affection
		print ">>> Commande reçu par %s."%nick
		if command == "dtc":
			print "DTC"
			self.msg(getDTC()[0])
			self.love(identifiant, 2)
		elif command == "vdm":
			print "VDM"
			self.love(identifiant, 1)
			self.msg(getVDM())
		elif command == "timer":
			print "timer"
			self.timer.switch("timer1")
			self.msg("timer is "+("on." if self.timer.state("timer1") else "off."))
		elif command == "quit":
			print "quit"
			if hash(identifiant) == self.id_master:
				self.quit()
			else:
				self.love(identifiant, -1)
				self.msg("%s est mon seul Maître."%self.master+choice(smiley.gentil()))
		elif command == "smiley":
			print "smiley"
			self.love(identifiant, 1)
			self.msg(choice(smiley.all())if nick==self.master or randrange(10)else"Nan, pas envie."+choice(smiley.mechant()+smiley.desabuse()))
		elif command[:7]=="smiley_":
			print "smiley_[classe]"
			self.love(identifiant, 2)
			if command[7:] not in smiley.smiley:return
			self.msg(choice(smiley.smiley[command[7:]])if nick==self.master or randrange(10)else"Nan, pas envie."+choice(smiley.mechant()+smiley.desabuse()))
		elif command == "love":
			print "love %s: %.1f"%(nick, self.caracteristiques[identifiant]["love"])
			if "love" in self.caracteristiques[identifiant]:
				self.msg("/me aime %s à %.1f / 10000"%(nick, self.caracteristiques[identifiant]["love"]))
			else:
				self.caracteristiques[identifiant]["love"] = 0
				self.msg("/me aime %s à %.1f / 10000"%(nick, self.caracteristiques[identifiant]["love"]))
		elif command == "pendu":
			print "pendu"
			self.love(identifiant, 3)
			self.init_pendu()
			self.pendu = True
		elif command == "help":
			print "help"
			self.print_help(identifiant, nick)
		elif self.pendu:
			self.pendu_lettre(command, nick, identifiant)
		else:
			print "Commande inconnue..."

	def init_pendu(self):
		print ">>> Début du pendu: initialisation"
		if "pendu_word" not in dir(self):self.pendu_word = choice(self.allwords).lower()
		if "lettre" not in dir(self):self.lettres = " "
		if "pendu_stat" not in dir(self):self.pendu_stat = 0
		self.new_pendu()
		self.msg(''.join([(i if i in self.lettres else '*') for i in self.pendu_word]))

	def print_help(self, identifiant, nick):
		print ">>> Affichage de l'aide pour %s"%nick
		aide = """!dtc: j'affiche un dtc aléatoire;\n!vdm j'affiche une vdm aléatoire;
!timer: active/désactive le timer qui me permet d'afficher des truc à certaines heures;
!quit: me fais partir... :'( ;\n!smiley: j'affiche un smiley aléatoire! ^^;
!smiley_classe: j'affiche un smiley d'une certaine classe. Les classes disponibles sont:\n"""+\
'\n'.join(["\t-"+i for i in smiley.smiley.keys()])+';\n'+"""!love: j'affiche à quel point je vous affectionne! :$ *rougis* ;
!pendu: lance un pendu. Les commandes du pendu sont:
	-!lettre: utilisation d'une lettre
	-!used: j'affiche les lettres déjà dîtes
	-!word: j'affiche le mot (avec des * pour les lettre cachées)
	-!abandon: j'affiche le mot en clair, et vous avez perdu (le principe d'un abandon, quoi...)
	-!stop: j'arrète le pendu (reprise possible avec !pendu)."""
		if hash(identifiant) != self.id_master:
			if self.caracteristiques[identifiant]["help_given"]:
				self.server.privmsg(nick, aide)
			elif not randrange(5):
				self.caracteristiques[identifiant]["help_given"] = True
				self.server.privmsg(nick, aide)
				self.save_id()
			else:
				self.caracteristiques[identifiant]["help_given"] = True
				self.msg("Tu veux un coup d'main?")
				self.msg("J'ai pas d'main.")
				self.msg("Par contre, des bits j'en ai plein!")
				self.save_id()
				return
		for i in aide.split('\n'):
			self.server.privmsg(nick, i)

	def pendu_lettre(self, lettre, nick, identifiant):
		#modifier:
			#enregistrement des scores en fonction de la personne et non du pseudo
		if len(lettre) != 1:
			print ">>> Commande du pendu"
			if lettre == "used":
				print "Affichage des lettres utilisees"
				self.msg("Lettres utilisées: "+' '.join(sorted(self.lettres)))
				return
			elif lettre == "word":
				print "Affichage du mot"
				self.msg(''.join([(i if i in self.lettres else '*') for i in self.pendu_word]))
				return
			elif lettre == "abandon":
				print "Abandon du pendu par %s."%nick
				self.love(identifiant, -5)
				self.msg("Le mot était: \"%s\"..."%(self.pendu_word)+choice(smiley.gentil()))
				self.new_pendu()
			elif lettre == "stop":
				print "Pendu quitté pas %s."%nick
				self.msg("Le mot était: \"%s\"..."%(self.pendu_word)+choice(smiley.gentil()))
				self.pendu = False
			elif lettre not in "ÀÂÄàâäÉÈÊËéèëêÌÎÏìîïÖÔÒòöôÜÙÛùûüŶŸỲỳŷÿçÇœ":
				return
		if lettre in self.lettres:
			print "Lettre déjà utilisée..."
			self.love(identifiant, -1)
			return
		elif lettre in self.pendu_word:
			print "Lettre trouvée par %s: %s"%(nick,lettre)
			self.lettres+=lettre
			self.love(identifiant, 2)
			if not [x for x in self.pendu_word if x not in self.lettres]:
				self.love(identifiant, 5)
				self.msg(''.join([(i if i in self.lettres else '*') for i in self.pendu_word]))
				self.msg("Gagné!!!")
				self.msg("Félicitation, %s!!"%nick)
				print "Pendu gagné par %s."%nick
				self.command("love", nick, identifiant)
				self.pendu = False
				return
		else:
			print "Lettre non présente dans le mot..."
			self.love(identifiant, -0.5)
			self.pendu_stat += 1
			try:self.print_pendu()
			except:
				self.love(identifiant, -5)
				print "Pendu perdu par %s."%nick
				self.msg("Perdu!!\nLe mot était: \"%s\"."%(self.pendu_word)+choice(smiley.gentil()))
				self.command("love", nick, identifiant)
				return self.new_pendu()
			self.lettres+=lettre
		self.msg(''.join([(i if i in self.lettres else '*') for i in self.pendu_word]))

	def print_pendu(self):
		print "Affichage du pendu"
		self.msg(pendu[self.pendu_stat])

	def new_pendu(self):
		print "Nouveau pendu"
		self.pendu_word = choice(self.allwords).lower()
		self.lettres = " "
		self.pendu_stat = 0

	def msg(self, msg, target=''):
		if not target:target = self.chan
		if '\n' in msg:
			for i in msg.split('\n'):
				self.msg(i)
		else:
			if msg[:3] == "/me":
				self.server.action(target, msg[4:])
			else:
				print ">>> Message envoyé: %s"%msg
				self.historique.insert(0,{"msg":msg,"nick":self.pseudo,"id":self.masque})
				self.server.privmsg(target, msg)

	def kick(self, pseudo, canal="", raison=''):
		print ">>> Kick de %s"+'' if not raison else" pour %s"%raison
		if not canal:
			canal = self.chan
		self.server.kick(pseudo, canal, raison)

	def add_person(self, nick, identifiant) :
		print ">>> Ajout d'un nouvelle personne: %s"%nick
		self.caracteristiques[identifiant] = {"main":nick,"other":[],"nick":nick,
		"help_given":False, "score_pendu":0,"count_quit":0, "total":0,"love":0, "last_co":time()}
		self.save_id()

	def love(self,ident, count):
		print ">>> Modification des love stats de %s (%s%.1f)"%(self.caracteristiques[ident]["main"],(''if count>0 else'-'),count)
		if "love" in self.caracteristiques[ident]:
			self.caracteristiques[ident]["love"] += count
		else:
			print self.caracteristiques[ident], ident
		self.save_id()

	def quit(self):
		#améliorer
			#ajouter un message au /quit
		self.save_id()
		heure = localtime()[3]
		horaires = {(17, 21):"Bonne soirée", (4, 12): "Bonne journée", (13, 16):"Bonne après-midi"}
		for debut, fin in horaires.keys():
			if debut <= heure <= fin:
				self.msg(horaires[(debut, fin)]+choice(personnes)+choice(smiley.gentil()))
				self.timer.end()
				quit()
		self.msg("Bonne nuit"+choice(personnes)+choice(smiley.gentil()))
		self.timer.end()
		print ">>> Quit"
		quit()


if __name__ == "__main__":
	Bot().start()














