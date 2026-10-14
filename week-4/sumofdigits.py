# Write a recursive algorithm to find the count of digits in a number.

# Example:
# Input: 353445

# Outpput: 6
def countdigits(n):
    if n==0:
        return 0
    else:
        return 1+countdigits(n//10)
print(countdigits(353445))