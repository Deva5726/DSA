# Write a program to get firstName and lastName and n as input and print fullName that is firstName+lastName for n times.
# Input
# Deva
# dny
# 5
# Expected output:
# Devadny
# Devadny
# Devadny
# Devadny
# Devadny

def nameprint(firstname,lastname,num):
    i=1
    while(i<=num):
        print(firstname+lastname)
        i+=1
nameprint(
    firstname=input(),
    lastname=input(),
    num=int(input())
    )
