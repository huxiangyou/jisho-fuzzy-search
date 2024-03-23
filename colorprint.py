"""Print with colors
"""
"""
Python 3.9

Hu Xiangyou
March 24, 2021
May 12, 2021
Oct 22, 2021
"""

import ctypes
import builtins

class Color:
	def __init__(self,code:int):
		self.code=code

WHITE=Color(15)
SILVER=Color(7)
GRAY=Color(8)
BLACK=Color(0)
RED=Color(12)
MAROON=Color(4)
YELLOW=Color(14)
OLIVE=Color(6)
LIME=Color(10)
GREEN=Color(2)
CYAN=Color(11)
TEAL=Color(3)
BLUE=Color(9)
NAVY=Color(1)
MAGENTA=Color(13)
PURPLE=Color(5)
BGWHITE=Color(15<<4)
BGSILVER=Color(7<<4)
BGGRAY=Color(8<<4|15)
BGBLACK=Color(0<<4|15)
BGRED=Color(12<<4|15)
BGMAROON=Color(4<<4|15)
BGYELLOW=Color(14<<4)
BGOLIVE=Color(6<<4|15)
BGLIME=Color(10<<4)
BGGREEN=Color(2<<4|15)
BGCYAN=Color(11<<4)
BGTEAL=Color(3<<4|15)
BGBLUE=Color(9<<4|15)
BGNAVY=Color(1<<4|15)
BGMAGENTA=Color(13<<4|15)
BGPURPLE=Color(5<<4|15)
DEFAULT=SILVER

def _print(*args:list[str|Color],sep:str=" ",end:str="\n"):
	if not args:
		builtins.print(end=end,flush=True)
		return
	for index,arg in enumerate(args):
		if isinstance(arg,Color):
			ctypes.windll.kernel32.SetConsoleTextAttribute(ctypes.windll.kernel32.GetStdHandle(-11),arg.code)
		else:
			if index==0:
				ctypes.windll.kernel32.SetConsoleTextAttribute(ctypes.windll.kernel32.GetStdHandle(-11),7)
			if index+1==len(args):
				builtins.print(arg,end="",flush=True)
				ctypes.windll.kernel32.SetConsoleTextAttribute(ctypes.windll.kernel32.GetStdHandle(-11),7)
				builtins.print(end=end,flush=True)
			else:
				builtins.print(arg,end=sep,flush=True)

def _logger(*args:list[str|Color],sep:str=" ",end:str="\n"):
	with open('output.txt','a+',encoding='utf-8') as f:
		f.write(sep.join(str(arg) for arg in args if not isinstance(arg,Color))+end)

def logger(*args:list[str|Color],sep:str=" ",end:str="\n"):
	_print(*args,sep=sep,end=end)
	_logger(*args,sep=sep,end=end)

print=_print

def useLogger()->callable:
	with open('output.txt','w',encoding='utf-8') as f:
		f.truncate()
	return logger

if __name__=="__main__":
	print(WHITE,"■ WHITE")
	print(SILVER,"■ SILVER")
	print(GRAY,"■ GRAY")
	print(BLACK,"■ BLACK")
	print(RED,"■ RED")
	print(MAROON,"■ MAROON")
	print(YELLOW,"■ YELLOW")
	print(OLIVE,"■ OLIVE")
	print(LIME,"■ LIME")
	print(GREEN,"■ GREEN")
	print(CYAN,"■ CYAN")
	print(TEAL,"■ TEAL")
	print(BLUE,"■ BLUE")
	print(NAVY,"■ NAVY")
	print(MAGENTA,"■ MAGENTA")
	print(PURPLE,"■ PURPLE")
	print(BGWHITE,"■ BGWHITE")
	print(BGSILVER,"■ BGSILVER")
	print(BGGRAY,"■ BGGRAY")
	print(BGBLACK,"■ BGBLACK")
	print(BGRED,"■ BGRED")
	print(BGMAROON,"■ BGMAROON")
	print(BGYELLOW,"■ BGYELLOW")
	print(BGOLIVE,"■ BGOLIVE")
	print(BGLIME,"■ BGLIME")
	print(BGGREEN,"■ BGGREEN")
	print(BGCYAN,"■ BGCYAN")
	print(BGTEAL,"■ BGTEAL")
	print(BGBLUE,"■ BGBLUE")
	print(BGNAVY,"■ BGNAVY")
	print(BGMAGENTA,"■ BGMAGENTA")
	print(BGPURPLE,"■ BGPURPLE")
	input()