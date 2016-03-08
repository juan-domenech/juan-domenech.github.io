# Given a file contains 1 million 7 digit numbers
# What's the fastest way to find out how many unique numbers the file contains
# Note: Fastest = dev time + run time

def unique_numbers(file):
	dataset = set()
	with open(file) as f :
		for number in f :
			dataset.add(number.strip())

	return len(dataset)

print "Total unique numbers",unique_numbers('file-with-numbers.txt')
