"""
3)Create a python function that give the factorial of a user entered number
"""

def factorial(a):
	for x in range(1,a):
		a *= x
	return a

