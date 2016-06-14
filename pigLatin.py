#List of vowels and Punctuations
VOWELS = ['a', 'e', 'i', 'o', 'u','A','E','I','O','U']
PUNC = [',',':',';','\'','\"','(',')','[',']','?','!','.']
result = list()

def mainFunc():
	global result
#Taking input from the user and splitting them based on space
	inpSent = raw_input("Type the sentence:\n")
	word = inpSent.split(' ')
#Loping through each word
	for w in word:
		hyphenWords = w.split("-")
		hyplen = len(hyphenWords)
#check if there is a word spearated by hyphen
		if hyplen > 1:
			output = ''
			for i in range(hyplen):
				prcsd_word = processWord(hyphenWords[i])
				output += prcsd_word
				if i == hyplen-1:
					continue
				output += '-'
			result.append(output)
		else:
			result.append(processWord(w))	
	display()	

def processWord(w):
#Two lists : one each for maintaining indexes of punctuations and capital letters
	indexList = list()
	puncIndex = dict()

	if len(w) > 1:
		if w[len(w)-3:len(w)] is "way":
			return w
#converting the string into a list
		wd = list(w)
		for l_i,letter in enumerate(wd):
			if letter.isupper():
				indexList.append(l_i)
			if letter in PUNC:
				puncIndex[len(wd)-l_i-1]=letter

		wd_str = "".join(wd)
		wd_str_new = ""
		for s in wd_str:
			if s in PUNC:
				continue
			wd_str_new += s

		wd = list(wd_str_new)
#checking conditions for piglatin conversion
		if wd[0] in VOWELS:
			wd.append('w')
			wd.append('a')
			wd.append('y')
			return formatWord(wd,indexList,puncIndex)
		else:
			first = wd[0]
			wd.remove(wd[0])
			wd.append(first)
			wd.append('a')
			wd.append('y')
			return formatWord(wd,indexList,puncIndex)
	else:
		return w

def formatWord(myList,indexList,puncIndex):
	for i,letter in enumerate(myList):
		myList[i] = myList[i].lower()
		for x in indexList:
			myList[x] = myList[x].upper()

	myWord = "".join(myList).strip()

#Iterating through the dictionary of punctuation index
	for k,v in puncIndex.items():
		myWord = myWord[:len(myWord)-k] + v + myWord[len(myWord)-k:]
	return myWord

#displaying the results
def display():
	print '\n'
	for words in result:
		print words,
	print '\n'
mainFunc()
