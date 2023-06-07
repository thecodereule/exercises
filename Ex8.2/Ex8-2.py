fname = input("Enter file name: ")
fileHandler = open(fname)
lst = list()
for line in fileHandler:
    line = line.rstrip()
    words = line.split()
    for i in range(len(words)):
        if words[i] not in lst:
            lst.append(words[i])
        else:
            continue

lst.sort()
print(lst)

'''output
['Arise', 'But', 'It', 'Juliet', 'Who', 'already', 'and', 'breaks', 'east', 'envious', 'fair', 'grief', 'is', 'kill', 'light', 'moon', 'pale', 'sick', 'soft', 'sun', 'the', 'through', 'what', 'window', 'with', 'yonder']
'''
