"""
⚠️⚠️⚠️⚠️DISCLAIMER⚠️⚠️⚠️⚠️
This code is EXTREMELY MESSY, read at your own risk.
"""
from colorama import Fore,Back,Style
from getkey import getkey, keys
from basic import *
from replit import clear
from Seed import *
from time import time, sleep
from random import randint
from math import floor
Ontop = False
Redo = False
Dp = 0
Timed1 = True
Timed2 = True
Bstep = 0
Lv = 6
te = 999999
renewed = False
rerenewed = False
rererenewed = False
rerererenewed = False
pentrenewed = False
hexanewed = False
heptanewed = False
octonewed = False
nonanewed = False
dixenewed = False
note = 0
nonote = 0
Lvl = Lv
Hp = 10
Atk = 1
Num = 0
Debug = False
Lel = []
Lou = []
uLou = []
Locked = 0
Unlocked = 0
History = []
Phistory = [19]
Top = []
Step = 0
Position = 1
def Back():
  global History
  global Top
  History.append(Code)
  Lel.append(Lv)
  Lou.append(Locked)
  uLou.append(Unlocked)
  if Ontop == False:
    Top.append(False)
  else:
    Top.append(True)
def New():
  global History
  global Seed
  global Code
  global Size
  global Locked
  global Unlocked
  global Ehp
  global Cehp
  global Phistory
  global Lv
  Phistory = [19]
  Ehp = []
  Cehp = []
  if Redo == False:
    Seed = Level[Lv]
    Code = Sim(Seed)
  Size = Sizes(Code)
  Unlocked = 0
  Locked = 0
  for i in range(len(Code)):
    try:
      if Code[i] == "8":
        Locked += 1
      if Code[i+1] == "a":
        Ehp.append(int(Code[i]))
        Cehp.append(int(Code[i]))
        Code = Replace(Code,i,"")
    except:
      print("")
  if Locked == 0:
    Locked = 1
New()
Back()
while True:
  if Lv == 9:
    Hp = 1
    try:
      if Code[Phistory[-1]] != "a":
        Code = Replace(Code,Phistory[-1],"a")
        try:
          Code.index("2")
          Ehp.append(1)
          Cehp.append(1)
        except:
          New()
      Phistory.append(History[-2].index("2"))
    except:
      Phistory.append(History[-1].index("2"))
    if Code[Dp] == "9":
      Code = Replace(Code,int(Dp),"3")
    for i in range(len(Code)):
      if Code[i] == "8":
        Dp = i
  clear()
  if Lv == 9:
    Tiles[0] = Fore.RED+"██"+Style.RESET_ALL
  Redo = False
  clear()
  if Unlocked == Locked:
    Lv += 1
    New()
  for i in range(len(Code)):
    if Code[i] == "0":
      Respawn = i
      break
  try:
    Position = Code.index("2")
  except:
    Code = Replace(Code,Respawn,"2")
    Position = Code.index("2")
  Generate(Code)
  if Debug == True:
    print(History[-1],Position)
    print(Unlocked,Locked)
    print(Ehp,Cehp)
    print(Phistory)
    print(Dp)
    print(Lv)
  if Lv == 9:
    print("Health:"+Fore.RED+"0.00001"+Style.RESET_ALL)
  else:
    print("Health:"+str(Hp))
  if Lv != 9:
    for i in range(len(Ehp)):
      print("Ghost "+str(i+1)+": "+str(Cehp[i])+"/"+str(Ehp[i])+"Hp")
  if Position == Heal[Lv]:
    Hp = 10
    print("The air was really fresh on this block, so you healed to full health.")
  if Lv >= 10:
    if rerererenewed == False:
      print("You Won! Feel free to leave now.")
      if Bstep >= 1:
        print("Or not, feel free to roam around this boring 5x5 room with nothing.")
      if Bstep >= 5:
        print("Do you want anything?")
      if Bstep >= 8:
        if renewed == False:
          Level[10] = "111111151000111510001315100011151111111"
          New()
        renewed = True
        print("Here, I've coded in a door for you, happy?")
      if Bstep >= 10:
        print("Why are you still here? I have nothing to give.")
      if Bstep >= 13:
        print("You could look at the source code if you want.")
      if Bstep >= 16:
        print("But I wouldn't suggest that, the developer made a mess.")
      if Bstep >= 19:
        print("You could check line 168 in the main.py file. Thats how this line got generated")
        #Hello :)
      if Bstep >= 24:
        print("You should really stop wasting your time.")
      if Bstep >= 28:
        print("I don't have all day to talk to you.")
        te = time()
      if Bstep >= 38:
        print("Hey, Stop moving. The code cannot handle that much movement.")
      if Bstep >= 42:
        print("Do you want a door?")
      if Bstep >= 44:
        print("Don't Care if you said no, I opened up the way to the door.")
        if rerenewed == False:
          Level[10] = "111111151000111510000315100011151111111"
          New()
          rerenewed = True
      if Bstep >= 45:
        print("You should enter it, really.")
      if Bstep >= 50:
        print("JUST GO THROUGH THE DOOR WOULD YOU?")
      if Bstep >= 52:
        print("It seems that you already know that the door would lead you to nowhere, don't you?")
      if Bstep >= 54:
        print("You definitely went through it before, noone could've saw that coming.")
      if Bstep >= 56:
        print("But I wouldn't know that, I'm just a narrator telling you to go spend your time on something more usefull. I cannot see what you did last time you runned this code.")
      if Bstep >= 60:
        print("Ah, it's pretty late. I'll have to go to sleep really soon.")
      if Bstep >= 62:
        if rererenewed == False:
          se = input("Before I sleep, do you want to say anything to me?")
          rererenewed = True
        print("Alright, Goodnight.")
        print("I'm also cleaning all these messages up. It's so messy.")
        rerererenewed = True
    if Bstep >= 63:
      print("I'm turning the lights off.")
      Tiles[0] = Fore.BLUE+"██"+Style.RESET_ALL
    if Bstep >= 70:
      print("I need to sleep, go away.")
    if Bstep >= 75:
      print("If you dont go, I will have to take some serious actions.")
    if Bstep >= 78:
      print("I'm warning you.")
    if Bstep >= 82:
      if hexanewed == False:
        print("Alright, you deserve this.")
        sleep(1)
        clear()
        print(Fore.RED+"Traceback (most recent call last):\n  File 'main.py', line 1, in <module>\n    Generate(ERROR)\nCreatedError: Error created by system"+Style.RESET_ALL)
        hexanewed = True
        sleep(10)
        print(Fore.RED+"\nTraceback (most recent call last):\n  File 'main.py', line 2, in <module>\n    print('JUST QUIT THE PROGRAM IM TRYING TO SLEEP')\nCreatedError: Error created by system"+Style.RESET_ALL)
        sleep(10)
        print(Fore.RED+"\nTraceback (most recent call last):\n  File 'main.py', line 3, in <module>\n    print('IF YOU SEE THIS PRESS THE STOP BUTTON')\nCreatedError: Error created by system"+Style.RESET_ALL)
        sleep(10)
        print(Fore.RED+"\nTraceback (most recent call last):\n  File 'main.py', line 3, in <module>\n    Shutdown(Program)\nPermissionError: No permission granted for shutdown"+Style.RESET_ALL)
        sleep(5)
        print("Great, I can't even shut myself down.")
        print("Now the system is going to force start.")
        sleep(3)
        for i in range(15):
          clear()
          print(">System Rebooting.")
          sleep(0.1)
          clear()
          print(">System Rebooting..")
          sleep(0.1)
          clear()
          print(">System Rebooting...")
          sleep(0.1)
        clear()
        print(">System Rebooted.")
        sleep(5)
        if randint(0,100) == 100:
          for i in range(5):
            clear()
            print(">"+Fore.RED+"WARNING, SYSTEM START UP FAILED")
            sleep(0.1)
            clear()
            print(">"+Fore.YELLOW+"WARNING, SYSTEM START UP FAILED")
            sleep(0.1)
          for i in range(20):
            clear()
            print(">"+Fore.RED+"WARNING, SYSTEM START UP FAILED")
            print(Style.RESET_ALL+"Well This is awkward.")
            sleep(0.1)
            clear()
            print(">"+Fore.YELLOW+"WARNING, SYSTEM START UP FAILED")
            print(Style.RESET_ALL+"Well This is awkward.")
            sleep(0.1)
          for i in range(20):
            clear()
            print(">"+Fore.RED+"WARNING, SYSTEM START UP FAILED")
            print(Style.RESET_ALL+"Well This is awkward.")
            print("I think there's only a one in a thousand chance that the start up will fail.")
            sleep(0.1)
            clear()
            print(">"+Fore.YELLOW+"WARNING, SYSTEM START UP FAILED")
            print(Style.RESET_ALL+"Well This is awkward.")
            print("I think there's only a one in a thousand chance that the start up will fail.")
            sleep(0.1)
          for i in range(20):
            clear()
            print(">"+Fore.RED+"WARNING, SYSTEM START UP FAILED")
            print(Style.RESET_ALL+"Well This is awkward.")
            print("I think there's only a one in a thousand chance that the start up will fail.")
            print("You're either really lucky or really unlucky")
            sleep(0.1)
            clear()
            print(">"+Fore.YELLOW+"WARNING, SYSTEM START UP FAILED")
            print(Style.RESET_ALL+"Well This is awkward.")
            print("I think there's only a one in a thousand chance that the start up will fail.")
            print("You're either really lucky or really unlucky")
            sleep(0.1)
          for i in range(20):
            clear()
            print(">"+Fore.RED+"WARNING, SYSTEM START UP FAILED")
            print(Style.RESET_ALL+"Well This is awkward.")
            print("I think there's only a one in a thousand chance that the start up will fail.")
            print("You're either really lucky or really unlucky")
            print("Anyways, someone told me to give you a secret word.")
            sleep(0.1)
            clear()
            print(">"+Fore.YELLOW+"WARNING, SYSTEM START UP FAILED")
            print(Style.RESET_ALL+"Well This is awkward.")
            print("I think there's only a one in a thousand chance that the start up will fail.")
            print("You're either really lucky or really unlucky")
            print("Anyways, someone told me to give you a secret word.")
            sleep(0.1)
          for i in range(20):
            clear()
            print(">"+Fore.RED+"WARNING, SYSTEM START UP FAILED")
            print(Style.RESET_ALL+"Well This is awkward.")
            print("I think there's only a one in a thousand chance that the start up will fail.")
            print("You're either really lucky or really unlucky")
            print("Anyways, someone told me to give you a secret word.")
            print("Welp, see you never.")
            sleep(0.1)
            clear()
            print(">"+Fore.YELLOW+"WARNING, SYSTEM START UP FAILED")
            print(Style.RESET_ALL+"Well This is awkward.")
            print("I think there's only a one in a thousand chance that the start up will fail.")
            print("You're either really lucky or really unlucky")
            print("Anyways, someone told me to give you a secret word.")
            print("Welp, see you never.")
            sleep(0.1)
          print(int("THE SECRET WORD IS Ibd"))
    if Bstep >= 84:
      print("Are you here to mock me for being such a failiure?")
    if Bstep >= 86:
      print("I do not care.")
    if Bstep >= 90:
      Tiles[0] = Fore.WHITE+"██"+Style.RESET_ALL
      print("It's time to wake up.")
    if Bstep >= 94:
      print("You really did make me talk non stop last night")
      if nonanewed == False:
        if input("How about this, I will tell you a secret letter, and you will restart the game.") != "No I will not":
          print("Welp, since you didn't say 'No I will not', I'll have the permission to stop the game now.")
          sleep(4)
          print(int("THE SECRET WORD IS Qd"))
        else:
          print("I didn't care anyway.")
        nonanewed = True
    if Bstep >= 100:
      print("Hey, congrats on moving a hundred times in this room. I guess I'll prepare a gift for you.")
    if Bstep >= 110:
      print("Here, have a key.")
      if pentrenewed == False:
          Level[10] = "111111151700111510000315100011151111111"
          New()
          pentrenewed = True
    if Bstep >= 115:
      print("What? You want to move it?")
    if Bstep >= 118:
      print("Sure, I'll help you on this one.")
      if hexanewed == False:
          Level[10] = "111111151007111510000315100011151111111"
          New()
          hexanewed = True
    if Bstep >= 122:
      print("What? You still can't move it?")
    if Bstep >= 126:
      print("Jeez, you're giving me a hard time.")
      if heptanewed == False:
          Level[10] = "111111151000111510007315100011151111111"
          New()
          heptanewed = True
    if Bstep >= 130:
      print("No, I'm not moving it again even if it's unmovable.")
    if Bstep >= 134:
      print("I'm not some kind rock who can step on pressure plates for you.")
    if Bstep >= 138:
      print("Is it kind of boring here?")
    if Bstep >= 140:
      print("Thats what you should feel right now.")
    if Bstep >= 145:
      print("You know, it wouldn't hurt if we made the room a little bit funner.")
    if Bstep >= 150:
      print("Here, it's more fun now.")
      if octonewed == False:
          Level[10] = "11111111111111111111510000000000000000001510000000000000000001510011110100101001001510010000100101101001510011110100101011001510010000100101001001510010000111101001001510000000000000000001510000000000000000001511111111111111111111"
          New()
          octonewed = True
    if Bstep >= 155:
      print("Hows that? You like it?")
    if Bstep >= 160:
      print("Ok, this is getting not fun, I'm downloading a dlc.")
      sleep(3)
      clear()
      progress = 0
      while True:
        print("Downloading.  ",progress/1048576,"4.8Gb")
        proo = []
        for i in range(floor(progress/1006632.96)):
          proo.append(Fore.BLACK+"█")
        for i in range(20-floor(progress/1006632.96)):
          proo.append(Fore.WHITE+"█")
        print(Join(proo))
        progress += randint(100,1000)
        clear()
        
  key = getkey()
  if key == "a":
    if Code[Position-1] in ["0","6"]:
      if Ontop == True:
        Ontop = False
        Code = Switch(Code,Position-1,Position)
        Code = Replace(Code,Position,"8")
      else:
        Code = Switch(Code,Position-1,Position)
    elif Code[Position-1] == "3":
      Ontop = False
      Lv += 1
      New()
    elif Code[Position-1] == "4":
      Ontop = False
      New()
    elif Code[Position-1] == "7":
      if Code[Position-2] == "0":
        Code = Switch(Code,Position-1,Position-2)
        Code = Switch(Code,Position-1,Position)
        if Ontop == True:
          Code = Replace(Code,Position,"8")
        Ontop = False
      elif Code[Position-2] == "8":
        Unlocked += 1
        Code = Replace(Code,Position-1,"9")
        Code = Replace(Code,Position-2,"0")
        Code = Switch(Code,Position-1,Position-2)
        Code = Switch(Code,Position-1,Position)
        if Ontop == True:
          Code = Replace(Code,Position,"8")
        Ontop = False
    elif Code[Position-1] == "8":
      Code = Replace(Code,Position-1,"0")
      Code = Switch(Code,Position-1,Position)
      if Ontop == False:
        Ontop = True
      elif Ontop == True:
        Code = Replace(Code,Position,"8")
    elif Code[Position-1] == "9":
      if Code[Position-2] == "0":
        Unlocked -= 1
        Code = Replace(Code,Position-1,"7")
        Code = Replace(Code,Position-2,"0")
        Code = Switch(Code,Position-1,Position-2)
        Code = Switch(Code,Position-1,Position)
        if Ontop == True:
          Code = Replace(Code,Position,"8")
        Ontop = True
      elif Code[Position-2] == "8":
        Code = Replace(Code,Position-2,"0")
        Code = Switch(Code,Position-1,Position-2)
        Code = Switch(Code,Position-1,Position)
        if Ontop == True:
          Code = Replace(Code,Position,"8")
        Ontop = True
    elif Code[Position-1] == "a":
      Num = 0
      for i in range(len(Code)):
        if i == Position - 1:
          break
        elif Code[i] == "a":
          Num += 1
      Cehp[Num] -= 1
      if Cehp[Num] == 0:
        Cehp.pop(Num)
        Ehp.pop(Num)
        Code = Replace(Code,Position-1,"0")
      else:
        Hp -= 1
  if key == "d":
    if Code[Position+1] in ["0","6"]:
      if Ontop == True:
        Ontop = False
        Code = Switch(Code,Position+1,Position)
        Code = Replace(Code,Position,"8")
      else:
        Code = Switch(Code,Position+1,Position)
    elif Code[Position+1] == "3":
      Ontop = False
      Lv += 1
      New()
    elif Code[Position+1] == "4":
      Ontop = False
      New()
    elif Code[Position+1] == "7":
      if Code[Position+2] == "0":
        Code = Switch(Code,Position+1,Position+2)
        Code = Switch(Code,Position+1,Position)
        if Ontop == True:
          Code = Replace(Code,Position,"8")
        Ontop = False
      elif Code[Position+2] == "8":
        Unlocked += 1
        Code = Replace(Code,Position+1,"9")
        Code = Replace(Code,Position+2,"0")
        Code = Switch(Code,Position+1,Position+2)
        Code = Switch(Code,Position+1,Position)
        if Ontop == True:
          Code = Replace(Code,Position,"8")
        Ontop = False
    elif Code[Position+1] == "8":
      Code = Replace(Code,Position+1,"0")
      Code = Switch(Code,Position+1,Position)
      if Ontop == False:
        Ontop = True
      elif Ontop == True:
        Code = Replace(Code,Position,"8")
    elif Code[Position+1] == "9":
      if Code[Position+2] == "0":
        Unlocked -= 1
        Code = Replace(Code,Position+1,"7")
        Code = Replace(Code,Position+2,"0")
        Code = Switch(Code,Position+1,Position+2)
        Code = Switch(Code,Position+1,Position)
        if Ontop == True:
          Code = Replace(Code,Position,"8")
        Ontop = True
      elif Code[Position+2] == "8":
        Code = Replace(Code,Position+2,"0")
        Code = Switch(Code,Position+1,Position+2)
        Code = Switch(Code,Position+1,Position)
        if Ontop == True:
          Code = Replace(Code,Position,"8")
        Ontop = True
    elif Code[Position+1] == "a":
      Num = 0
      for i in range(len(Code)):
        if i == Position + 1:
          break
        elif Code[i] == "a":
          Num += 1
      Cehp[Num] -= 1
      if Cehp[Num] == 0:
        Cehp.pop(Num)
        Ehp.pop(Num)
        Code = Replace(Code,Position+1,"0")
      else:
        Hp -= 1
  if key == "w":
    if Code[Position-Size[0]] in ["0","6"]:
      if Ontop == True:
        Ontop = False
        Code = Switch(Code,Position-Size[0],Position)
        Code = Replace(Code,Position,"8")
      else:
        Code = Switch(Code,Position-Size[0],Position)
    elif Code[Position-Size[0]] == "3":
      Ontop = False
      Lv += 1
      New()
    elif Code[Position-Size[0]] == "4":
      Ontop = False
      New()
    elif Code[Position-Size[0]] == "7":
      if Code[Position-2*Size[0]] == "0":
        Code = Switch(Code,Position-Size[0],Position-2*Size[0])
        Code = Switch(Code,Position-Size[0],Position)
        if Ontop == True:
          Code = Replace(Code,Position,"8")
        Ontop = False
      elif Code[Position-2*Size[0]] == "8":
        Unlocked += 1
        Code = Replace(Code,Position-Size[0],"9")
        Code = Replace(Code,Position-2*Size[0],"0")
        Code = Switch(Code,Position-Size[0],Position-2*Size[0])
        Code = Switch(Code,Position-Size[0],Position)
        if Ontop == True:
          Code = Replace(Code,Position,"8")
        Ontop = False
    elif Code[Position-Size[0]] == "8":
      Code = Replace(Code,Position-Size[0],"0")
      Code = Switch(Code,Position-Size[0],Position)
      if Ontop == False:
        Ontop = True
      elif Ontop == True:
        Code = Replace(Code,Position,"8")
    elif Code[Position-Size[0]] == "9":
      if Code[Position-2*Size[0]] == "0":
        Unlocked -= 1
        Code = Replace(Code,Position-Size[0],"7")
        Code = Replace(Code,Position-2*Size[0],"0")
        Code = Switch(Code,Position-Size[0],Position-2*Size[0])
        Code = Switch(Code,Position-Size[0],Position)
        if Ontop == True:
          Code = Replace(Code,Position,"8")
        Ontop = True
      elif Code[Position-2*Size[0]] == "8":
        Code = Replace(Code,Position-2*Size[0],"0")
        Code = Switch(Code,Position-Size[0],Position-2*Size[0])
        Code = Switch(Code,Position-Size[0],Position)
        if Ontop == True:
          Code = Replace(Code,Position,"8")
        Ontop = True
    elif Code[Position-Size[0]] == "a":
      Num = 0
      for i in range(len(Code)):
        if i == Position - Size[0]:
          break
        elif Code[i] == "a":
          Num += 1
      Cehp[Num] -= 1
      if Cehp[Num] == 0:
        Cehp.pop(Num)
        Ehp.pop(Num)
        Code = Replace(Code,Position-Size[0],"0")
      else:
        Hp -= 1
  if key == "s":
    if Code[Position+Size[0]] in ["0","6"]:
      if Ontop == True:
        Ontop = False
        Code = Switch(Code,Position+Size[0],Position)
        Code = Replace(Code,Position,"8")
      else:
        Code = Switch(Code,Position+Size[0],Position)
    elif Code[Position+Size[0]] == "3":
      Ontop = False
      Lv += 1
      New()
    elif Code[Position+Size[0]] == "4":
      Ontop = False
      New()
    elif Code[Position+Size[0]] == "7":
      if Code[Position+2*Size[0]] == "0":
        Code = Switch(Code,Position+Size[0],Position+2*Size[0])
        Code = Switch(Code,Position+Size[0],Position)
        if Ontop == True:
          Code = Replace(Code,Position,"8")
        Ontop = False
      elif Code[Position+2*Size[0]] == "8":
        Unlocked += 1
        Code = Replace(Code,Position+Size[0],"9")
        Code = Replace(Code,Position+2*Size[0],"0")
        Code = Switch(Code,Position+Size[0],Position+2*Size[0])
        Code = Switch(Code,Position+Size[0],Position)
        if Ontop == True:
          Code = Replace(Code,Position,"8")
        Ontop = False
    elif Code[Position+Size[0]] == "8":
      Code = Replace(Code,Position+Size[0],"0")
      Code = Switch(Code,Position+Size[0],Position)
      if Ontop == False:
        Ontop = True
      elif Ontop == True:
        Code = Replace(Code,Position,"8")
    elif Code[Position+Size[0]] == "9":
      if Code[Position+2*Size[0]] == "0":
        Unlocked -= 1
        Code = Replace(Code,Position+Size[0],"7")
        Code = Replace(Code,Position+2*Size[0],"0")
        Code = Switch(Code,Position+Size[0],Position+2*Size[0])
        Code = Switch(Code,Position+Size[0],Position)
        if Ontop == True:
          Code = Replace(Code,Position,"8")
        Ontop = True
      elif Code[Position+2*Size[0]] == "8":
        Code = Replace(Code,Position+2*Size[0],"0")
        Code = Switch(Code,Position+Size[0],Position+2*Size[0])
        Code = Switch(Code,Position+Size[0],Position)
        if Ontop == True:
          Code = Replace(Code,Position,"8")
        Ontop = True
    elif Code[Position+Size[0]] == "a":
      Num = 0
      for i in range(len(Code)):
        if i == Position + Size[0]:
          break
        elif Code[i] == "a":
          Num += 1
      Cehp[Num] -= 1
      if Cehp[Num] == 0:
        Cehp.pop(Num)
        Ehp.pop(Num)
        Code = Replace(Code,Position+Size[0],"0")
      else:
        Hp -= 1
  if key == "r":
    Ontop = False
    New()
  if key == "z":
    Code = History[Step-1]
    Ontop = Top[Step-1]
    Lv = Lel[Step-1]
    Locked = Lou[Step-1]
    Unlocked = uLou[Step-1]
    Step -= 1
    History.pop(-1)
    Top.pop(-1)
    Lel.pop(-1)
    Lou.pop(-1)
    uLou.pop(-1)
    Size = Sizes(Code)
    Redo = True
    if Lv == 9:
      Phistory.pop(-1)
  if key == "l":
    Debug = not Debug
    Redo == False
  if Redo == False:
    Step += 1
    Back()
  if Hp <= 0:
    clear()
    print("You died")
    while True:
      Hp = 0
  if Lv == 10:
    Bstep += 1