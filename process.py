# -*- coding: utf-8 -*-
#March 6, 2023
#Hu Xiangyou

import re

print("reading.")

with open('dict_original.txt','r',encoding='utf-8') as f:
	original=f.read().splitlines()

result=[]

flags={
	'adj-f','adj-i','adj-ix','adj-ku','adj-na','adj-nari','adj-no','adj-pn','adj-shiku','adj-t',
	'adv','adv-to',
	'n','n-pref','n-suf','num','pn',
	'v-unspec','v1','v1-s',
	'v2a-s','v2a-s','v2b-k','v2b-s','v2d-k','v2d-s','v2g-k','v2g-s','v2h-k','v2h-s','v2k-k','v2k-s','v2m-k','v2m-s','v2n-s','v2r-k','v2r-s','v2s-s','v2t-k','v2t-s','v2w-s','v2y-k','v2y-s','v2z-s'
	'v4b','v4g','v4h','v4k','v4m','v4n','v4r','v4s','v4t',
	'v5aru','v5b','v5g','v5k','v5k-s','v5m','v5n','v5r','v5r-i','v5s','v5t','v5u','v5u-s',
	'vk','vn','vr','vs','vs-c','vs-i','vs-s','vz',
	'company','group','organization',
	'surname','given','person',
	'place','product','ev','serv','work',
	'aux','aux-adj','aux-v',
	'conj','cop','ctr',
	'exp','int',
	'abbr',#'id','proverb','quote','sl','net-sl',
	'pref','prt','suf',
	'unc',
	'P',
	'arch','dated','hist','rare',
	'ik','iK','io','ok','oK','rk','rK','sk','sK','uk','uK',
}

def i1toi2(i1):
	"""convert spelling to reading. e.g. エマ・ヴェルデ -> えまゔぇるで"""
	return "".join(chr(ord(i1i)-96) if re.match(r'[ァ-ヶ]',i1i) else i1i for i1i in i1).replace("・","").replace("〜","ー")
	# return i1.replace("・","")

print("handling.")

for i in original:
	i3=re.findall(r'(?<=\()[^\n"()〆〇㐀-䶿一-鿿豈-舘並-龎𠀀-𪛟𪜀-𫜹𫝀-𫠝𫠠-𬺡𬺰-𮯠𱍐-𲎯丽-𪘀𰀀-𱍊ぁ-ゖァ-ヺ ]+?(?=\))',i.split('/',1)[1])
	i3=filter(lambda x:not re.fullmatch(r'^[\d\-\.]+$',x),i3)
	i3n=set()
	for i3i in i3:
		i3n.update(i3i.split(','))
	i3=','.join(sorted(i3n&flags))
	i4=i.split(" /",1)[1]

	i4=re.sub(r'/EntL[^\n ]+?(?=/)','',i4)

	i1=re.findall(r'^[^\[/]+?(?= \[| /)',i)[0]
	i1=i1.split(";")
	i1={re.sub(r'\([a-zA-Z]+?\)','',i1i):','.join(sorted(re.findall(r'(?<=\()[a-zA-Z]+?(?=\))',i1i))) for i1i in i1}

	i2=re.findall(r'(?<=\[)[^\n\[\]]+?(?=\])',i)
	if i2:
		i2=i2[0].replace("・","").split(";")
		for i2i in i2:
			i2f=','.join(sorted(re.findall(r'(?<=\()[a-zA-Z]+?(?=\))',i2i)))
			i2toi1=re.findall(r'(?<=\()[^\n\(\)]*?[〆〇㐀-䶿一-鿿豈-舘並-龎𠀀-𪛟𪜀-𫜹𫝀-𫠝𫠠-𬺡𬺰-𮯠𱍐-𲎯丽-𪘀𰀀-𱍊ぁ-ゖァ-ヺ][^\n\(\)]*?(?=\))',i2i)
			i2i=re.sub(r'\([^\n() ]+?\)',"",i2i)
			if i2toi1:
				i2toi1=i2toi1[0].split(",")
				for i2toi1i in i2toi1:
					result.append([i2toi1i,i1toi2(i2i),';'.join(filter(None,[i1.get(i2toi1i,''),i2f,i3])),i4])
			else:
				for i1i in i1:
					result.append([i1i,i1toi2(i2i),';'.join(filter(None,[i1.get(i1i,''),i2f,i3])),i4])
					if i2i!=i1toi2(i2i):
						result.append([i2i,i1toi2(i2i),';'.join(filter(None,[i2f,i3])),i4])
	else:
		for i1i in i1:
			result.append([i1i,i1toi2(i1i),';'.join(filter(None,[i1.get(i1i,''),'',i3])),i4])

print("sorting.")

result.sort(key=lambda w:(
	bool(re.findall(r'(?<=\b)(arch|hist|dated|rare)(?=,|;|$)',w[2]))-bool(re.findall(r'(?<=\b)P(?=,|;|$)',w[2])),
	# -bool(re.findall(r'(?<=\b)P(?=,|;|$)',w[2])),
	len(w[1]),len(w[0]),w[1],w[0]
))
# result=list(map(lambda r:r[:2],result))
result=list(map('\t'.join,result))

print("writing.")

with open('dict.txt','w',encoding='utf-8') as f:
	result_dict={}
	for r in result:
		if r not in result_dict:
			f.write(r+"\n")
			result_dict[r]=0

input("Done.")
