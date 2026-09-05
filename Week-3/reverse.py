# Input : 

# 325345

# Expected output:

# 543523
n=int(input())

while(n>0):
    ld=n%10
    n=n//10
    print(ld,end="")
