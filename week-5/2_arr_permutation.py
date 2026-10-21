# a =[1,2,2,3]
# b =[2,1,3,2]
#  True ,As two arrays have same elements eventhough the order is irregular.
def checkequal(a:list[int],b:list[int])->bool:
    if len(a)!=len(b):
        return False
    freq={}
    for num in a:
        freq[num]=freq.get(num,0)+1
    for num in b:
        if num not in freq:
            return False
        freq[num]=freq[num]-1
        if freq[num]==0:
            del freq[num]
    return len(freq)==0
a=[1,2,2,3]
b=[2,1,3,2]
result=checkequal(a,b)
print(result)