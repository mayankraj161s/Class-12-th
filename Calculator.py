# Write a program to calculate and store the input and output in a text file
from datetime import datetime
file = open("output.txt", "a")
count = 0
while True:
    def add(a, b):
        global count
        count += 1
        return a+b
    def difference(a, b):
        global count
        count += 1
        return a-b
    def product(a, b):
        global count
        count += 1
        return a*b
    def quotient(a, b):
        global count
        count += 1
        return a/b
    
    print("Calculator : Used for 2 numbers")
    print("Menu:-")
    print("1) Addition")
    print("2) Difference")
    print("3) Product")
    print("4) Quotient")
    ch = int(input("Enter your Choice:(1-4) "))
    if ch in [1,2,3,4]:
        x = int(input("Enter first number: "))
        y = int(input("Enter second number: "))
    if ch == 1:
        sum = add(x, y)
        print("The Sum of {} and {}".format(x, y), "is", sum)
        file.write("The Sum of {} and {}".format(x, y))
        file.write(" is ")
        file.write(str(sum))
        file.write("\n\n")
    elif ch == 2:
        diff = difference(x, y)
        print("The Differnce of {} and {}".format(x, y), "is", diff)
        file.write("The Difference of {} and {}".format(x, y))
        file.write(" is ")
        file.write(str(diff))
        file.write("\n\n")
    elif ch == 3:
        pro = product(x, y)
        print("The Product of {} and {}".format(x, y), "is", pro)
        file.write("The Product of {} and {}".format(x, y))
        file.write(" is ")
        file.write(str(pro))
        file.write("\n\n")
    elif ch == 4:
        quot = quotient(x, y)
        print("The Quotient of {} and {}".format(x, y), "is", quot)
        file.write("The Quotient of {} and {}".format(x, y))
        file.write(" is ")
        file.write(str(quot))
        file.write("\n\n")
    else:
        print("You entered wrong input.")
        print("Try again")
        break

print("Total operation performed: ", count)
file.write("Total operation performed: ")
file.write(str(count))
file.write("\n\nOperations perfomed on: ")
now = datetime.now() # Storing current date and time
dt_string = now.strftime("%d/%m/%Y %H:%M:%S\n")
file.write(str(dt_string))
file.write("-"*50)
file.write("\n\n")
file.close()
