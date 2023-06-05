fh = open('mbox-short.txt')

for line in fh:
    sline = line.rstrip()
    print(sline.upper())
