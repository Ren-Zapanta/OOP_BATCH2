#Prog10: Create a program that ask user to input 2 numbers. Print all the numbers between the two numbers.
num_1 = int(input("Please enter a number: "))
num_2 = int(input("Please enter a number: "))

SMALL = min(num_1, num_2)
LARGE = max(num_1, num_2)

for i in range(SMALL + 1, LARGE):
    print(
