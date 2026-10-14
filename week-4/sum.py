# Write a recursive program to find the sum of digits of a number.
# Input: 34534

# Ouput: 19
def sum(n):
    if n==0:
        return 0
    return n%10 + sum(n//10)
print(sum(34534))
