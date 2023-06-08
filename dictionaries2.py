counts = dict()
names = ['csev', 'cwen', 'csev', 'zqian', 'cwen']

for name in names:
    counts[name] = counts.get(name, 0) + 1
print(counts)

'''output:
{'csev': 2, 'cwen': 2, 'zqian': 1}
'''
