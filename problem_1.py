# Prob 1 : Write a program that takes an integer, then a string, then a char from the user and prints them in the screen.
# Input:  2 Name y
# Expected Output:
# 2
# Name
# y

data=input().split()

num = int(data[0])
text=data[1]
char=data[2][0]

print (num)
print (text)
print (char)