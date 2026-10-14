def sorted_array(a,n,i):
    if i>=n-1:
        return True
    if a[i]>a[i+1]:
        return False
    else:
        return sorted_array(a,n,i+1)
a=[5,6,2]
result=sorted_array(a,len(a),0)
print(result)
 
 