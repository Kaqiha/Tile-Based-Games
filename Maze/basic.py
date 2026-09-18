from colorama import Fore,Back,Style
from Seed import *
Ehp = []
Cehp = []
Alphabet = "abcdefghijklkmnopqrstuvwxyz"
Tiles = [Fore.WHITE+"██"+Style.RESET_ALL,Fore.BLACK+"██"+Style.RESET_ALL,Back.WHITE+"人"+Style.RESET_ALL,Back.YELLOW+"门"+Style.RESET_ALL,Fore.RED+"██"+Style.RESET_ALL,"\n",Back.BLACK+"墙"+Style.RESET_ALL,Back.YELLOW+"钥"+Style.RESET_ALL,Back.YELLOW+"锁"+Style.RESET_ALL,Back.GREEN+"钥"+Style.RESET_ALL,Back.WHITE+"鬼"+Style.RESET_ALL]
def Join(x):
  return(''.join(x))
def Sim(x):
  raw = []
  for i in range(len(x)):
    try:
      Integer = True
      t = int(x[i]) - 1
    except:
      Integer = False
    try:
      if x[i] == "a":
        raw.append("a")
      elif Integer == True:
        raw.append(x[i])
      else: 
        for a in range(Alphabet.index(x[i])):
          raw.append(x[i-1])
    except:
      if Integer == True:
        raw.append(x[i])
      else: 
        for a in range(Alphabet.index(x[i])):
          raw.append(x[i-1])
  return(Join(raw))
def Generate(x):
  Gen = []
  for i in range(len(x)):
    try:
      if x[i] == "a":
        Gen.append(Tiles[10])
      else:
        Gen.append(Tiles[int(x[i])])
    except:
      Gen.append(Tiles[int(x[i])])
  print(''.join(Gen))
def Sizes(x):
  size = []
  l = 0
  w = 0
  for i in range(len(x)):
    if x[i] != "5":
      l += 1
    else:
      size.append(l+1)
      break
  for i in range(len(x)):
    if x[i] == "5":
      w += 1
  size.append(w+1)
  return(size)
def Switch(x,y,z):
  #x=string y=first char z=second char
  slist = list(x)
  slist[y] = x[z]
  slist[z] = x[y]
  return(''.join(slist))
def Replace(x,y,z):
  #x=string y=index z=replacement
  slist = list(x)
  slist[y] = z
  return(''.join(slist))
def Distance(x):
  print(print)