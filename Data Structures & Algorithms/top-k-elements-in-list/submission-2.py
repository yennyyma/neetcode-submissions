class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # Make hashmap to count all occurrances of each number
        count = {}
        result = []
        # Highest frequency can only be the number of values possible in the integer array
        # This is an array of buckets (a list of empty lists)
        # Looks like: [[], [], [], ...]
        # Index:        0,  1,  2, ...
        freq = [[] for i in range(len(nums) + 1)]

        # Iterate through all values to count all occurrances
        for n in nums:
            count[n] = count.get(n, 0) + 1
        
        # Iterating through all key-value pairs in hashmap
        # key: n, value: c
        # Using the counts as the indices in the freq array
        for n, c in count.items():
            freq[c].append(n)

        # Iterating backward through the freq from highest to lowest index
        # Begin at the greatest index to 0 by decrementing by 1
        for i in range(len(freq) - 1, 0, -1):
            # Append all values in the list under each index
            for n in freq[i]:
                result.append(n)
                if len(result) == k:
                    return result