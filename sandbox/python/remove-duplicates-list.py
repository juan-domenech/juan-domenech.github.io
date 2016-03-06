# Given a list of integers or strings,remove all duplicates
# The list might be unsorted and with one or none elements
# Example:
# [5,1,2,3,4,5] = [1,2,3,4,5]
# ['aaa','aaa','aab'] = ['aaa','aab']
# [1] = [1]
# [] = []

def remove_duplicates(todo):
	todo = sorted(todo)
	return [ todo[item] for item in range(0,len(todo)) if todo[item:item+1] != todo[item+1:item+2] ]