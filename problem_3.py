# Prob 3: 
# Given mark of student, Print the Grade
# Grade A if mark is greater than or equal to 90
# Grade B if mark is greater than or equal to 80
# Grade C if mark if greater than or equal to 60
# Grade D if mark if greaer than or equal to 35
# Fail if mark is lesser than 35
# Input: 95
# Expected Output:
# Grade A
# Explanation: Here 95 is greater than or equal to 90 so its Grade A
mark= int(input())
if (mark>=0):
    if (mark>=90):
        print("Grade A")
    elif (mark>=80):
        print("Grade B")
    elif (mark>=60):
        print("Grade C")
    elif (mark>=35):
        print("Grade D")
    else:
        print("Fail")
else:
    print("Invalid Input")