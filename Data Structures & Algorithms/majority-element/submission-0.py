class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        hashmap = defaultdict(int)
        maxCount = majorityNum = 0
        
        for i in nums:
            hashmap[i] += 1
            if maxCount < hashmap[i]:
                maxCount = hashmap[i]
                majorityNum = i

        return majorityNum