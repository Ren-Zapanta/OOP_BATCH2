#Prog02: Create a program that ask user to input 2 numbers. Print "Not Equal" when the numbers are not the same.
num_1 = int(input("Please enter a number: "))
num_2 = int(input("Please enter another: "))

if num_1 == num_2:
    print("Numbers are equal")
else:
    print("Not equal")