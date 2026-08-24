# Input:
# n= 6
# output:
# 654321
# 54321
# 4321
# 321
# 21
# 1
print("Input:")
n=int(input("n = "))
print("   ")
print("Output:")
for i in range(1,n+1):
    # range(start, stop, step) , (-1)-->reverse order
    for j in range(n-i+1,0,-1):
        print(j,end="")
    print(" ")