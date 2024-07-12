from colorama import Style, Back, Fore
from getkey import getkey, keys
from replit import clear
from level import lcode, ccode, tdcode
import signal, os
def handler(signum, frame):
  jerryisshabi = True
signal.signal(signal.SIGINT, handler)
hp = 10
savemode = 1
cmode = True
emode = 0
mode = 0
color = '1'
level = 0
unlocked = 0
tlocked = 0
esc = False
menu = False
bcode = 'This is the base code' 
pcode = 'This is the present code'
alp = "abcdefghijklmnopqrstuvwxyz"
blp = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
tiles = [[Style.RESET_ALL+"\n",Back.BLACK+"  ",Back.WHITE+"  ",Back.RED+"  ",Back.LIGHTYELLOW_EX+"  ",Back.GREEN+"  ",Back.CYAN+"  ",Back.BLUE+"  ",Back.MAGENTA+"  ",Back.LIGHTWHITE_EX+"  ",Back.YELLOW+"  "],['0\n','1 ','2 ','3 ','4 ','5 ','6 ','7 ','8 ','9 ','10']]
ctiles = ["0\n","1","2","3","4"]
def back():
  #Makes the background of player same as the actual one
  global bg
  if bcode[pos(x,y)] == '1':
    bg = 'BLACK'
  if bcode[pos(x,y)] == '2':
    bg = 'WHITE'
  if bcode[pos(x,y)] == '3':
    bg = 'RED'
  if bcode[pos(x,y)] == '4':
    bg = 'YELLOW'
  if bcode[pos(x,y)] == '5':
    bg = 'GREEN'
  if bcode[pos(x,y)] == '6':
    bg = 'CYAN'
  if bcode[pos(x,y)] == '7':
    bg = 'BLUE'
  if bcode[pos(x,y)] == '8':
    bg = 'MAGENTA'
  if bcode[pos(x,y)] == '9':
    bg = 'LIGHTWHITE_EX'
  if bcode[pos(x,y)] == '-':
    bg = 'YELLOW'
def generate(code):
  #Generates the Image
  t = 0 #how many times for loop repeat
  ret = [] #return value
  cp = [] #copy paste
  for i in code:
    if i == '.':
      if emode == 0:
        back()
        ret.append(getattr(Back,bg)+"〇")
      else:
        ret.append("〇")
    else:
      try:
        ret.append(tiles[emode][int(i)])
      except:
        if i in alp:
          try:
            ret.append(tiles[emode][int(code[t-1])] * alp.index(i))
          except:
            ret.extend(generate(cp) * (alp.index(i)+1))
        elif i in blp:
          cp = code[t-blp.index(i)-1:t]
        elif i == "-":
          ret.append(tiles[emode][10])
        else:
          t += 0#haha
    t += 1
  return(''.join(ret))
def raw(code):
  #Generates the raw code
  t = 0 #how many times for loop repeat
  ret = [] #return value
  cp = [] #copy paste
  redo = False #Redo bc copypaste
  for i in code:
    global retu
    try:
      int(i)
      ret.append(i)
    except:
      if i in alp:
        try:
          ret.append(str(int(code[t-1])) * alp.index(i))
        except:
          ret.extend((cp) * alp.index(i))
          redo = True
      elif i in blp:
        cp = code[t-blp.index(i)-1:t]
      elif i == "-":
        ret.append("-")
      else:
        t += 0#hehe
    t += 1
  if redo is True:
    raw(''.join(ret))
  else:
    retu = ''.join(ret)
  return(retu)
def compact(x):
  a = x[0] #selected term
  time = 1 #how many times repeated
  ans = []
  for i in range(1,len(x)):
    if x[i] == a:
      time +=1
    elif time > 1:
      ans.extend([a,alp[time-1]])
      a = x[i]
      time = 1
    else:
      ans.append(a)
      a = x[i]
  return(''.join(ans))
def replace(obj,pos,rep):
  #Replace a list's object with another 
  obj = list(obj)
  obj[pos] = str(rep)
  return(''.join(obj))
def paint():
  #initiates the painting program
  clear()
  global bcode
  global x
  global y
  global w
  global h
  t= 0
  this = True
  while this is True:
    try:
      h = int(input("Enter the height of the screen"))
      w = int(input("Enter the width of the screen"))
      this = False
    except:
      clear()
  bcode = raw(("2"*w+"0")*h)
  x = 0 #x position
  y = 0 #y position
  while menu is False:
    Refresh()
    while esc is False:
      pmove()
    Setting()  
def pmove():
  #movement for the painting program
  global x
  global y
  global bcode
  global savemode
  global esc
  global color
  global emode
  key = getkey()
  if key == 'a' or key == keys.LEFT:
    if x>0:
      x -= 1
      Refresh()
    else:
      Refresh()
  elif key == 'd' or key == keys.RIGHT:
    if x<w-1:
      x += 1
      Refresh()
    else:
      Refresh()
  elif key == 'w' or key == keys.UP:
    if y>0:
      y -= 1
      Refresh()
    else:
      Refresh()
  elif key == 's' or key == keys.DOWN:
    if y<h-1:
      y += 1
      Refresh()
    else:
      Refresh()
  elif key <= '9' and key >= "1":
    color = key
    Refresh()
  elif key == 'z':
    bcode = replace(bcode,pos(x,y),color)
    Refresh()
  elif key == '\x1b':
    esc = True
  elif key == 'l':
    savemode *= -1
    Refresh()
  elif key == 'e':
    emode = 1 if emode == 0 else 0
    Refresh()
  else:
    Refresh()
def puzzle():
  setup()
  while menu is False:
    Refresh()
    while esc is False:
      pzmove()
    Setting()
def pzmove():
  #movement for the painting program
  global x
  global hp
  global y
  global bcode
  global savemode
  global esc
  global color
  global emode
  global level
  global unlocked
  key = getkey()
  hx = x
  hy = y
  if key == 'a' or key == keys.LEFT:
    if x>0:
      x -= 1
  elif key == 'd' or key == keys.RIGHT:
    if x<wi[y]-1:
      x += 1
  elif key == 'w' or key == keys.UP:
    if y>0:
      if x <= min(wi[y],wi[y-1]) and bcode[pos(x,y-1)] != '0':
        y -= 1
  elif key == 's' or key == keys.DOWN:
    if y<h-1:
      if x+1 <= min(wi[y],wi[y+1]) and bcode[pos(x,y+1)] != '0':
        y += 1
  elif key == 'r':
    setup()
  elif key <= '6' and key >= '1':
    level = int(key)
    bcode = lcode[level]
    setup()
  elif key == '\x1b':
    esc = True
  elif key == 'e':
    emode = 1 if emode == 0 else 0
  if bcode[pos(x,y)] == "1":
    x = hx
    y = hy
  elif bcode[pos(x,y)] == "3":
    hp -= 1
    if hp <= 0:
      setup()
  elif bcode[pos(x,y)] == "4":
    try:
      if 2*x-hx >= 0 and 2*y-hy >= 0 and 2*x-hx <= wi[2*y-hy]-1 and 2*y-hy <= h:
        if bcode[pos(2*x-hx,2*y-hy)] in ["1","3","4","5","8","-"]:
          x = hx
          y = hy
        elif bcode[pos(2*x-hx,2*y-hy)] == "2":
          bcode = replace(bcode,pos(2*x-hx,2*y-hy),"4")
          bcode = replace(bcode,pos(x,y),"2")
        elif bcode[pos(2*x-hx,2*y-hy)] == "6":
          bcode = replace(bcode,pos(2*x-hx,2*y-hy),"-")
          bcode = replace(bcode,pos(x,y),"2")
          unlocked += 1
        elif bcode[pos(2*x-hx,2*y-hy)] == "7":
          bcode = replace(bcode,pos(2*x-hx,2*y-hy),"2")
          bcode = replace(bcode,pos(x,y),"2")
      else:
        x = hx
        y = hy
    except:
      x = hx
      y = hy
  elif bcode[pos(x,y)] == "5":
    level += 1
    bcode = lcode[level]
    setup()
  elif bcode[pos(x,y)] == "7":
    setup()
  elif bcode[pos(x,y)] == "-":
    try:
      if 2*x-hx >= 0 and 2*y-hy >= 0 and 2*x-hx <= wi[2*y-hy]-1 and 2*y-hy <= h:
        if bcode[pos(2*x-hx,2*y-hy)] in ["1","3","4","5","8","-"]:
          x = hx
          y = hy
        elif bcode[pos(2*x-hx,2*y-hy)] == "2":
          bcode = replace(bcode,pos(2*x-hx,2*y-hy),"4")
          bcode = replace(bcode,pos(x,y),"6")
          unlocked -= 1
        elif bcode[pos(2*x-hx,2*y-hy)] == "6":
          bcode = replace(bcode,pos(2*x-hx,2*y-hy),"-")
          bcode = replace(bcode,pos(x,y),"6")
        elif bcode[pos(2*x-hx,2*y-hy)] == "6":
          bcode = replace(bcode,pos(2*x-hx,2*y-hy),"2")
          bcode = replace(bcode,pos(x,y),"6")
          unlocked -= 1
      else:
        x = hx
        y = hy
    except:
      x = hx
      y = hy
  if unlocked == tlocked:
    bcode = replace(bcode,bcode.index('8'),'5')
    unlocked = 0
  Refresh()
def sokaban():
  setup()
  while menu is False:
    Refresh()
    while esc is False:
      smove()
    Setting()
def smove():
  global x
  global y
  global bcode
  global savemode
  global esc
  global color
  global emode
  global level
  global unlocked
  key = getkey()
  hx = x
  hy = y
  if key == 'a' or key == keys.LEFT:
    if x>0:
      x -= 1
  elif key == 'd' or key == keys.RIGHT:
    if x<wi[y]-1:
      x += 1
  elif key == 'w' or key == keys.UP:
    if y>0:
      if x <= min(wi[y],wi[y-1]) and bcode[pos(x,y-1)] != '0':
        y -= 1
  elif key == 's' or key == keys.DOWN:
    if y<h-1:
      if x+1 <= min(wi[y],wi[y+1]) and bcode[pos(x,y+1)] != '0':
        y += 1
  elif key == 'r':
    setup()
  elif key <= '6' and key >= '1':
    level = int(key)
    bcode = ccode[level]
    setup()
  elif key == '\x1b':
    esc = True
  elif key == 'e':
    emode = 1 if emode == 0 else 0
  if bcode[pos(x,y)] == "1":
    x = hx
    y = hy
  elif bcode[pos(x,y)] == "4":
    try:
      if 2*x-hx >= 0 and 2*y-hy >= 0 and 2*x-hx <= wi[2*y-hy]-1 and 2*y-hy <= h:
        if bcode[pos(2*x-hx,2*y-hy)] in ["1","3","4","5","8","-"]:
          x = hx
          y = hy
        elif bcode[pos(2*x-hx,2*y-hy)] == "2":
          bcode = replace(bcode,pos(2*x-hx,2*y-hy),"4")
          bcode = replace(bcode,pos(x,y),"2")
        elif bcode[pos(2*x-hx,2*y-hy)] == "6":
          bcode = replace(bcode,pos(2*x-hx,2*y-hy),"-")
          bcode = replace(bcode,pos(x,y),"2")
          unlocked += 1
        elif bcode[pos(2*x-hx,2*y-hy)] == "7":
          bcode = replace(bcode,pos(2*x-hx,2*y-hy),"2")
          bcode = replace(bcode,pos(x,y),"2")
      else:
        x = hx
        y = hy
    except:
      x = hx
      y = hy
  elif bcode[pos(x,y)] == "5":
    level += 1
    bcode = ccode[level]
    setup()
  elif bcode[pos(x,y)] == "-":
    try:
      if 2*x-hx >= 0 and 2*y-hy >= 0 and 2*x-hx <= wi[2*y-hy]-1 and 2*y-hy <= h:
        if bcode[pos(2*x-hx,2*y-hy)] in ["1","3","4","5","8","-"]:
          x = hx
          y = hy
        elif bcode[pos(2*x-hx,2*y-hy)] == "2":
          bcode = replace(bcode,pos(2*x-hx,2*y-hy),"4")
          bcode = replace(bcode,pos(x,y),"6")
          unlocked -= 1
        elif bcode[pos(2*x-hx,2*y-hy)] == "6":
          bcode = replace(bcode,pos(2*x-hx,2*y-hy),"-")
          bcode = replace(bcode,pos(x,y),"6")
        elif bcode[pos(2*x-hx,2*y-hy)] == "6":
          bcode = replace(bcode,pos(2*x-hx,2*y-hy),"2")
          bcode = replace(bcode,pos(x,y),"6")
          unlocked -= 1
      else:
        x = hx
        y = hy
    except:
      x = hx
      y = hy
  if unlocked == tlocked:
    bcode = replace(bcode,bcode.index('8'),'5')
    unlocked = 0
  Refresh()
def ThreeD():
  global bcode
  global x
  global y
  global z
  global w
  global h
  global l
  global menu
  global esc
  global tcode
  x=0
  y=0
  z=0
  clear()
  while True:
    try:
      w = int(input("Whats the width of the screen?"))
      h = int(input("Whats the length of the screen?"))
      l = int(input("Whats the depth of the screen?"))
      break
    except:
      z += 0
  tcode = [("2"*w+"0")*h]*l
  input(tcode)
  bcode = raw(tcode[z])
  input(bcode)
  while menu is False:
    Trefresh()
    while esc is False:
      tove()
    Setting()
def Trefresh():
  global pcode
  global bcode
  clear()
  bcode = raw(tcode[z])
  pcode = bcode
  pcode = replace(pcode,pos(x,y),".")
  print(generate(pcode)+"-"*18)
def tove():
  #movement for the painting program
  global x
  global y
  global z
  global bcode
  global savemode
  global esc
  global color
  global emode
  global tcode
  key = getkey()
  if key == 'a' or key == keys.LEFT:
    if x>0:
      x -= 1
  elif key == 'd' or key == keys.RIGHT:
    if x<w-1:
      x += 1
  elif key == 'w' or key == keys.UP:
    if y>0:
      y -= 1
  elif key == 's' or key == keys.DOWN:
    if y<h-1:
      y += 1
  elif key == ',':
    if z>0:
      z -= 1
  elif key == '.':
    if z<l-1:
      z += 1
  elif key <= '9' and key >= "1":
    color = key
  elif key == 'z':
    tcode[z] = replace(tcode[z],pos(x,y),color)
  elif key == '\x1b':
    esc = True
  elif key == 'l':
    savemode *= -1
  elif key == 'e':
    emode = 1 if emode == 0 else 0
  Trefresh()
def setup():
  global bcode
  global x
  global y
  global wi
  global h
  global hp
  global tlocked
  global unlocked
  global cmode
  if mode == 0:
    hp = 10
    if level < 5:
      bcode = lcode[level]
      bcode = raw(bcode)
    else:
      clear()
      print("You completed every level.\n"+Fore.RED+"Challenge Mode Unlocked"+Style.RESET_ALL)
      input("Press Enter to continue")
      cmode = True
    try:
      x = bcode.index('9')
    except:
      try:
        x = bcode.index('2')
      except:
        x = 0
    y = 0
    wi = width(bcode)
    h = bcode.count('0')
    unlocked = 0
    tlocked = bcode.count('6')
    if tlocked == 0:
      tlocked += 1
    i = 0
    while x - wi[i] -1 >= 0:
      x -= wi[i]+1
      y+=1
      i+=1
  if mode == 3:
    if level < len(ccode)-1:
      bcode = ccode[level]
      bcode = raw(bcode)
    else:
      clear()
      print("You completed every level(For now)")
      input("Press Enter to continue")
      cmode = True
    try:
      x = bcode.index('9')
    except:
      try:
        x = bcode.index('2')
      except:
        x = 0
    y = 0
    wi = width(bcode)
    h = bcode.count('0')
    unlocked = 0
    tlocked = bcode.count('6')
    if tlocked == 0:
      tlocked += 1
    i = 0
    while x - wi[i] -1 >= 0:
      x -= wi[i]+1
      y+=1
      i+=1
def load():
  global bcode
  global x
  global y
  global wi
  global h
  global cmode
  global menu
  global esc
  clear()
  while True:
    try:
      bcode = input("Enter the code")
      try:
        if bcode[-1] != '0':
          bcode+='0'
      except:
        x += 0#haha
      bcode = raw(bcode)
      x = 0
      y = 0
      wi = width(bcode)
      h = bcode.count('0')
      while menu is False:
        Refresh()
        while esc is False:
          lmove()
        Setting() 
      break
    except:
      clear()
def lmove():
  #movement for the painting program
  global x
  global y
  global bcode
  global savemode
  global esc
  global color
  global emode
  key = getkey()
  if key == 'a' or key == keys.LEFT:
    if x>0:
      x -= 1
      Refresh()
    else:
      Refresh()
  elif key == 'd' or key == keys.RIGHT:
    if x<wi[y]-1:
      x += 1
      Refresh()
    else:
      Refresh()
  elif key == 'w' or key == keys.UP:
    if y>0:
      if x <= min(wi[y],wi[y-1]) and bcode[pos(x,y-1)] != '0':
        y -= 1
        Refresh()
    else:
      Refresh()
  elif key == 's' or key == keys.DOWN:
    if y<h-1:
      if x+1 <= min(wi[y],wi[y+1]) and bcode[pos(x,y+1)] != '0':
        y += 1
        Refresh()
    else:
      Refresh()
  elif key <= '9' and key >= "1":
    color = key
    Refresh()
  elif key == 'z':
    bcode = replace(bcode,pos(x,y),color)
    Refresh()
  elif key == '\x1b':
    esc = True
  elif key == 'l':
    savemode *= -1
    Refresh()
  elif key == 'e':
    emode = 1 if emode == 0 else 0
    Refresh()
  else:
    Refresh()
def Refresh():
  #Refreshes the screen
  global pcode
  clear()
  pcode = bcode
  pcode = replace(pcode,pos(x,y),'.')
  if mode == 0:
    print(generate(pcode)+"-"*18)
    print(Fore.RED+"♥︎"*hp+Fore.BLACK+"♥︎"*(10-hp))
  elif mode == 1:
    print(generate(pcode)+"-"*18)
    print(Back.BLACK+"1",Back.WHITE+"2",Back.RED+"3",Back.LIGHTYELLOW_EX+"4",Back.GREEN+"5",Back.CYAN+"6",Back.BLUE+"7",Back.MAGENTA+"8",Back.LIGHTWHITE_EX+"9S"+Style.RESET_ALL)
    print("  "*(int(color)-1)+"↑")
  elif mode == 2:
    print(generate(pcode)+"-"*18)
    print(Back.BLACK+"1",Back.WHITE+"2",Back.RED+"3",Back.LIGHTYELLOW_EX+"4",Back.GREEN+"5",Back.CYAN+"6",Back.BLUE+"7",Back.MAGENTA+"8",Back.LIGHTWHITE_EX+"9S"+Style.RESET_ALL)
    print("  "*(int(color)-1)+"↑")
    print(pcode)
    print(wi[y])
  elif mode == 3:
    print(generate(pcode)+"-"*18)
  if savemode == -1:
    print(compact(bcode)+'0')
def Setting():
  global esc
  global menu
  global level
  choice = 0
  b = False
  while b is False:
    clear()
    print("------------------\n  Settings\n------------------")
    if choice == 0:
      print(">Resume\n Restart\n Controls\n Exit")
    elif choice == 1:
      print(" Resume\n>Restart\n Controls\n Exit")
    elif choice == 2:
      print(" Resume\n Restart\n>Controls\n Exit")
    elif choice == 3:
      print(" Resume\n Restart\n Controls\n>Exit")
    if b is True:
      print("Yes")
    key = getkey()
    if key == keys.DOWN:
      if choice <3:
        choice += 1
    elif key == keys.UP:
      if choice >0:
        choice -= 1
    elif key == 'z':
      b = True
  if choice == 0:
    esc = False
  elif choice == 1:
    esc = False
    if mode == 0:
      level = 0
      puzzle()
    if mode == 1:
      paint()
    elif mode == 2:
      load()
  elif choice == 2:
    if mode == 1:
      clear()
      print("Controls:\n---------------\nAWSD or Arrow Keys to move\n1-8 to change color\nZ to paint\nL to show to raw code")
      input("Press Enter to go back")
  elif choice == 3:
    menu = True 
def pos(x,y):
  #returns the list position of a point
  if mode != 1 and mode != 4:
    a = 0
    for i in range(y):
      a += wi[i]+1
    return(x+a)
  else:
    return(x+(w+1)*y)
def width(x):
  t = 0
  wi = []
  for i in x:
    if i == '0':
      wi.append(t)
      t = 0
    else:
      t += 1
  return(wi)
while True:
  clear()
  color = 0
  choice = 0
  chosen = False
  menu = False
  esc = False
  if cmode is False:
    while chosen is False:
      clear()
      print("------------------\n    Tile Game\n------------------")
      if choice == 0:
        print(">Puzzle\n Create\n Load")
      elif choice == 1:
        print(" Puzzle\n>Create\n Load")
      elif choice == 2:
        print(" Puzzle\n Create\n>Load")
      key = getkey()
      if key == keys.DOWN:
        if choice <2:
          choice += 1
      elif key == keys.UP:
        if choice >0:
          choice -= 1
      elif key == 'z':
        chosen = True
    if choice == 0:
      mode = 0
      puzzle()
    elif choice == 1:
      mode = 1
      color = '1'
      paint()
    elif choice == 2:
      mode = 2
      menu = False
      esc = False
      load()
  else:
    while chosen is False:
      clear()
      print(Fore.RED+"------------------\n  Challenge Mode\n------------------"+Style.RESET_ALL)
      if choice == 0:
        print(">Sokaban\n 3D Maze\n Quit")
      elif choice == 1:
        print(" Sokaban\n>3D Maze\n Quit")
      elif choice == 2:
        print(" Sokaban\n 3D Maze\n>Quit")
      key = getkey()
      if key == keys.DOWN:
        if choice <2:
          choice += 1
      elif key == keys.UP:
        if choice >0:
          choice -= 1
      elif key == 'z':
        chosen = True
    if choice == 0:
      mode = 3
      sokaban()
    elif choice == 1:
      mode = 4
      color = '1'
      ThreeD()
    elif choice == 2:
      cmode = False
