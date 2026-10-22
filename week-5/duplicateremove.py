class Solution:
    def removeDuplicates(self, arr):
        l=[]
        freq={}
        for i in arr:
            freq[i]=freq.get(i,0)+1
            if freq[i]==1:
                l.append(i)
        print(l)
                           
arr=[1,2,2,3,4,4,5,5,5,6,7,8,8]
rr=[1,2,4]
sol=Solution()
sol.removeDuplicates(arr)
sol.removeDuplicates(rr)
