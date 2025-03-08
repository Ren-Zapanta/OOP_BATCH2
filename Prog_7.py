#Prog07: Create a program that ask user to input 10 numbers. Print how many are even numbers.

numbers = []

for i in range(10):
    num = int(input(f"Please input a number {i + 1}: "))
    numbers.append(num)

evens = 0

for num in numbers:
    if num % 2 == 0:
        evens += 1

print(evens)