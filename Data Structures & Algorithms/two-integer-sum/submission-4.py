class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        count = {}
        
        for i in range(len(nums)):
            complement = target - nums[i]
            j = count.get(complement)

            if complement in count and i != j:
                return [j, i]

            count.update({nums[i]: i})