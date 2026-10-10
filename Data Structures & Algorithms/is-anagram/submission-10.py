class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        # Anagrams must always be the same length
        if len(s) != len(t):
            return False

        # Create hashmaps for both strings
        hashmap1 = {}
        hashmap2 = {}

        # Iterate through both strings to map counts of each character
        for i in range(len(s)):
            hashmap1.update({s[i]: hashmap1.get(s[i], 0) + 1})
            hashmap2.update({t[i]: hashmap2.get(t[i], 0) + 1})

        # Compare the hashmaps to see if they're equal
        if hashmap1 == hashmap2:
            return True

        return False