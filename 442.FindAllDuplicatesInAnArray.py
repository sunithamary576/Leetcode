class Solution(object):
    def findDuplicates(self, nums):
        seen=set()
        dup=[]
        for i in nums:
            if i in seen:
                dup.append(i)
            else:
                seen.add(i)
        return dup
        