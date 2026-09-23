class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False

        hashmap1 = dict()
        hashmap2 = dict()

        for char in s:
            hashmap1.update({char: hashmap1.get(char, 0) + 1})

        for char in t:
            hashmap2.update({char: hashmap2.get(char, 0) + 1})

        for i in hashmap1:
            if hashmap1[i] != hashmap2.get(i, 0):
                return False

        return True