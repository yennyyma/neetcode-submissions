class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        result = defaultdict(list)

        for s in strs: # "act"
            count = [0] * 26
            for char in s: # "a" in "act"
                count[ord(char) - ord("a")] += 1
            # {a: 1, c: 1, t: 1}
            
            result[tuple(count)].append(s)

        return list(result.values())