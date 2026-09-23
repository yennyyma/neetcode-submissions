class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        l, total = 0, 0
        minLen = len(nums) + 1

        for r in range(len(nums)):
            total += nums[r]
            while total >= target:
                minLen = min(minLen, r - l + 1)
                total -= nums[l]
                l += 1

        return 0 if minLen == len(nums) + 1 else minLen