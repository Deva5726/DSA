# swapping of variables
#a=2, b=3

def swapping(a, b):
    temp = a
    a = b
    b=temp # b receives original a
    return a, b    # Return the swapped values

a = int(input("a: "))
b = int(input("b: "))

# Assign returned values back to a and b
a, b = swapping(a, b)

print("a:", a)
print("b:", b)
    



