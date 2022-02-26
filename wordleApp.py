import sys
import enchant
import random
import urllib.request
rep = True
tep = True
won = False
pz = 0
while tep == True:
	while rep == True:
		try:
			word_site = "https://www.mit.edu/~ecprice/wordlist.10000" #Website database with 10,000 unique words
			response = urllib.request.urlopen(word_site)
			txt = response.read().decode() #HTML splicer
			WORDS = txt.splitlines() #creates a str list
		except:
			print()
		dicCheck = enchant.Dict("en_US") #imports the English-US dictionary
		if pz == 0:
			print("Welcome to my version of Wordle. (Hint: uppercase letters = green & lowercase letters = yellow)")
			print()
		pz+=1
		let = True
		while let == True:
			q2=input("How many players: 1, 2, or ?: ") #different gamemodes
			if q2 == "1" or q2 == "2" or q2 == "":
				if len(q2) == 1 or q2 == "":
					let = False
			else:
				let = True
			if q2 == "?":
				print("                                                                                                         ")
				print(" vvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvv")
				print("|   1. Chose either 1 or 2 players. 1 Player mode selects a random 5-letter word out of a list of 10,000.    ")
				print("|      The second option, 2 player mode, allows a person to input a word, regardless of length.")
				print("|")
				print("|   2. Once you see the game graphic, enter a real word with the correct length.                   ")
				print("|")
				print("|   3. When you press enter to submit your guess, the graphic will change:                      ")
				print("|")
				print("|      Uppercase = Green (Letter is correct and at that position)                          ")
				print("|      Lowercase = Yellow (Letter is correct, but is not at that position)                          ")
				print("|      (-) = Gray (Letter is not found in the word)                         ")
				print("|")
				print("|   4. You are given 6 tries to guess the correct word.                          ")
				print("|")
				print("|   GOOD LUCK!                                                                                           ")
				print(" vvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvv")
				print("                                                                                                         ") 
		print()
		wordLetList=[]
		guessRep=[] #List to check for repeating guesses
		guesses="Previous Guesses: "
		letList=["a", "b", "c", "d", "e", "f", "g", "h", "i"
		, "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", 
		"t", "u", "v", "w", "x", "y", "z"]
		guess1 = ""
		guess2 = ""
		guess3 = ""
		guess4 = ""
		guess5 = ""
		guess6 = ""
		def guessLists():
			c1n = str(c1)[1:-1]
			c1n = c1n.replace(',',' ')
			c1n = c1n.replace("'",'')
			c2n = str(c2)[1:-1]
			c2n = c2n.replace(',',' ')
			c2n = c2n.replace("'",'')
			c3n = str(c3)[1:-1]
			c3n = c3n.replace(',',' ')
			c3n = c3n.replace("'",'')
			c4n = str(c4)[1:-1]
			c4n = c4n.replace(',',' ')
			c4n = c4n.replace("'",'')
			c5n = str(c5)[1:-1]
			c5n = c5n.replace(',',' ')
			c5n = c5n.replace("'",'')
			c6n = str(c6)[1:-1]
			c6n = c6n.replace(',',' ')
			c6n = c6n.replace("'",'')
			print()
			print(" 1)   "+c1n," "+guess1)
			print(" 2)   "+c2n," "+guess2)
			print(" 3)   "+c3n," "+guess3)
			print(" 4)   "+c4n," "+guess4)
			print(" 5)   "+c5n," "+guess5)
			print(" 6)   "+c6n," "+guess6)
		def guessLists1():
			if correctWp != "":
				print("Correct and Place:",correctWp)
			if correctWtP != "":
				print("Correct:",correctWtP)
			if incorrect != "":
				print("Incorrect:",incorrect)
			print("Last guess: "+guess)
			c1n = str(c1)[1:-1]
			c1n = c1n.replace(',',' ')
			c1n = c1n.replace("'",'')
			c2n = str(c2)[1:-1]
			c2n = c2n.replace(',',' ')
			c2n = c2n.replace("'",'')
			c3n = str(c3)[1:-1]
			c3n = c3n.replace(',',' ')
			c3n = c3n.replace("'",'')
			c4n = str(c4)[1:-1]
			c4n = c4n.replace(',',' ')
			c4n = c4n.replace("'",'')
			c5n = str(c5)[1:-1]
			c5n = c5n.replace(',',' ')
			c5n = c5n.replace("'",'')
			c6n = str(c6)[1:-1]
			c6n = c6n.replace(',',' ')
			c6n = c6n.replace("'",'')
			print()
			print(" 1)   "+c1n," "+guess1)
			print(" 2)   "+c2n," "+guess2)
			print(" 3)   "+c3n," "+guess3)
			print(" 4)   "+c4n," "+guess4)
			print(" 5)   "+c5n," "+guess5)
			print(" 6)   "+c6n," "+guess6)
		def spacing():
			for x in range(0,39):
				print()	
		c1=[] #creates empty lists
		c2=[]
		c3=[]
		c4=[]
		c5=[]
		c6=[]
		correctWp=""
		correctWtP=""
		incorrect=""
		if q2 == "2":
			#word input [2 players]
			ntyornot = "w"
			y=True
			po=True
			while po == True:
				word=input("Enter a word here: ").lower()
				if word == "":
					print("MESSAGE: Please enter a real word")
					print()
				elif dicCheck.check(word):
					po = False
				else:
					print("MESSAGE: Please enter a real word")
					print()
			#word checker
			while y==True:
				if word=="":
					po=True
					while po == True:
						word=input("Enter a word here: ").lower()
						if word == "":
							print("MESSAGE: Please enter a real word")
							print()
						elif dicCheck.check(word):
							po = False
						else:
							print("MESSAGE: Please enter a real word")
							print()
				for i in word:
					if i in letList:
						wordLetList.append(i)
					elif i not in letList and i == " ":
						print("Please enter a correct word")
						y=True
				y=False
					
		elif q2 == "1" or q2 == "":
			#word input [1 player]
			ntyornot = "w"
			t=True
			while t == True:
				if ntyornot == "w" or ntyornot == "":
					word=random.choice(WORDS)
				if len(word) == 5 and dicCheck.check(word): #change default length here
					t=False
			for i in word:
				wordLetList.append(i)
		wordLen=len(wordLetList) #finds correct input length
		for z in range(0,wordLen):#fills all lists with blank chars to start off
			c1.append("-")
			c2.append("-")
			c3.append("-")
			c4.append("-")
			c5.append("-")
			c6.append("-")
		spacing()
		bp=0
		xm=0
		if ntyornot == "w" or ntyornot == "":
			print("You are playing: Wordle")
			adin = ""
		print()
		print("You have 6 tries to guess a "+adin+"word "+str(wordLen)+" letters long")
		print()
		for n in range(0,6): #6 = number of rows *DON'T change*
			#guess starting
			if n == 0:
				guessLists()
			else:
				guessLists1()
			print()
			b = True
			while b == True:
				f=0
				d=True
				while d == True:
					aa=True
					#Input inital guess here
					while aa == True:
						guess = input("Enter your guess #"+str(n+1)+" here: ").lower()
						iguess=guess
						if guess == "":
							aa = True
						elif guess == "01001101":
							aa = False
						elif guess in guessRep:
							spacing()
							guess+=" (incorrect)"
							guessLists1()
							print()
							print("MESSAGE: You have already guessed: "+iguess+"!")
							print()
						elif dicCheck.check(guess):
							aa = False
						else:
							spacing()
							guess+=" (incorrect)"
							guessLists1()
							print()
							print("MESSAGE: Word not found in dictionary!")
							print()
					if guess == "100101101":
						if guesses == "Previous Guesses: ":
							spacing()
							guessLists1()
							print()
							print("No previous guesses!")
							print()
						else:
							spacing()
							guessLists1()
							print()
							print(guesses)
							print()
					else:
						d=False
				gcheck = [char for char in guess]
				for j in gcheck:
					if j not in letList or j == "":
						f+=1
				if f > 0:
					spacing()
					if n == 0:
						guessLists()
					else:
						guessLists1()
					print()
					print("MESSAGE: Please don't include numbers, symbols, or spaces in your guess!")
					xm+=1
					print()
					b = True
				else:
					b = False
			z=True
			while z==True:
				if len(guess) == int(wordLen): #checks word for length error
					z=False
				else:
					spacing()
					guess+=" (incorrect)"
					print()
					if n == 0:
						guessLists()
					else:
						guessLists1()
					print()
					print("MESSAGE: Please enter a word "+str(wordLen)+" letters long!")
					bp+=1
					print()
					k = True
					while k == True: #checks word for non-alphebet chars
						f=0
						d=True
						while d == True:
							#Input guess here
							aa = True
							while aa == True:
								guess = input("Enter your guess #"+str(n+1)+" here: ").lower()
								iguess=guess
								if guess == "":
									aa = True
								elif guess == "100101101":
									aa = False
								elif guess in guessRep:
									spacing()
									guess+=" (incorrect)"
									guessLists1()
									print()
									print("MESSAGE: You have already guessed: "+iguess+"!")
									print()
								elif dicCheck.check(guess):
									aa = False
								else:
									spacing()
									guess+=" (incorrect)"
									guessLists1()
									print()
									print("MESSAGE: Word not found in dictionary!")
									print()
							if guess == "100100011":
								if guesses == "Previous Guesses: ":
									spacing()
									guessLists1()
									print()
									if bp > 0:
										print("MESSAGE: Please enter a word "+str(wordLen)+" letters long!")
									if xm > 0:
										print("MESSAGE: Please don't include numbers, symbols, or spaces in your guess!")
									print()
									print("No previous guesses!")
									print()
								else:
									spacing()
									guessLists1()
									print()
									print(guesses)
									print()
							else:
								d=False
						gcheck = [char for char in guess]
						for j in gcheck:
							if j not in letList or j == "":
								f+=1
						if f > 0:
							guess+=" (incorrect)"
							spacing()
							if n == 0:
								guessLists()
							else:
								guessLists1()
							print()
							print("MESSAGE: Please don't include numbers, symbols, or spaces in your guess!")
							print()
							k = True
						else:
							k = False
					z=True
			guessLetList=[char for char in guess]
			guesses+=str(guess)+" " #adds guess to previous guesses str (visible)
			guessRep.append(str(guess)) #adds guess to previous guess list (hidden)
			bp=0
			xm=0
			if n==0:
				guess1 = "("+guess+")"
				ccL = c1
			elif n==1:
				guess2 = "("+guess+")"
				ccL = c2
			elif n==2:
				guess3 = "("+guess+")"
				ccL = c3
			elif n==3:
				guess4 = "("+guess+")"
				ccL = c4
			elif n==4:
				guess5 = "("+guess+")"
				ccL = c5
			elif n==5:
				guess6 = "("+guess+")"
				ccL = c6
			#list filler mechanism
			c=0
			ccL.clear() #clears the list of blanks (-)
			for i in guessLetList:
				if i == wordLetList[c]: #cond1 (Correct & Place)
					ccL.append(i.upper())
					if i not in correctWp: #appends to correct word/place list
						correctWp+=i+" "
				elif i != wordLetList[c] and i in wordLetList: #cond2 (Correct)
					ccL.append(i.lower())
					if i not in correctWtP: #appends to correct word list
						correctWtP+=i+" "
				else: #cond3 (Incorrect)
					ccL.append("-")
					if i not in incorrect: #appends to incorrect word list
						incorrect+=i+" "
				c+=1
			oh=0
			for j in ccL: #Checks for all caps (win) in row
				if j.isupper():
					oh+=1
			if n == 0:
				c1 = ccL
			elif n == 1:
				c2 = ccL
			elif n == 2:
				c3 = ccL
			elif n == 3:
				c4 = ccL
			elif n == 4:
				c5 = ccL
			elif n == 5:
				c6 = ccL
			if oh == wordLen:
				spacing()
				guessLists()
				won = True
				print()
				print("Congrats, you found the word: "+word.upper()+"!")
				print()
				rr=True
				while rr == True:
					eostat=input("Press (enter) to play again, or (q) to quit: ").lower()
					if eostat == "q":
						sys.exit()
					elif eostat == "":
						spacing()
						rr = False
				break
			spacing()
			#Letter repeat checker mechinism
			splG=str(word)
			splitWordList = list(set(splG)) #splits word into unique str characters
			if n == 0:
				ccL = c1
			elif n == 1:
				ccL = c2
			elif n == 2:
				ccL = c3
			elif n == 3:
				ccL = c4
			elif n == 4:
				ccL = c5
			elif n == 5:
				ccL = c6
			for i in splitWordList: #loop through every letter
				wordCount = word.count(i) #counts the frequency of letters
				guessLowCount = ccL.count(i)
				guessUppCount = ccL.count(i.upper())
				guessCount = guessLowCount + guessUppCount
				uppCount = 0 #frequency number of uppercase
				if guessCount > wordCount: #checks to see if too many letters in list
					for j in ccL:
						if j == i.upper(): #checks to see if the word is upper (skips over)
							uppCount += 1
					lowerDel = int(guessCount) - int(wordCount) #final number of lowercase to delete from list
					zz = 0
					fl = 0 #number of lowercase deleted
					for j in ccL:			
						if j.lower() == i.lower():
							if j.islower():#checks to see if lowercase
								del ccL[zz]
								ccL.insert(zz,"-") #deletes and replaces extra lowercase with "-" (blank)
								fl += 1
							if fl == lowerDel: #once the number is met, loop is broken and game continues
								break
						zz+=1
			if n == 0:
				c1 = ccL
			elif n == 1:
				c2 = ccL
			elif n == 2:
				c3 = ccL
			elif n == 3:
				c4 = ccL
			elif n == 4:
				c5 = ccL
			elif n == 5:
				c6 = ccL
		if n == 5:
			break
	spacing()
	guessLists()
	if won != True:
		print()
		print("Sorry, you lost! The word was:",word.upper())
		print()
		rr=True
		while rr == True:
			eostat=input("Press (enter) to play again, or (q) to quit: ").lower()
			if eostat == "q":
				sys.exit()
			elif eostat == "":
				rr = False
				spacing()
		ttt=0
