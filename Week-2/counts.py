# Write a program that gets n as input and print the number of digits in the number

# Testcase 1 :

# Input : 

# 325345

# Expected output:

# 6
n=int(input())
count=0
while(n>0):
    tem=n%10
    n=n//10
    count+=1
print(count)