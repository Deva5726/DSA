# Write a program which takes the following input and prints them one by one. 
# 1. An whole number
# 2. A letter 
# 3. A number with fractional part 
# 4. A word
# Sample Input 0

# 34
# S
# 56.7
# Str
# Sample Output 0

# 34
# S
# 56.7
# Str
text=input()
y=text.isdigit()
if y==True:
    print(text)
letter=input()
print(letter)
frac=float(input())
print(frac)
word=input()
print(word)   