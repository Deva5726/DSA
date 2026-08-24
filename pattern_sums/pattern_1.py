# Input:
# n= 6
# ******
# *****
# ****
# ***
# **
# *
print("input:")
n=int(input("n = "))
print("output:")
for i in range(1,n+1):
    star=n-i+1
    print("*"*star)