# otvoriti romeo.txt file
fhand = open('romeo.txt')

# ucitati sve rijeci u dict i prikazati koliko puta se rijec ponavlja
counts = dict()

for line in fhand:
    words = line.split()
    # varijabla words je objekt list sastavljen od stringova iz te linije
    for word in words:
        counts[word] = counts.get(word, 1) + 1

# da bi vrijednosti u dictionary sortirali, moramo od njega napraviti listu

print ( sorted( [ (v,k) for k,v in counts.items() ] ) )
'''
[(1, 'b'), (10,'b'), (22, 'c')]
'''
