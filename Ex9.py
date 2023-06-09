fname = input('Enter File Name: ')
if len(fname) < 1:
    fname = 'clown.txt'

hand = open(fname)
di = {}
for line in hand:
    line = line.rstrip()
    words = line.split()
    print(words)
    print("***BREAK LINE***")
    for word in words:
        di[word] = di.get(word, 0) + 1

print(di.items())
bigcount = None
bigword = None
for key,value in di.items():
    if bigcount is None or value > bigcount:
        bigcount = value
        bigword = key

print(f'Done "{bigword}" count is {bigcount}')

