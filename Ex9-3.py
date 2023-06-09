name = input('Enter a file: ')
handler = open(name)

counts = {}
for line in handler:
    words = line.split()
    for word in words:
        counts[word] = counts.get(word,0) + 1

bigcount = None
bigword = None
for word,count in counts.items():
    if bigcount is None or count > bigcount:
        bigword = word
        bigcount = count

print(f'Word with the highest Value is : "{bigword}" and the total Count is : {bigcount}')
