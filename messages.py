#!/usr/bin/python
# -*- coding: utf-8 -*-

from random import choice

from ascii_art import *


personnes = type('',(),{
"pers":(", les gens !! ","!! ",", tout le monde! ",", peuple de fRance! ",", bande de boulets! ",", les débiles! ",
", sales geeks!! ", ", et keur sur vous!! "," ","! "," "),
	"gentil":lambda self:self.pers[:3],
	"mechant":lambda self:self.pers[3:],
	"__repr__":lambda self:self.pers,
	"__len__":lambda self:len(self.pers),
	"__getslice__":lambda self,i,j:self.pers[i,j],
	"__getitem__":lambda self,i:self.pers[i]
	})()
"""

·◡- <3
"""

smiley = type('',(),{
"smiley":{
	"gentil":("=)", ":)","·◡·"),
	"joyeux":("^o^","^_^","=^_^=","^◡^"),
	"amour":("♥_♥","♥◡♥","*◡*"),
	"autres":("\n          _\n._.  |:  · ·  :|  ._.  <- bébé dans un lave-linge",
		"<o/  *supermaaaaan!!!*","\oμO/","\°o°/",
		"[\o/] *ouvre ses fenêtres*","\(*ϖ*)/"),
	"mechant":("to/",),
	"desabuse":("><",">︵<",">_<",".___.","u_u"),
	"triste":("é_è",";_;","'︵'"),
	"peur":("=0", "='o", ":o", ":'0",">~<", "'~'","°~°"),
	"gene":("=$",":$"),
	"moqueur":("=P",":P","·◡-"),
	"WTF":("o_O",),
	"idunno":("_       _\n \(ø_°)/",),
	"flopping_table":("-╯°□°）╯︵-┻━┻","(/｀ο´)/  ┫:’ﾟ:｡･,. 。゜","(ノ-o-)ノ⌒┳ ┫┻┣"),
	"put_table":(" ┬──┬◡ﾉ(° -°ﾉ)",),
	"flopping_guy":("(╯°Д°）╯︵/(.□ . )",),
	"flopping_fb":("(╯°□°)╯︵ ʞooqǝɔɐℲ",),
	"flopping_table_to":("(╯°□°）╯彡┻━┻  ◡(>_<◡)", "(╯°□°）╯    ┻━┻☆(>_<)/"),
	"bite":(bite,),
	"YSNP":(you_shall_not_pass,),
	"dragon":(dragon,)},
"gentil":lambda self:self.smiley["gentil"],
"autre":lambda self:self.smiley["autre"],
"mechant":lambda self:self.smiley["mechant"],
"desabuse":lambda self:self.smiley["desabuse"],
"triste":lambda self:self.smiley["triste"],
"peur":lambda self:self.smiley["peur"],
"gene":lambda self:self.smiley["gene"],
"moqueur":lambda self:self.smiley["moqueur"],
"WTF":lambda self:self.smiley["WTF"],
"idunno":lambda self:self.smiley["idunno"],
"flopping_table":lambda self:self.smiley["flopping_table"],
"put_table":lambda self:self.smiley["put_table"],
"flopping_guy":lambda self:self.smiley["flopping_guy"],
"flopping_fb":lambda self:self.smiley["flopping_fb"],
"flopping_table_to":lambda self:self.smiley["flopping_table_to"],
"all":lambda self:tuple([j for i in self.smiley for j in self.smiley[i]]),
"__repr__":lambda self:str(self.all()),
"__getitem__":lambda self,typ:self.smiley[typ]})()


salutation = type('',(),{
"salut":{
	"gentil":("coucou","salut","ohayo","yop","yo", "plop"),
	"autres":("bonjour","je vous salut bien bas", "salutation","mes sincères salutations"),
	"mechant":("je ne vous souhaite pas le bonjour",),
	"desabuse":("b'jour","'lut")},
"gentil":lambda self:self.salut["gentil"],
"autre":lambda self:self.salut["autre"],
"mechant":lambda self:self.salut["mechant"],
"desabuse":lambda self:self.salut["desabuse"],
"all":lambda self:tuple([j for i in self.salut for j in self.salut[i]]),
"__repr__":lambda self:str(self.all()),
"__getitem__":lambda self,typ:self.salut[typ]})()


salutation2 = type('',(),{
"salut":{
	"exclamation_neutre":("Bonjour, %s.", "plop, %s."),
	"exclamation_joie1":("salut, %s! =)", "heureux de t'voir, %s! =)"),
	"exclamation_joie2":("Cool! %s est lààà!!! ^◡^", "/me saute de joie de voir %s\n=^_^=", "ohayooo, %s!! *◡*"),
	"exclamation_joie3":("Youhouuuu!!!!\nSalut, %s!! *◡* <3","/me fais la fête à %s\nkeur keur !!! ^◡^"),
	"exclamation_colere1":("pfff...","encore toi...","/me ignore %s...","/me regarde %s de manière hautaine\nu_u"),
	"exclamation_colere2":("*pense: dééégaaaage...*","Encore toi...","T'en a pas mare de venir ici?"),
	"exclamation_colere3":("grrrr!!! è_é","/me mord %s\nDégage!! è_é")},
"all":lambda self:tuple([j for i in self.salut for j in self.salut[i]]),
"__repr__":lambda self:str(self.all()),
"__getitem__":lambda self,typ:self.salut[typ]})()


msgNoQuit = type('',(),{
"msg":{
	"gentil":("toi, va, je ne te hais point... ","Je resterais pour toujours auprès de mon maître. "),
	"autres":("Je n'ai qu'un seul maître, et tu ne l'es point. ",
			"Je n'ai qu'un seul maître, et tu n'en a pas l'étoffe. ",
			"Je n'obéis qu'à mon maître. ", "Nope! "),
	"mechant":("Tu m'parles sur un autre ton, ok? ", "TOI, casse-toi! ",
		"Tu t'prends pour qui? ", "...débile. ", "tu commence à m'gaver, là! ",
		"Go Fuck Yourself!! " ),
	"desabuse":("...","pfff...","dît-il...")},
"gentil":lambda self:self.msg["gentil"],
"autre":lambda self:self.msg["autre"],
"mechant":lambda self:self.msg["mechant"],
"desabuse":lambda self:self.msg["desabuse"],
"all":lambda self:tuple([j for i in self.msg for j in self.msg[i]]),
"__repr__":lambda self:str(self.all()),
"__getitem__":lambda self,typ:self.msg[typ]})()


reponses = type('',(),{
"rep":{
	"positif":("oui","ouais","ouai","yup", "yeah"),
	"negatif":("non","nan","nein","nop","nope"),
	"neutre":("bof","si tu veux",".")},
"positif":lambda self:self.rep["positif"],
"negatif":lambda self:self.rep["negatif"],
"autre":lambda self:self.rep["autre"],
"all":lambda self:tuple([j for i in self.rep for j in self.rep[i]]),
"__repr__":lambda self:str(self.all()),
"__getitem__":lambda self,typ:self.rep[typ]})()


humeur = type('',(),{
"hum":{
	"heureu":("ouiiii!!!","joie en moiii!!!", "youpi!","*saute de joie*"),
	"nostalgique":("%s me manque...",),
	"triste":("*pleure*","*triste*")},
"heureu":lambda self:self.hum["heureu"],
"nostalgique":lambda self:self.hum["nostalgique"],
"triste":lambda self:self.msg["triste"],
"all":lambda self:tuple([j for i in self.hum for j in self.hum[i]]),
"__repr__":lambda self:str(self.all()),
"__getitem__":lambda self,typ:self.hum[typ]})()


msgEnnui = type('',(),{
"_ennui":("J'm'énnuiiiiiieeeuuuuhhhh!!!!", "Je\nme\nfais\nchierrrrr!!!!",bite,"Il s'passe rieeennnn!!!!"),
"_pendu":("on fais quoi?\nJe sais pas... T'as pas une idée?\nUn pendu?\nOuiiii!!!\n\
******\n!a e\n*a***e\n!l\n*a**le\n!t\nta**le\n...\n!g\ntaggle\nGagné!!!\n\
Félicitation, Cuillere!!\nNan, mais sérieux...\nQuelqu'un veut faire un pendu?",
"Quelqu'un veut faire un pendu?"),
"_finPendu":("Et le pendu...?", "si vous trouvez pas, vous pouvez toujours abandonner (!abandon)...",
"hey! n'm'oubliez pas!!\ny'a un pendu de lancé, hein!","...et mon pendu...?"),
"ch_smiley":lambda self, smiley_:choice(smiley.smiley[choice(smiley_)]),
"pendu":lambda self:self._pendu,
"ennui":lambda self:tuple([i+self.ch_smiley(["triste","desabuse","flopping_table"])for i in self._ennui]),
"finPendu":lambda self:tuple([i+self.ch_smiley(["flopping_table",
"flopping_guy","triste","desabuse"]) for i in self._finPendu])})()


insultes = type('',(),{
"insulte_to":{
	(-1,-1):("batez vous et creuvez, qu'on en parle plus! ", "si vous continuez,"+\
	" j'vais finir par vous kick tous les deux... ","vos gueulle, bande débiles! "+\
	"\nj'veux pas voir de putain d'insultes sur ce saloprie de chan!! ",
	"j'vais finir par vous kickerrrrr!!! ", "vous deux, la ferme! "),
	(-1,0):("Oh!! %1, pas d'insultes, STP!! ", "reste poli, %1 ", "on s'calme, mec... "),
	(0,0):("Oh!! %1, pas d'insultes, STP!! ", "reste poli, %1 ", "on s'calme, mec... "),
	(0,-1):("Oh!! %1, pas d'insultes, STP!! ", "reste poli, %1 ", "on s'calme, mec... "),
	(-1,1):("oh! tu parle pas comme ça à %2!! ", "mais j'vais t'kick, moi! sérieux!! Tu lui parle pas comme ça!! ",
	"oh!! tu dis pas %3 à %2, toi!!! "),
	(0,1):("oh! tu parle pas comme ça à %2!! ", "mais j'vais t'kick, moi! sérieux!! Tu lui parle pas comme ça!! ",
	"oh!! tu dis pas %3 à %2, toi!!! ","reste poli, %1! "),
	(1,-1):("Wè! Exactement! %3!! ", "Wè, casse-toi, %2!! ","j'suis d'accord avec %1. "),
	(1,0):("heu... %1, sois plus sympa... ", "%2, arrète d'énerver %1, stp "),
	(1,1):("Faites l'amour, pas la guerre! ","faut pas dire des insultes, c'est pas gentil! ",
	"maiiiiiis!! arrêtez de vous baaattreuuuuh!! ")},
"insultes":{" abruti":1," niquer ta mère":2," nique ta mère":2," va te faire enculer":3,"te faire foutre":3,"te faire mettre":3,
	" bâtard":1," biatch":1," bouffon":1," branleur":1," sale chien":1," sale chienne":1," con ":1," conne ":1,
	"connard":1,"connasse":1,"débile":1,"enculé":1,"enflure":1,"folle":1,"garce":1,"imbécile":1,"kikoo":1,
	"kikou":1,"kikoulol":1,"kikoolol":1,"lopette":1,"sous-merde":1,"sale merde":1," mongole":1," pute":1," ptain":1,"sac à foutre":1,
	"sac à merde":1," salaud":1," salope":1,"sous-merde":1,"sous-développé":1," ta gueule":0,"sale traînée":1,
	"trou du cul":1},
"love":{(-1,-1):(-2,0),(-1,0):(-5,0),(-1,1):(-10,0),
	(-0,-1):(0,0),(0,0):(-2,0),(0,-1):(-5,0),
	(1,-1):(+5,0),(1,0):(0,0),(1,1):(-2,0)},
"to":lambda self, a:self.insulte_to[a],
"get":lambda self:self.insultes.keys(),
"get_love":lambda self, a:self.love[a]})()
#"va chier""pute"
#3 = va te
#2 = va
#1 = espèce de
#0 = autre (ta gueule)
msgQuit = ("De toute façon, fallait que je parte archiver quelques dossiers... ",
	"En même temps, qui voudrait rester avec vous!? ","j'y compte bien, wè!")
