# Given a list of integers or strings, remove all duplicates.
# The list might be unsorted and with one or none elements.
# Example:
# [5,1,2,3,4,5] = [1,2,3,4,5]
# ['aaa','aaa','aab'] = ['aaa','aab']
# [1] = [1]
# [] = []

def remove_duplicates(work):
	work = sorted(work)
	return [ work[item] for item in xrange(0,len(work)) if work[item:item+1] != work[item+1:item+2] ]