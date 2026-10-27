class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hashmap = {}

        for i, n in enumerate(nums):
            hashmap.update({n: i})

        for i in range(len(nums)):
            diff = target - nums[i]
            print(diff)
            j = hashmap.get(diff)
            print(j)
            if j in hashmap.values() and i != j:
                return [i, j]

        return []