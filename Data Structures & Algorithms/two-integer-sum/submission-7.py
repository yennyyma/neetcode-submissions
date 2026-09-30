class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        count = {} # value, index
        
        for i in range(len(nums)):
            complement = target - nums[i] # value

            if complement in count:
                return [count.get(complement), i]
                # OR return [count[complement], i]

            count.update({nums[i]: i})