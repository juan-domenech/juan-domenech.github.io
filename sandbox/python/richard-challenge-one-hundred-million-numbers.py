# Give a file that contains 100 millions 7 digit numbers find a number that is not in the file

from random import randint

def find_not_present_number(file):
	with open(file) as f :
		while True:
			guess = randint(1000000,9999999)
			for number in f :
				if number.strip() != guess :
					print "Number found!", guess, "is not in the list."
					return guess


print find_not_present_number('one-hundred-million-numbers.txt')
