import sys

num = input('How many number? ')
num = int(num)
total_sum = 0

for n in range(num):
    numbers = float(input("Enter any number "))
    total_sum  = total_sum + numbers


avg = total_sum / num
print("The average is {0}".format(avg))








