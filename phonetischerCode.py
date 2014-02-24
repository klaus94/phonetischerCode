#!/ usr/binenv python
# -*- coding : utf -8 -*-

import os
from test_array import *

#this program consists of two main parts: the decoding (simple) and the encoding (hard) part
#Phonetischer Code:
#this method can combine numbers and words. vocals can diversify. Consonants stant for a specific 
#number:
#0 ... s, z
#1 ... d, t
#2 ... n
#3 ... m
#4 ... r									#TODO: encode with database(.txt)!!!
#5 ... l
#6 ... j, ch, sch
#7 ... g, k
#8 ... f, v
#9 ... b, p

#Dictionarray: extra code for "ch" and "sch" !!!
code = {"s":"0", "z":"0", "d":"1", "t":"1", "n":"2", "m":"3", "r":"4", "l":"5", "j":"6", "g":"7", "k":"7", "f":"8", "v":"8", "b":"9", "p":"9", "c":""}		#c--> identification in if-request, value not important

def find_number(word):
	solution = ""
	word = word.lower()
	zaehler = 0
	while (zaehler < len(word)):
		add = 1				#counts how many positions zaehler has to continue (ch, sch)
		is_special = False
		if (word[zaehler] in code):			# = if word[i] is a consonant
			try:							#sch
				if (word[zaehler] == "s") and (word[zaehler+1] == "c") and (word[zaehler+2] == "h"):
					solution += "6"
					add += 2
					is_special = True
				elif (word[zaehler] == "c") and (word[zaehler+1] == "h"):	#ch
					solution += "6"
					add += 1
					is_special = True
			except:
				print "FATALER FEHLER!!! ;)"
				
			if (not is_special):				#not in special case like "sch" or "ch"
				solution += code[word[zaehler]]		#general for all the other consonants
		zaehler += add							#also +1 if vocal --> next position
	return solution


def find_words(zahl):
	data_num = open("zahlenListe.txt","r")
	data_words = open("data.txt","r")
	numbers = str(data_num.read())
	numbers = numbers.split("\n")
	words = str(data_words.read())
	words = words.split("\n")
	results = []
	for i in range(len(numbers)):
		if (numbers[i] == zahl):
			results.append(words[i].split("/")[0].replace("\xf6","oe").replace("\xe4","ae").replace("\xfc","ue").replace("\xdf","s"))
	data_num.close()
	data_words.close()
	return results

def main():
	ant = "y"
	while (ant == "y"):
		os.system("clear")
		print "This program can handle the phonetic code"
		print "PRESS '1' to convert a number into a word"
		print "PRESS '2' to convert a word into a number"
		print "PRESS 'i' to get some information about the program"
		print "PRESS 'l' to get a list for better understanding"
		choice = raw_input("What do you want to do? ")
		if (choice == "1"):	#number --> word
			number = raw_input("enter a number: ")
			allPossible = teile(number)					#allPossible enthaelt alle Kombinationen der zahl z.B.: 123--> 123; 1,23; 12,3; 1,2,3
			for i in allPossible:						#fuer jede kombination wird nach moeglichen worten gesucht
				newWord = i.split(",")
				for part in newWord:					#
					print part + " " + str(find_words(part)) + "\n"
				print "--------------------------------------------------" + "\n"	#new section
				
				
		elif (choice == "2"):	#word --> number
			word = raw_input("enter a word: ")
			print "your code is: " + find_number(word)
		elif (choice == "i"):
			os.system("clear")
			print "the phonetic code"
			print "with the help of this code you can convert numbers into words. so you will keep them better in mind."
			print "the system goes like this: every number from 0 to 9 stands for a group of consonants, thats sound quite similar (behold the list). To get a comlete word we fill in some vowels between the consonants."
			print ""
			print "e.g. the number '02' could be the word: 'sun', because 0 is 's' and 2 is 'n'." 
		elif (choice == "l"):
			print "List, that says, which number belongs to which consonant and a memory hook to each:"
			print "0.. 'ZZZero' ........................ s,z" 
			print "1.. 'vertigal line' ................. d,t"
			print "2.. 'two feets' ..................... n" 
			print "3.. 'three feets' ................... m"
			print "4.. 'fouRRR' ........................ r" 
			print "5.. '...' ........................... l" 
			print "6.. 'six letters with same sound' ... j,ch,sch"
			print "7.. 'two 7 looks like a k' .......... g,k"
			print "8.. 'V-8 motor' ..................... f,v"
			print "9.. '9 looks like a b upside down' .. b,p"
		else:
			print "you made a wrong input. enter either '1' or '2' !!!" 
		print ""	#for better appearance
		
		ant = raw_input("continue? (y/n) ")

if __name__ = "__main__":
	main()
