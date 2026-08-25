# Sample 1:
# Input:
# n = 8
# Expected output:
# 1 

# 2 2 

# 3 3 3 

# 4 4 4 4 

# 5 5 5 5 5 

# 6 6 6 6 6 6 

# 7 7 7 7 7 7 7 

# 8 8 8 8 8 8 8 8 
print("input:")
n=int(input("n= "))
print("output: ")
print(" ")
for i in range(1,n+1):
    for j in range(1,i+1):
        print(i,end=" ")
    print(" ")