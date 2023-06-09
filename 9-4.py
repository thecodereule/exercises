'''
9.4 Write a program to read through the mbox-short.txt and figure out who has sent the greatest number of mail messages. The program looks for 'From ' lines and takes the second word of those lines as the person who sent the mail. The program creates a Python dictionary that maps the sender's mail address to a count of the number of times they appear in the file. After the dictionary is produced, the program reads through the dictionary using a maximum loop to find the most prolific committer.
'''
# Note: using len(words) < 1 as a condition would cause the computer to read lines that have only one word, and unintentionally causing an indexError when accesing words[1]

fhandle = open('mbox-short.txt')

email_count = {}

for line in fhandle:
    line = line.rstrip()
    words = line.split()
    # Consider only the lines starting with 'From '
    if len(words) < 2 or words[0] != 'From':
        continue
    email = words[1]
    # Increment the count for this email
    email_count[email] = email_count.get(email, 0) + 1

bigcount = None
bigemail = None
for k,v in email_count.items():
    if bigcount is None or bigcount < v:
        bigcount = v
        bigemail = k

print(bigemail, bigcount)
