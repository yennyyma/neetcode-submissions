class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        hashmap1 = dict()
        hashmap2 = dict()

        for char in s:
            hashmap1.update({char: hashmap1.setdefault(char, 0) + 1})

        for char in t:
            hashmap2.update({char: hashmap2.setdefault(char, 0) + 1})

        if hashmap1 == hashmap2:
            return True
        else:
            return False