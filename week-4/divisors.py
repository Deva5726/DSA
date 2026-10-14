# Write a program to print the divisors of a number recursively.

# Example:
# Input: 6
# Output: 1 2 3 6
def div_array(n, i=1):
    if i>n:
        return 
    if n%i==0:
        print(i ,end=" ")
    div_array(n, i+1)
n=6
div_array(n)
    
