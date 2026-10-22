class Solution:
    def removeDuplicates(self, arr):
        l=[]
        freq={}
        for i in arr:
            freq[i]=freq.get(i,0)+1
            if freq[i]==1:
                l.append(i)
        print(l)
                           
arr=[2, 2, 2,2,2]
rr=[1,2,4]
sol=Solution()
sol.removeDuplicates(arr)
sol.removeDuplicates(rr)
