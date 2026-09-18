from sys import dont_write_bytecode
from colorama import Style, Back, Fore
from getkey import getkey, keys
from replit import clear
import signal, os
def handler(signum, frame):
  jerryisshabi = True
signal.signal(signal.SIGINT, handler)
savemode = 1
emode = 0
mode = 0
color = '1'
sdim = 0
esc = False
menu = False
bg = 'BLACK'
bcode = 'This is the base code' 
pcode = 'This is the present code'
alp = "abcdefghijklmnopqrstuvwxyz"
blp = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
tiles = [[Style.RESET_ALL+"\n",Back.BLACK+"  ",Back.WHITE+"  ",Back.RED+"  ",Back.LIGHTYELLOW_EX+"  ",Back.GREEN+"  ",Back.CYAN+"  ",Back.BLUE+"  ",Back.MAGENTA+"  ",Back.LIGHTWHITE_EX+"  ",Back.YELLOW+"  "],['0\n','1 ','2 ','3 ','4 ','5 ','6 ','7 ','8 ','9 ','10']]
ctiles = ["0\n","1","2","3","4"]
def back(x):
  #Makes the background of player same as the actual one
  global bg
  if x == '1':
    bg = 'BLACK'
  elif x == '2':
    bg = 'WHITE'
  elif x == '3':
    bg = 'RED'
  elif x == '4':
    bg = 'YELLOW'
  elif x == '5':
    bg = 'GREEN'
  elif x == '6':
    bg = 'CYAN'
  elif x == '7':
    bg = 'BLUE'
  elif x == '8':
    bg = 'MAGENTA'
  elif x == '9':
    bg = 'LIGHTWHITE_EX'
  elif x == '-':
    bg = 'YELLOW'
def generate(code):
  #Generates the Image
  t = 0 #how many times for loop repeat
  ret = [] #return value
  cp = [] #copy paste
  for i in code:
    if i == '.':
      if emode == 0:
        back(bcode[pos(x,y)])
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
  global dcode
  global bcode
  global posit
  global dims
  global x
  global y
  global w
  global h
  dims = []
  for i in range(int(input("How many dimensions do you want?"))):
    while True:
      try:
        dims.append(int(input(f"Enter the length of the {i+1}th dimesion of the screen")))
        break
      except:
        clear()
  dcode =("2"*dims[0]+"0")*dims[1]
  for i in range(len(dims)-2):
    dcode = [dcode] * dims[i+2]
  w = dims[0]
  h = dims[1]
  x = 0
  y = 0
  posit = [0]*(len(dims)-2)+[str(pos(x,y))]
  bcode = find(dcode,posit[:-1])
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
  global dcode
  global savemode
  global esc
  global color
  global emode
  nothing = True
  global sdim
  global posit
  key = getkey()
  if key == 'a':
    if x>0:
      x -= 1
    else:
      nothing = False
  elif key == 'd':
    if x<w-1:
      x += 1
    else:
      nothing = False
  elif key == 'w':
    if y>0:
      y -= 1
    else:
      nothing = False  
  elif key == 's':
    if y<h-1:
      y += 1
    else:
      nothing = False
  elif key == keys.UP:
    if int(posit[-sdim-2]) > 0:
      posit[-sdim-2] = int(posit[-sdim-2])-1
    else:
      nothing = False
  elif key == keys.DOWN:
    if int(posit[-sdim-2]) < int(dims[sdim+2])-1:
      posit[-sdim-2] = int(posit[-sdim-2])+1
    else:
      nothing = False
  elif key == keys.RIGHT:
    if sdim+1 < len(posit)-1:
      sdim += 1
    else:
      nothing = False
  elif key == keys.LEFT:
    if sdim > 0:
      sdim -= 1
    else:
      nothing = False
  elif key <= '9' and key >= "1":
    color = key
  elif key == 'z':
    dcode = inject(dcode,posit,color)
  elif key == '\x1b':
    esc = True
  elif key == 'l':
    savemode *= -1
  elif key == 'e':
    emode = 1 if emode == 0 else 0
  else:
    nothing = False
  if nothing is True:
    Refresh()
  nothing = True
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
  global dcode
  global savemode
  global esc
  global color
  global emode
  global sdim
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
    input(color)
    dcode = inject(dcode,posit,color)
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
  global dcode
  global bcode
  global pcode
  global posit
  clear()
  posit[-1] = pos(x,y)
  bcode = find(dcode,posit[:-1])
  pcode = bcode
  pcode = replace(pcode,pos(x,y),'.')
  print(generate(pcode)+"-"*18)
  print(Back.BLACK+"1",Back.WHITE+"2",Back.RED+"3",Back.LIGHTYELLOW_EX+"4",Back.GREEN+"5",Back.CYAN+"6",Back.BLUE+"7",Back.MAGENTA+"8",Back.LIGHTWHITE_EX+"9S"+Style.RESET_ALL)
  print("  "*(int(color)-1)+"↑")
  ret = []
  for i in range(len(posit)-1):
    if sdim == i:
      if i+3 < 10:
        ret.append(Back.WHITE+f"{i+3}D "+Style.RESET_ALL)
      else:
        ret.append(Back.WHITE+f"{i+3}D "+Style.RESET_ALL)
    else:
      if i+3 < 10:
        ret.append(f"{i+3}D ")
      else:
        ret.append(f"{i+3}D ")
  print(''.join(ret))
  print('  '.join(str(i) for i in reversed(posit[:-1])))
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
    if mode == 1:
      paint()
    elif mode == 2:
      load()
  elif choice == 2:
    clear()
    print("Controls:\n---------------\nAWSD to move\n1-8 to change color\nZ to paint\nArrow keys to change dimension.")
    input("Press Enter to go back")
  elif choice == 3:
    menu = True 
def pos(x,y):
  #returns the list position of a point
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
def imit(li,opt):
  ret = []
  global chosen
  global choice
  for i in li:
      ret.extend([" ",i,"\n"])
  ret[opt*3] = ">"
  print(''.join(ret))
  key = getkey()
  if key == keys.DOWN:
    if choice <len(li)-1:
      choice += 1
  elif key == keys.UP:
    if choice >0:
      choice -= 1
  elif key == 'z':
    chosen = True 
def find(code,pos):
  a = code
  for i in range(len(pos)):
    a = a[int(pos[i])]
  return(a)
def inject(code,pos,value):
  cpos = list(pos)
  cpos.pop()
  a = list(find(code,cpos))
  a[int(pos[-1])] = value
  a = ''.join(a)
  for i in range(len(pos)-1):
    cpos.pop()
    b = list(find(code,cpos))
    b[int(pos[-i-2])] = a
    a = b
  return(a)
while True:
  clear()
  color = '1'
  choice = 0
  x = 0
  y = 0
  z = 0
  menus = ["Paint","Load"]
  chosen = False
  menu = False
  esc = False
  while chosen is False:
    clear()
    print("------------------\n    Tile Game\n------------------")
    imit(menus,choice)
  key = ""
  if choice == 0:
    mode = 1
    paint()
  elif choice == 1:
    mode = 2
    load()