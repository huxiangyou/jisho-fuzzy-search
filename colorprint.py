"""Print with colors

Python 3.12

Hu Xiangyou
March 24, 2021
May 12, 2021
Oct 22, 2021
June 11, 2024

Part of https://github.com/huxiangyou/hulubot
under MIT License
"""

import ctypes
import builtins

C_WHITE=15
C_SILVER=7
C_GRAY=8
C_BLACK=0
C_RED=12
C_MAROON=4
C_YELLOW=14
C_OLIVE=6
C_LIME=10
C_GREEN=2
C_CYAN=11
C_TEAL=3
C_BLUE=9
C_NAVY=1
C_MAGENTA=13
C_PURPLE=5

class Color:
	def __init__(self,foreground:int=0,background:int=0):
		self.code=foreground|background<<4

WHITE=Color(C_WHITE)
SILVER=Color(C_SILVER)
GRAY=Color(C_GRAY)
BLACK=Color(C_BLACK)
RED=Color(C_RED)
MAROON=Color(C_MAROON)
YELLOW=Color(C_YELLOW)
OLIVE=Color(C_OLIVE)
LIME=Color(C_LIME)
GREEN=Color(C_GREEN)
CYAN=Color(C_CYAN)
TEAL=Color(C_TEAL)
BLUE=Color(C_BLUE)
NAVY=Color(C_NAVY)
MAGENTA=Color(C_MAGENTA)
PURPLE=Color(C_PURPLE)

BGWHITE=Color(C_BLACK,C_WHITE)
BGSILVER=Color(C_BLACK,C_SILVER)
BGGRAY=Color(C_WHITE,C_GRAY)
BGBLACK=Color(C_WHITE,C_BLACK)
BGRED=Color(C_WHITE,C_RED)
BGMAROON=Color(C_WHITE,C_MAROON)
BGYELLOW=Color(C_BLACK,C_YELLOW)
BGOLIVE=Color(C_WHITE,C_OLIVE)
BGLIME=Color(C_BLACK,C_LIME)
BGGREEN=Color(C_WHITE,C_GREEN)
BGCYAN=Color(C_BLACK,C_CYAN)
BGTEAL=Color(C_WHITE,C_TEAL)
BGBLUE=Color(C_WHITE,C_BLUE)
BGNAVY=Color(C_WHITE,C_NAVY)
BGMAGENTA=Color(C_WHITE,C_MAGENTA)
BGPURPLE=Color(C_WHITE,C_PURPLE)

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
				ctypes.windll.kernel32.SetConsoleTextAttribute(ctypes.windll.kernel32.GetStdHandle(-11),DEFAULT.code)
			if index+1==len(args):
				builtins.print(arg,end="",flush=True)
				ctypes.windll.kernel32.SetConsoleTextAttribute(ctypes.windll.kernel32.GetStdHandle(-11),DEFAULT.code)
				builtins.print(end=end,flush=True)
			else:
				builtins.print(arg,end=sep,flush=True)

print=_print

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
