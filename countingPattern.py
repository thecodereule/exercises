counts = {}
line = input('Enter a line of text: ')
words = line.split()

print('Words:', words)
for word in words:
    counts[word] = counts.get(word, 0) + 1
print('Counts', counts)
