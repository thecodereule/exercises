# 5.2 Write a program that repeatedly prompts a user for integer numbers until the user enters 'done'. Once 'done' is entered, print out the largest and smallest of the numbers. If the user enters anything other than a valid number catch it with a try/except and put out an appropriate message and ignore the number. Enter 7, 2, bob, 10, and 4 and match the output below.


max = 0
min = 0
first_iteration = True
while True:
    num = input("Enter a number: ")
    if num == "done":
        break
    try:
        num = int(num)
    except:
        print("Invalid input")
        continue
    if first_iteration:
        max = num
        min = num
        first_iteration = False
    else:
        if num>max:
            max=num
        elif num<min:
            min=num    
    
print("Maximum is",max)
print("Minimum is",min)
