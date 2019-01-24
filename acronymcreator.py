"""
POSSIBLE FORMATS:
CC	coordinating conjunction
CD	cardinal digit
DT	determiner
EX	existential there (like: "there is" ... think of it like "there exists")
FW	foreign word
IN	preposition/subordinating conjunction
JJ	adjective	'big'
JJR	adjective, comparative	'bigger'
JJS	adjective, superlative	'biggest'
LS	list marker	1)
MD	modal	could, will
NN	noun, singular 'desk'
NNS	noun plural	'desks'
NNP	proper noun, singular	'Harrison'
NNPS	proper noun, plural	'Americans'
PDT	predeterminer	'all the kids'
POS	possessive ending	parent's
PRP	personal pronoun	I, he, she
PRP$	possessive pronoun	my, his, hers
RB	adverb	very, silently,
RBR	adverb, comparative	better
RBS	adverb, superlative	best
RP	particle	give up
TO	to	go 'to' the store.
UH	interjection	errrrrrrrm
VB	verb, base form	take
VBD	verb, past tense	took
VBG	verb, gerund/present participle	taking
VBN	verb, past participle	taken
VBP	verb, sing. present, non-3d	take
VBZ	verb, 3rd person sing. present	takes
WDT	wh-determiner	which
WP	wh-pronoun	who, what
WP$	possessive wh-pronoun	whose
WRB	wh-abverb	where, when


0 - Noun
1 - Verb
2 - Adjective
3 - Adverb
4 - Preposition
5 - Article

numbertotag format : {number : "tag"}

Hydrogen
Lithium
Sodium
Potasium
Rubidium
Caesium
Francium

"""

import nltk
import random
import sys

sample_data = ["Hydrogen", "Lithium", "Sodium", "Potasium", "Rubidium", "Caesium", "Francium"]

struct = (5, 2, 0, 1, 4, 5, 0)

numbertotag = {0 : "NN", 1 : "VB", 2 : "JJ",3 : "RB",4 : "TO", 5 : "DT", 6 : "NNP"}

dictionary = "wordlist.txt"

def acronym_create(parsedwordlist):
	acronym = ""
	for word in parsedwordlist:
		acronym += word[0].upper()
	return acronym



def creator():

	acronym = acronym_create(sample_data)
	acrwords = ""

	print (acronym)

	wordlist = nltk.corpus.brown.tagged_words()
	#wordlist = nltk.word_tokenize(list)
	#wordlist = nltk.pos_tag(tokenized)


	print("Loaded Word List...")

	for x in range(len(sample_data)):
		temp = False
		print("INDEX: " + str(x))
		print(numbertotag[struct[x]])
		for word in wordlist:
			if word[1] == numbertotag[struct[x]] and word[0][0] == acronym[x]:
				print (word[1])
				acrwords += word[0] + " "
				break


	print (acrwords)

def wordfinder(pos):
	wordlist = nltk.corpus.brown.tagged_words()

	for word in wordlist:
		#print (word[1] + " " + pos)
		if word[1] == pos:
			print (word[0])	
			pass



wordfinder(numbertotag[struct[1]])
#creator()



