# Input: 5 2

# Output: 25

# # Explanation: 5^2 is 25
def pow_array(a,n):  #(base , power)
    if n==0:
        return 1
    else:
        return a*pow_array(a,n-1)
print(pow_array(5,2))
"\n"
print(pow_array(2,3))