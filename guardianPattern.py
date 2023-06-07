hand = open('mbox-short.txt')

for line in hand:
    line = line.rstrip()
    wrds = line.split()
    # guardian in a compound statement
    if len(wds) < 3 or wds[0] != 'From':
        continue
    print(wds[2])
