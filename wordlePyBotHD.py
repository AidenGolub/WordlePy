import sys
import enchant
import random
import urllib.request
import csv
import time
with open('woords.lst','r+') as f:
	WORDS=f.read().splitlines()
dd = enchant.Dict("en_US")
goodList = []
for i in WORDS:
	if dd.check(i) and len(i) == 5:
		goodList.append(i)
incorrectList=[]
cc1=[]
guessWords=[]
def spacing():
	for x in range(0,100):
		print()
flagger=0
#len(goodList) = 6334 words = 40,119,556 combinations
cc2=[]
cc3=[]
cc4=[]
cc5=[]
check=0
nnn = True
while nnn == True:
	ratesInfo=0
	check=0
	sway1=[]
	sway2=[]
	sway3=[]
	sway4=[]
	uppCor=[]
	cor=[]
	f=4
	wearyList=[]
	test1=[]
	test2=[]
	test3=[]
	test=[]
	percentNum=0
	beg = True
	while beg == True:
		ss = input("Enter your guess from Wordle (EX: weary): ").lower()
		if ss == "" and flagger >= 1:
			ss = guessWords[len(guessWords)-1]
			print("Guess from Wordle:",ss.upper())
			beg = False
		if ss == "inclear":
			incorrectList = []
			guessWords = []
			flagger=0
			cc1=[]
			cc2=[]
			cc3=[]
			cc4=[]
			cc5=[]
			print("Cleared")
		elif len(ss) == 5 and "-" not in ss:
			beg = False
	beg = True
	while beg == True:
		s = input("Enter a Word from Wordle with its hints (EX: We--Y): ")
		if len(s) == 5:
			beg = False
	print()
	if len(s) == 5:
		scheck = s.lower()
		if scheck[0] == "-":
			if ss[0] not in scheck:
				incorrectList.append(ss[0])
		if scheck[1] == "-":
			if ss[1] not in scheck:
				incorrectList.append(ss[1])
		if scheck[2] == "-":
			if ss[2] not in scheck:
				incorrectList.append(ss[2])
		if scheck[3] == "-":
			if ss[3] not in scheck:
				incorrectList.append(ss[3])
		if scheck[4] == "-":
			if ss[4] not in scheck:
				incorrectList.append(ss[4])
		if s[0] != "-" and s[0].islower():
			cc1.append(s[0])
		if s[1] != "-" and s[1].islower():
			cc2.append(s[1])
		if s[2] != "-" and s[2].islower():
			cc3.append(s[2])
		if s[3] != "-" and s[3].islower():
			cc4.append(s[3])
		if s[4] != "-" and s[4].islower():
			cc5.append(s[4])
		if s[0].isupper():
			for i in goodList:
				if i[0] == s[0].lower():
					sway1.append(i[0].upper()+i[1]+i[2]+i[3]+i[4])
		else:
			for j in goodList:
				sway1.append(j)
		if s[1].isupper():
			for i in sway1:
				if i[1] == s[1].lower():
					sway2.append(i[0]+i[1].upper()+i[2]+i[3]+i[4])
		else:
			for j in sway1:
				sway2.append(j)
		if s[2].isupper():
			for i in sway2:
				if i[2] == s[2].lower():
					sway3.append(i[0]+i[1]+i[2].upper()+i[3]+i[4])
		else:
			for j in sway2:
				sway3.append(j)
		if s[3].isupper():
			for i in sway3:
				if i[3] == s[3].lower():
					sway4.append(i[0]+i[1]+i[2]+i[3].upper()+i[4])
		else:
			for j in sway3:
				sway4.append(j)
		if s[4].isupper():
			for i in sway4:
				if i[4] == s[4].lower():
					uppCor.append(i[0]+i[1]+i[2]+i[3]+i[4].upper())
		else:
			for j in sway4:
				uppCor.append(j)
		letChecklow = []
		letCheckup = []
		letCheck = []
		letCheckno = 0
		for i in s:
			if i != "-":
				letCheck.append(i)
		for o in letCheck:
			if o.islower():
				letChecklow.append(o)
			else:
				letCheckup.append(o)
		if len(letCheckup) == 0 and len(letChecklow) >= 1:
			for j in goodList:
				uppCor.append(j)
		lowLet=[]
		for i in s:
			if i != "-" and i.islower():
				lowLet.append(i)
		lowLen=len(lowLet)
		for o in uppCor:
			if lowLen == 1:
				nu = s.count(lowLet[0])
				bu = o.count(lowLet[0])
				if nu == bu:
					cor.append(o)
			elif lowLen == 2:
				nu1 = s.count(lowLet[0])
				bu1 = o.count(lowLet[0])
				nu2 = s.count(lowLet[1])
				bu2 = o.count(lowLet[1])
				if nu1 == bu1 and nu2 == bu2:
					cor.append(o)
			elif lowLen == 3:
				nu1 = s.count(lowLet[0])
				bu1 = o.count(lowLet[0])
				nu2 = s.count(lowLet[1])
				bu2 = o.count(lowLet[1])
				nu3 = s.count(lowLet[2])
				bu3 = o.count(lowLet[2])
				if nu1 == bu1 and nu2 == bu2 and nu3 == bu3:
					cor.append(o)
			elif lowLen == 4:
				nu1 = s.count(lowLet[0])
				bu1 = o.count(lowLet[0])
				nu2 = s.count(lowLet[1])
				bu2 = o.count(lowLet[1])
				nu3 = s.count(lowLet[2])
				bu3 = o.count(lowLet[2])
				nu4 = s.count(lowLet[3])
				bu4 = o.count(lowLet[3])
				if nu1 == bu1 and nu2 == bu2 and nu3 == bu3 and nu4 == bu4:
					cor.append(o)
			elif lowLen == 5:
				nu1 = s.count(lowLet[0])
				bu1 = o.count(lowLet[0])
				nu2 = s.count(lowLet[1])
				bu2 = o.count(lowLet[1])
				nu3 = s.count(lowLet[2])
				bu3 = o.count(lowLet[2])
				nu4 = s.count(lowLet[3])
				bu4 = o.count(lowLet[3])
				nu5 = s.count(lowLet[4])
				bu5 = o.count(lowLet[4])
				if nu1 == bu1 and nu2 == bu2 and nu3 == bu3 and nu4 == bu4 and nu5 == bu5:
					cor.append(o)
			elif lowLen == 0:
				cor.append(o)
		ttt = 0
		for o in cor:
			ttt = 0
			for re in range(0,5):
				if s[re] != "-" and s[re].islower():
					if o[re] == s[re]:
						ttt+=1
			if ttt == 0:
				test1.append(o)
		for gg in test1:
			ppp = 0
			for s in gg:
				if s.lower() in incorrectList:
					ppp+=1
			if ppp == 0:
				test2.append(gg)
		for o in test2:
			ppp = 0
			if o[0] not in cc1 and o[1] not in cc2 and o[2] not in cc3 and o[3] not in cc4 and o[4] not in cc5:
				test3.append(o.lower())
		test = list(dict.fromkeys(test3))
		for lll in test:
			percentNum+=1
			checker = []
			for ppp in test: #change to goodlist for entire vocab (slower)
				count = 0
				naughtyList = []
				for x in range(0,1):
					q2=""
					wordLetList=[]
					guessRep=[]
					guesses="Previous Guesses: "
					letList=["a", "b", "c", "d", "e", "f", "g", "h", "i"
					, "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", 
					"t", "u", "v", "w", "x", "y", "z"]
					def spacing():
						for x in range(0,39):
							print()
					def won():
						spacing()
						guessLists()
						print()
						print("Congrats, you found the word: "+word.upper()+"!")
					def guessLists():
						percent=round(float(float(percentNum)/(len(test))*100.0),2)
						c1n = str(c1)[1:-1]
						c1n = c1n.replace(',',' ')
						c1n = c1n.replace("'",'')
						print(" "+c1n," "+lll,ppp,"("+str(percent)+"%)")
					c1=[]
					correctWp=""
					correctWtP=""
					incorrect=""
					if q2 == "1" or q2 == "":
						nn = True
						ntyornot = ""
						word = lll
						for i in word:
							wordLetList.append(i)
					wordLen=len(wordLetList)
					for z in range(0,wordLen):
						c1.append("-")
					bp=0
					xm=0
					for n in range(0,1):
						guess = ppp
						guessLetList=[char for char in guess]
						guesses+=str(guess)+" "
						guessRep.append(str(guess))
						bp=0
						xm=0
						if n==0:
							guess1 = "("+guess+")"
							ccL = c1
						c=0
						ccL.clear()
						for i in guessLetList:
							if i == wordLetList[c]:
								ccL.append(i.upper())
							elif i != wordLetList[c] and i in wordLetList:
								ccL.append(i.lower())
							else:
								ccL.append("-")
							c+=1
						oh=0
						for j in ccL:
							if j.isupper():
								oh+=1
						if n == 0:
							c1 = ccL
						if oh == wordLen:
							hh=0
						splG=str(word)
						splitWordList = list(set(splG))
						if n == 0:
							ccL = c1
						for i in splitWordList:
							wordCount = word.count(i)
							guessLowCount = ccL.count(i)
							guessUppCount = ccL.count(i.upper())
							guessCount = guessLowCount + guessUppCount
							uppCount = 0
							if guessCount > wordCount:
								for j in ccL:
									if j == i.upper():
										uppCount += 1
								lowerDel = int(guessCount) - int(wordCount)
								zz = 0
								fl = 0
								for j in ccL:			
									if j.lower() == i.lower():
										if j.islower():
											del ccL[zz]
											ccL.insert(zz,"-")
											fl += 1
										if fl == lowerDel:
											break
									zz+=1
						if n == 0:
							c1 = ccL
						guessLists()
					break
				for i in c1:
					if i.isupper():
						count+=2
					elif i.islower():
						count+=1
				checker.append(count)
			total = sum(checker)/len(checker)
			if total > check:
				bestWord = lll
				check = total
				ratesInfo = total
		print()
		pChance = round(float(float(ratesInfo)/10.0)*100,2)
		print("Best word: "+bestWord.upper(),"("+str(pChance)+"% chance of receiving a hint)")
		print()
		guessWords.append(bestWord)
		testn = str(test)[1:-1]
		testn = testn.replace("'",'')
		print("All possible words: ["+testn+"]")
		print()
		flagger+=1
