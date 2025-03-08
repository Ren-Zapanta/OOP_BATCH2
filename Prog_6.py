#Prog06: Create a program that ask user to input 10 numbers. Print the result of the first number minus all of the remaining numbers.
numbers = []
for i in range(10):
    num = int(input(f"Please enter a number {i + 1}: "))
    numbers.append(num)

f_num = numbers[0]

result = f_num

for i in range(1, 10):
    result -= numbers[i]

print(result)

