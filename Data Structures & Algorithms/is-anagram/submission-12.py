class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        
        hashmapS = {}
        hashmapT = {}

        for i in range(len(s)):
            hashmapS.update({s[i]: hashmapS.get(s[i], 0) + 1})
            hashmapT.update({t[i]: hashmapT.get(t[i], 0) + 1})

        if hashmapS == hashmapT:
            return True

        return False