class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # Make a hashmap to track the indices and their values
        hashmap = {}

        for i in range(len(nums)):
            hashmap.update({nums[i]: i})

        for i in range(len(nums)):
            if target - nums[i] in hashmap and hashmap.get(target - nums[i]) != i:
                return [i, hashmap.get(target - nums[i])]