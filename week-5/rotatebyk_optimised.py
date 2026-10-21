# input = [3,4,5,1,2]
# output = 3
# find out the step of rotation of array.
def rotationbyk(arr):
    low=0
    high=len(arr)-1
    ans=0
    while low<=high:
        mid= int((low + high)/2)
        i=(mid-1+len(arr)) % len(arr)
        j=(mid+1) % len(arr)

        if arr[mid]<arr[i] and arr[mid]<arr[j]:
            return mid
        if arr[j]>arr[mid]:
            high=mid-1
        else:
            ans = mid
            low = mid+1
    return ans # least element finding
arr = [4,5,6,7,0,1,2,3]
result = rotationbyk(arr)
print(result)
