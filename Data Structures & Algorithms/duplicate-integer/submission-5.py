class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        count = set() # tracks whether each number has already appeared once

        for n in nums:
            if n in count:
                return True

            count.add(n)

        return False
