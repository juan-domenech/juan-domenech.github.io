"""
2)Create a python function that prints all the even numbers from a range of numbers i.e 0-100
"""

def evenNumbers (a,b):
	for x in range(a,b+1):
		if not x % 2:
			print "Number:",x,"is even!"
