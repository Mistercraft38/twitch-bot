#-*- coding: utf-8 -*-
import socket
import sys
import time

s = socket.socket()

#Variable indispensable
CHANNEL = "#elemzje"                                                                                                        #Channel auquel se connecter
PASS = "oauth:censure"                                                                               #oAuth twitch
NICK = "mistercraft38"
#Variables pour fonctions
wiz = 0
sel = -20

def connection():                                                                                                           #Connection au serveur + channel
    print("connecting...")
    s.connect(("irc.chat.twitch.tv", 6667))
    print("identifing with nickname: "+NICK)
    s.send("PASS " + PASS + "\r\n")
    s.send("NICK " + NICK + "\r\n")
    print("joining channel " + CHANNEL)
    s.send("JOIN " + CHANNEL + "\r\n")
    print("Connected")


def send(Message):                                                                                                          #Envoit de messages dans le Channel
    if "/" in Message:
        s.send("PRIVMSG " + CHANNEL + " :" + Message + "\r\n")              #envoie commande
        print("Commande : " + Message)
    else:
        s.send("PRIVMSG " + CHANNEL + " :/me _ MrDestructoid : " + Message + "\r\n")        #envoie message
	       print("Envoyé : " + Message)

connection()
send("/me Le bot de l'enfer est de retour, cachez vous !!!")

try:
 while 1:
    
    text = ""
    recu = s.recv(2040)
    if len(recu.split(":")) >= 3:                                                                                           #séparation user/texte
        user = recu.split("!")[0]
        user = user.split(":")[1]
        for i in range(2, len(recu.split(":")), 1):
            text = text + recu.split(":")[i] + ":"
        print(user+" : "+text)                                                                                              #log
    elif "PING" in recu:                                                                                                    #pong
        rep = recu.split(":")[1]
        s.send("PONG :" + rep + "\r\n")
        print("Ping")

            ###______Commandes______###

    if user == "lawry25":
        send("Kappa")

    if " c " in text and not ("ctrl" in text or "ctl" in text or "contr" in text) and sel < 1:
        send("On n'écrit pas \"c\" quand on parle français... on écrit \"c\'est\", \"ces\", \"ses\" ou encore \"sait\" @"+user)

    if " pa " in text and sel < 1:
    	send("*pas @" + user)

    if " t " in text and sel <1:
        send("On n'écrit pas \"t\" quand on parle francais... on écrit \"t'es\", \"thé\" ou \"tes\" @"+user)
        
    if ("blg" or "BLG" or "beluga" or "Beluga" or "béluga" or "Béluga") in text:
        send("sckBLG sckBLG sckBLG")

    if ("HLT" in text or "salut" in text) and user != "mistercraft38":
        send("sckHLT @" + user)
        
    if "!to " in text and user == "mistercraft38":
        if "!to" in text.split(" ")[0] and len(text.split(" ")) == 3:
            send("/timeout " + text.split(" ")[1] + " " + text.split(" ")[2])

    if user == "wizebot" and wiz == 0:
        send("bonjour @wizebot je viens en paix, pour ne pas t'assister. Je serai present ici pour te faire souffrir.")
        wiz = 1

    if "!twitter" in text and len(text.split(" ")) < 2:
        send("Bon... nightbot vas te donner le twitter d'@elemzje , donc le mien c'est @ mistercraft385 ;)")

    if "!au revoir" in text and (user == "mistercraft38" or "elemzje" or "lawry25"):
        print("au revoir")
        send("/me Sur demande de @" + user + " votre bot bien aimé s'en vas... au revoir. sckHLT ;) ")
        wiz = 0
        while not "!bonjour" in text:
            text = ""
            recu = s.recv(2040)
            if len(recu.split(":")) >= 3:
                user = recu.split("!")[0]
                user = user.split(":")[1]
                for i in range(2, len(recu.split(":")), 1):
                    text = text + recu.split(":")[i] + ":"
                    print(user+" : "+text)
            elif "PING" in recu:
                rep = recu.split(":")[1]
                s.send("PONG :" + rep + "\r\n")
        send("/me Votre bot préféré ( Kappa ) est de retour !!! Merci à @"+user+" pour avoir aidé le phoenix à renaitre de ses cendres")
        
    if "!config" in text and len(text.split(" ")) < 2:
        send("Tu sais que c'est marqué dans la description de la chaine ? Bon aller, vus que je suis gentil: ")
        send("MONITOR : BenQ XL2411Z (144 Hz ! OMG!!!), HEADSET : HYPER X CLOUD II, MOUSE : STEELSERIES Rival (la 1ere), MOUSEPAD : STEELSERIES Qck Heavy (lol j'ai le même Kappa ), KEYBOARD : STEELSERIES APEX M800, MB : ASUS H81-PLUS, CPU : INTEL i5-4690, GPU : MSI GTX 970 4GB (j'ai autant de vram mais bon... j'ai une 750Ti...), HDD : SEAGATE Barracuda 1 To, SDD : SEAGATE 250 Go (riche...), RAM : 2 x 4 Go CORSAIR Vengeance, PSU : CORSAIR 550W.")
    
    if "!pseudo" in text and len(text.split(" ")) < 2:
        send("il était une fois, dans une lointaine contrée naz.. eu non.. il  était une fois, en alsace, un jeune CM1 prénomé Bryan (brillant... LOL). Lors d'une journée d'orage, il jouait avec ses amis. Cependant, avec ses amis, il jouais au foot. L'orage n'etait pas habituel (ciel violet, pluie fine et tout le tralala). ...")
        send("... Avec ses amis, ils s'amusaient à dire \"les elements se dechainent, les elements se déchainent\", ensuite, en classe, ils continuaient avec les elements, leur maîtresse dit \"oui bien l'element, il vas se calmer\". Depuis, element,est resté et s'est transformé en @elemzje. \"zje\" étant là uniquement \"pour faire chier les gens\".")

    if ("!sale" or "!salé") in text:
        sel = 1
        send("Le niveau de PJSalt est reglé à " + str(sel))

    if "!sel" in text:
        send("Le niveau de PJSalt actuel est de " + str(sel))

    if ("!sucre" or "!sucré") in text:
        sel = -50
        send("Le niveau de PJSalt est reglé à "+ str(sel))

    if (" con " or " merde " or " chiant ") in text:
        sel = sel + 1
		
    if (" amour " or " aime " or " <3 ") in text:
        sel = sel - 2






except KeyboardInterrupt:
	send("Votre bot bot préféré s'en vas sur demande imperative de son maitre suprême... Le bot reviendra potentiellement bientôt ;) sckHLT")
	send("/disconnect")