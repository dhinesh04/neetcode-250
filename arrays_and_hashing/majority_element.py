# Approach 1: Hash Map
class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        hashMap = dict()
        res, maxCount = 0,0
        for i in nums:
            hashMap[i] = 1 + hashMap.get(i,0)
            if hashMap[i] > maxCount:
                res = i
            maxCount = max(hashMap[i], maxCount)
        return res
        

# Approach 2: Boyer-Moore Algorithm
class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        majElem, count = 0, 0 
        for i in nums:
            if count == 0:
                majElem = i
            if i == majElem:
                count+=1
            else:
                count-=1
        return majElem