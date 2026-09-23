class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        hashmap = defaultdict(list) 

        for i in strs: # goes through all strings
            count = [0] * 26

            for j in i: # goes through each string's letters
                count[ord(j) - ord("a")] += 1
            
            # full string's letters have been accounted for in array
            hashmap[tuple(count)].append(i)

        return list(hashmap.values())