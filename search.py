# -*- coding: utf-8 -*-
#July 4, 2020
#November 16, 2020
#March 6, 2023
#Hu Xiangyou

import re
from colorprint import *
import jaconv

words=[]
def refresh():
	global words
	with open('dict.txt','r',encoding='utf-8') as f:
		words=list(map(lambda x:x.split('\t'),f.read().splitlines()))

refresh()
print(LIME,len(words),DEFAULT,'words')

wilds={
'katakana':'[ァ-ヺー]',
'hiragana':'[ぁ-ゖ]',
'kanji':'[〆〇㐀-䶿一-鿿豈-舘並-龎𠀀-𪛟𪜀-𫜹𫝀-𫠝𫠠-𬺡𬺰-𮯠𱍐-𲎯丽-𪘀𰀀-𱍊𮯰-𮹝]',
'by':'びゃ|びゅ|びぇ|びょ|ビャ|ビュ|ビェ|ビョ',
'ch':'ち|ちゃ|ちゅ|ちぇ|ちょ|チ|チャ|チュ|チェ|チョ',
'cw':'つ|つぁ|つぃ|つぇ|つぉ|ず|ずぃ|づ|ツ|ツァ|ツィ|ツェ|ツォ|ズ|ズィ|ヅ',
'cy':'ちゃ|ちゅ|ちぇ|ちょ|チャ|チュ|チェ|チョ',
'dh':'でゃ|でぃ|でぅ|でゅ|でぇ|でょ|デャ|ディ|デゥ|デュ|デェ|デョ',
'dw':'どぁ|どぃ|どぅ|どぇ|どぉ|ドァ|ドィ|ドゥ|ドェ|ドォ',
'dy':'ぢゃ|ぢゅ|ぢぇ|ぢょ|ヂャ|ヂュ|ヂェ|ヂョ',
'dz':'ぢ|づ|ヂ|ヅ',
'fw':'ふぁ|ふぃ|ふぅ|ふぇ|ふぉ|ファ|フィ|フゥ|フェ|フォ',
'fy':'ふゃ|ふぃ|ふゅ|ふぇ|ふょ|フィ|フェ|フャ|フュ|フョ',
'gw':'ぐぁ|ぐぃ|ぐぅ|ぐぇ|ぐぉ|ぐゎ|グァ|グィ|グゥ|グェ|グォ|ぐヮ',
'gy':'ぎゃ|ぎゅ|ぎぇ|ぎょ|ギャ|ギュ|ギェ|ギョ',
'hy':'ひゃ|ひゅ|ひぇ|ひょ|ヒャ|ヒュ|ヒェ|ヒョ',
'jy':'じゃ|じゅ|じぇ|じょ|ぢゃ|ぢゅ|ぢぇ|ぢょ|ジャ|ジュ|ジェ|ジョ|ヂャ|ヂュ|ヂェ|ヂョ',
'kw':'くぁ|くぃ|くぅ|くぇ|くぉ|くゃ|くゅ|くょ|くゎ|クァ|クィ|クゥ|クェ|クォ|クャ|クュ|クョ|クヮ',
'ky':'きゃ|きゅ|きぇ|きょ|キャ|キュ|キェ|キョ',
'lx':'ぁ|ぃ|ぅ|ぇ|ぉ|ゃ|ゅ|ょ|ゎ|ァ|ィ|ゥ|ェ|ォ|ャ|ュ|ョ|ヮ',
'ly':'ゃ|ゅ|ょ|ャ|ュ|ョ',
'my':'みゃ|みゅ|みぇ|みょ|ミャ|ミュ|ミェ|ミョ',
'nn':'ん|ン',
'ny':'にゃ|にゅ|にぇ|にょ|ニャ|ニュ|ニェ|ニョ',
'py':'ぴゃ|ぴゅ|ぴぇ|ぴょ|ピャ|ピュ|ピェ|ピョ',
'qw':'くぁ|くぃ|くぅ|くぇ|くぉ|くゎ|クァ|クィ|クゥ|クェ|クォ|クヮ',
'qy':'くゃ|くぃ|くゅ|くぇ|くょ|クャ|クィ|クュ|クェ|クョ',
'ry':'りゃ|りゅ|りぇ|りょ|リャ|リュ|リェ|リョ',
'sh':'し|しゃ|しゅ|しぇ|しょ|シ|シャ|シュ|シェ|ショ',
'sw':'すぁ|すぃ|すぅ|すぇ|すぉ|スァ|スィ|スゥ|スェ|スォ',
'sy':'しゃ|しゅ|しぇ|しょ|すぃ|シャ|シュ|シェ|ショ|スィ',
'th':'てゃ|てぃ|てぅ|てゅ|てぇ|てょ|テャ|ティ|テゥ|テュ|テェ|テョ',
'ts':'つ|つぁ|つぃ|つぇ|つぉ|ツ|ツァ|ツィ|ツェ|ツォ',
'tw':'とぁ|とぃ|とぅ|とぇ|とぉ|トァ|トィ|トゥ|トェ|トォ',
'ty':'ちゃ|ちゅ|ちぇ|ちょ|チャ|チュ|チェ|チョ',
'vy':'ゔぁ|ゔぃ|ゔゅ|ゔぇ|ゔぉ|ヴァ|ヴィ|ヴュ|ヴェ|ヴォ',
'wy':'うぁ|うぃ|うぇ|うぉ|ウァ|ウィ|ウェ|ウォ',
'xy':'ゃ|ゅ|ょ|ャ|ュ|ョ',
'zw':'ずぃ|ズィ',
'zy':'じゃ|じゅ|じぇ|じょ|ぢゃ|ぢゅ|ぢぇ|ぢょ|ジャ|ジュ|ジェ|ジョ|ヂャ|ヂュ|ヂェ|ヂョ',
 'a':'あ|か|が|さ|ざ|た|だ|な|は|ば|ぱ|ま|や|ら|わ|ぁ|ゃ|ア|カ|ガ|サ|ザ|タ|ダ|ナ|ハ|バ|パ|マ|ヤ|ラ|ワ|ァ|ャ|ヵ|ヶ',
 'b':'ば|び|ぶ|べ|ぼ|バ|ビ|ブ|ベ|ボ',
 'c':'ち|ちゃ|ちゅ|ちぇ|ちょ|じ|じゃ|じゅ|じぇ|じょ|ぢ|ぢゃ|ぢゅ|ぢぇ|ぢょ|チ|チャ|チュ|チェ|チョ|ジ|ジャ|ジュ|ジェ|ジョ|ヂ|ヂャ|ヂュ|ヂェ|ヂョ',
 'd':'だ|ぢ|づ|で|ど|ダ|ヂ|ヅ|デ|ド',
 'e':'え|け|げ|せ|ぜ|て|で|ね|へ|べ|ぺ|め|れ|ゑ|ぇ|エ|ケ|ゲ|セ|ゼ|テ|デ|ネ|ヘ|ベ|ペ|メ|レ|ヱ|ェ',
 'f':'ふ|ふぁ|ふぃ|ふゅ|ふぇ|ふぉ|フ|ファ|フィ|フュ|フェ|フォ',
 'g':'が|ぎ|ぐ|げ|ご|ガ|ギ|グ|ゲ|ゴ|ヵ|ヶ',
 'h':'は|ひ|ふ|へ|ほ|ハ|ヒ|フ|ヘ|ホ',
 'i':'い|き|ぎ|し|じ|ち|ぢ|に|ひ|び|ぴ|み|り|ゐ|ぃ|イ|キ|ギ|シ|ジ|チ|ヂ|ニ|ヒ|ビ|ピ|ミ|リ|ヰ|ィ',
 'j':'じ|ぢ|ジ|ヂ',
 'k':'か|き|く|け|こ|カ|キ|ク|ケ|コ',
 'l':'ぁ|ぃ|ぅ|ぇ|ぉ|っ|ゃ|ゅ|ょ|ゎ|ゕ|ゖ|ァ|ィ|ゥ|ェ|ォ|ッ|ャ|ュ|ョ|ヮ|ヵ|ヶ',
 'm':'ま|み|む|め|も|マ|ミ|ム|メ|モ',
 'n':'な|に|ぬ|ね|の|ナ|ニ|ヌ|ネ|ノ',
 'o':'お|こ|ご|そ|ぞ|と|ど|の|ほ|ぼ|ぽ|も|よ|ろ|を|ぉ|ょ|オ|コ|ゴ|ソ|ゾ|ト|ド|ノ|ホ|ボ|ポ|モ|ヨ|ロ|ヲ|ォ|ョ',
 'p':'ぱ|ぴ|ぷ|ぺ|ぽ|パ|ピ|プ|ペ|ポ',
 'q':'くぁ|くぃ|くぅ|くぇ|くぉ|くゃ|くゅ|くょ|くゎ|クァ|クィ|クゥ|クェ|クォ|クャ|クュ|クョ|クヮ',
 'r':'ら|り|る|れ|ろ|ラ|リ|ル|レ|ロ',
 's':'さ|し|す|せ|そ|サ|シ|ス|セ|ソ',
 't':'た|ち|つ|て|と|タ|チ|ツ|テ|ト',
 'u':'う|く|ぐ|す|ず|つ|づ|ぬ|ふ|ぶ|ぷ|む|ゆ|る|ぅ|ゅ|ゔ|ウ|ク|グ|ス|ズ|ツ|ヅ|ヌ|フ|ブ|プ|ム|ユ|ル|ゥ|ュ|ヴ',
 'v':'ゔ|ゔぁ|ゔぃ|ゔゅ|ゔぇ|ゔぉ|ヴ|ヴァ|ヴィ|ヴュ|ヴェ|ヴォ',
 'w':'わ|ゐ|ゑ|を|うぁ|うぃ|うぇ|うぉ|(?<!^)は|ワ|ヰ|ヱ|ヲ|ウァ|ウィ|ウェ|ウォ',
 'x':'あ|い|う|え|お|っ|(?<!^)へ|ア|イ|ウ|エ|オ|ー|ッ',
 'y':'や|ゆ|よ|いぇ|ヤ|ユ|ヨ|イェ',
 'z':'ざ|じ|ず|ぜ|ぞ|ぢ|づ|ザ|ジ|ズ|ゼ|ゾ|ヂ|ヅ',
}

while True:
	print(GRAY,'>>> ',end="")
	qo=input()
	if not qo:
		continue
	if 'hiragana' in qo and not re.findall(r'[a-z]',qo.replace('hiragana','')):
		print(MAROON,"Hiragana only is forbidden.")
		print(GRAY,"====================")
		continue
	q=qo
	newWords=[]
	for w,wt in wilds.items():
		q=q.replace(w,'('+wt+')')
	qj=jaconv.convert(q,'zh2ja')
	q=list(q)
	for qi,(qq,qjq) in enumerate(zip(q,qj)):
		if qq!=qjq:
			q[qi]='[{}{}]'.format(qq,qjq)
	q=''.join(q)
	q=q.replace('\'','').replace(' ','.{0,4}').replace('$','ー?$')
	try:
		if not re.fullmatch(r'^[\(\)\.\* ]+$',q):
			if q!=qo:
				print(GRAY,"<<<",q)
			for w in words:
				if re.findall(q,w[0]) or re.findall(q,w[1]):
					newWords.append(w)
		if not newWords and re.fullmatch(r'^[a-z ]{3,}$',qo):
			q='.*'.join(qo.split())
			if q!=qo:
				print(GRAY,"<<<",q)
			for w in words:
				if re.findall(q,w[3],flags=re.IGNORECASE):
					newWords.append(w)
	except:
		print(MAROON,"×")
		print(GRAY,"====================")
		continue
	newLen=len(newWords)
	leftLen=newLen
	exactWords=[]
	hasExact=False
	for w in newWords:
		if q==w[0] or q==w[1] or re.fullmatch(q,w[0]) or re.fullmatch(q,w[1]):
			exactWords.append(w)
			hasExact=True
	if len(exactWords)>200:
		print(LIME,newLen,DEFAULT,"words found, including",LIME,len(exactWords),DEFAULT,"exact words.",MAROON,"Too many.",DEFAULT,"Show?",end="")
		if not input():
			print(GRAY,"====================")
			refresh()
			continue
	for w in exactWords:
		if w[0]==w[1]:
			print(YELLOW,w[1],TEAL,w[2],GRAY,w[3],sep='\t')
		else:
			print(YELLOW,w[0],SILVER,w[1],TEAL,w[2],GRAY,w[3],sep='\t')
		leftLen-=1
	if hasExact:
		newWords=list(filter(lambda w:q!=w[0] and q!=w[1] and not re.fullmatch(q,w[0]) and not re.fullmatch(q,w[1]),newWords))
		leftLen=len(newWords)
		if leftLen>0:
			print(LIME,newLen,DEFAULT,"words found.",LIME,leftLen,DEFAULT,"more.","Show?",end="")
			if not input():
				print(GRAY,"====================")
				refresh()
				continue
	while leftLen>0:
		for w in (newWords[-leftLen:-leftLen+100] if leftLen>100 else newWords[-leftLen:]):
			if w[0]==w[1]:
				print(YELLOW,w[1],TEAL,w[2],GRAY,w[3],sep='\t')
			else:
				print(YELLOW,w[0],SILVER,w[1],TEAL,w[2],GRAY,w[3],sep='\t')
			leftLen-=1
		if leftLen>0:
			print(LIME,newLen,DEFAULT,"words found.",LIME,leftLen,DEFAULT,"more.","Show?",end="")
			if not input():
				break
		else:
			print(LIME,newLen,DEFAULT,"words found.")
	print(GRAY,"====================")
	refresh()

input('Done.')
