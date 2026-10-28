class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = {}
        freq = [[] for i in range(len(nums) + 1)]

        # Fill up hashmap with nums and their counts
        for n in nums:
            count[n] = count.get(n, 0) + 1
        
        # Iterate through key-value pairs in hashmap
        # We'll be mapping the nums by their counts in the array
        for n, c in count.items():
            freq[c].append(n)

        result = []
        
        for i in range(len(freq) - 1, 0, -1):
            for n in freq[i]:
                result.append(n)
                if len(result) == k:
                    return result
