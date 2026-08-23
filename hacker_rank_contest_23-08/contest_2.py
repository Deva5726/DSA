# Write a program to print N numbers starting from 2. Take N as input and print from 2 to N;

# Input Format

# 6

# Constraints

# 3<=N<=10^3

# Output Format

# 2 3 4 5 6
data=int(input())
for i in range(2,data+1):
    print(i,end=' ')