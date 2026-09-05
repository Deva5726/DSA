# Input : 

# 11

# Expected output:

# 2 3 5 7 11
def prime(n):
    prime=[]
    for num in range(2,n+1):#(iterates through 2,n)
        is_prime=True
        for i in range(2,int(num**0.5)+1): #(here we checking is there divisors available for num upto sqrt(num))
            if num%i==0:
                is_prime=False
                break
        if is_prime:
            prime.append(num)
    print(*prime)
n=int(input())
prime(n)


