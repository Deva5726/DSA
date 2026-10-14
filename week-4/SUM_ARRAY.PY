def sum_array(a,n,i):
    if i>=n:
        return 0
    else:
        return a[i]+sum_array(a,n,i+1)
a=[3,4]
result=sum_array(a,len(a),0)
print(result)