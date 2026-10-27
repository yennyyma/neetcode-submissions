class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False

        hashmap1 = {}
        hashmap2 = {}

        for i in range(len(s)):
            hashmap1.update({s[i]: hashmap1.get(s[i], 0) + 1})
            hashmap2.update({t[i]: hashmap2.get(t[i], 0) + 1})

        if hashmap1 == hashmap2:
            return True

        return False