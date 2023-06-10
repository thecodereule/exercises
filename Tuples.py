fhand = open('romeo.txt')
counts = dict()

for line in fhand:
    words = line.split()
    for word in words:
        counts[word] = counts.get(word, 0) + 1

# print(counts.items())
tmp = list()
for k,v in counts.items():
    tmp.append( (v,k) )

tmp = sorted(tmp, reverse = True)
print(tmp)
