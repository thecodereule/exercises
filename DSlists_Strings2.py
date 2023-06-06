line = 'A lot           of spaces'
etc = line.split()
print(etc)
'''['A', 'lot', 'of', 'spaces']'''

line = 'first;second;third'
thing = line.split()
'''['first;second;third']'''

print(len(thing))
'''1'''

thing = line.split(';')
print(thing)
'''['first','second','third']'''
print(len(thing))
'''3'''

# When you do not specify a delimiter, multiple spaces are treated like one delimiter
# You can specify what delimiter characters to use in the splitting method

