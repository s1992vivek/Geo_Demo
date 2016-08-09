'''
This script gives the nearest Levenshtein distance address of the input address
to adresses in the provided dataset using fuzzy search

This file requires installation of fuzzywuzzy python library
Command: sudo pip install fuzzywuzzy

'''

str1=[]
#importing the address data as a list
with open('data.txt') as inputfile:
    for line in inputfile:
        str1.append(line.strip().split(','))

print len(str1)
import re
from fuzzywuzzy import fuzz
from fuzzywuzzy import process
# importing fuzzywuzzy function

givenloc= raw_input("Please enter new address with delimiter comma and state name at the end: ")
givenloc=givenloc.strip().split(',')

'''
token.txt has all the addresses from data that do not have last word as a state name or not seperated by a comma 
'''

L={}
with open("token.txt", "w") as text_file:
	for name in str1:
		#appending tokens in token.txt with last name not as state
		file = open('states.txt', 'r')
		if name[-1] not in file.read():
			name =(', ').join(name)
			text_file.write(name+'\n')
			name=name.strip().split(',')

		#calculating fuzzy ratio with last name as state
		if givenloc[-1].strip() == name[-1].strip():
			givenloc=(', ').join(givenloc)
			L[(', ').join(name)] = fuzz.token_sort_ratio(name, givenloc)
			givenloc=givenloc.strip().split(',')



with open("token.txt", "r") as text_file:
	for i in text_file:
		toke=i.split()
		#calculating fuzzy ratio if last name is a state but in token list		
		if givenloc[-1].strip() == toke[-1].strip():
			givenloc=(', ').join(givenloc)
			L[(', ').join(toke)] = fuzz.token_sort_ratio(toke, givenloc)
			givenloc=givenloc.strip().split(',')
		
		#calculating fuzzy ratio if for cases where last word was a city in the address data	
		if givenloc[-2].strip() == toke[-1].strip():
			givenloc=(', ').join(givenloc)
			L[(', ').join(toke)] = fuzz.token_sort_ratio(toke, givenloc)
			givenloc=givenloc.strip().split(',')
			
#sorting the fuzzy ratios to give the key with maximum value, L is a dictionary
if L!={}:
	M=sorted(L.values())
	y= M[-1]
	print y
	for x in L.items():
		if x[1] == y:
			print x[0]
else:
	print 'no match in data'




