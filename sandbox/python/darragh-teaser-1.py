"""
1)Using a python loop create this print out :
*
**
***
****
*****
******
*****
****
***
**
*
"""

for x in range(1,12):
	print '*' * abs(abs(x-6)-6)
