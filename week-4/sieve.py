# Given a range [L, R]. The task is to find the sum of all the prime numbers in the given range from L to R both inclusive.
# Examples:  
# Input : L = 10, R = 20
# Output : Sum = 60
# Prime numbers between [10, 20] are:
# 11, 13, 17, 19
# Therefore, sum = 11 + 13 + 17 + 19 = 60
# Input : L = 15, R = 25
# Output : Sum = 59
# Note: Use sieve of eratosthenes to solve the problem
def sieve(L,R):
    if R<2:
        return 0
    is_prime=[True]*(R+1)
    is_prime[0]=is_prime[1]=False
    p=2
    while (p*p)<=R:
        if is_prime[p]:
            for i in range(p*p,R+1,p):
                is_prime[i]=False
        p+=1
    prime_sum=0
    for i in range(max(2,L),R+1):
        if is_prime[i]:
            prime_sum+=i
    return prime_sum
print(sieve(10,20))
print(sieve(15,25))
