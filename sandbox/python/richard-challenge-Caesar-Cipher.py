with open('cipher.txt') as f:
    content = f.readlines()

result = ''
dic = {}

print "Input:"
print content
print

for item in range(0,len(content[0])):
	if content[0][item] in dic.keys():
		dic[content[0][item]] += 1
	else:
		dic[content[0][item]] = 1

# ranking
print dic

# most used symbol
counter = 0
most_used = ''
for item in dic:
	if dic[item] > counter:
		counter = dic[item]
		most_used = item

print "Most user symbol:",most_used

# In this case is the Space
shift = ord(most_used)-ord(' ')

for item in range(0,len(content[0])):
	result += unichr(ord(content[0][item])-shift)

print "Result:"
print result
