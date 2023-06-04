'''5.1 Write a program which repeatedly reads numbers until the user enters 
done”. Once “done” is entered, print out the total, count, and average of 
the numbers. If the user enters anything other than a number, detect their 
mistake using try and except and 
print an error message and skip to the next number.
'''

list = []
sum = 0
count = 0
average = 0
while True:
    inp = input("Enter a number: ")
    if inp == "done":
        print(sum, count, average)
        break
    
    try:
        inp = float(inp)
        count = count + 1
        sum = sum + inp
        average = sum/count

    except:
        print("Invalid Input")
        continue
    
