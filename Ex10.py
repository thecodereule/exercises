fhand = input('Enter the name of a File: ')
if len(fhand) < 1:
    fhand = 'clown.txt'
hand = open(fhand)

counts = {}
for line in hand:
    line = line.rstrip()
    words = line.split()
    for word in words:
        counts[word] = counts.get(word,1)+1

lst = []
for k,v in counts.items():
    lst.append((v,k))

lst = sorted(lst, reverse=True)
# print(lst)

for v,k in lst[:10]:
    print(k,v)