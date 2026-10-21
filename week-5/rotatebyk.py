
def default(arr,k):
    o=[]
    l=arr[len(arr)-k:]
    for s in range(0,len(arr)-k):
        o.append(arr[s])
    return l+o

arr=[1,2,4,6,7]
k=3
result=default(arr,k)
print(result)