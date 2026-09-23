class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        prefix = ""

        for i in range(len(strs[0])): # indexes of first string
            for s in strs: # all strings in strs
                if i == len(s) or s[i] != strs[0][i]:
                    return prefix
            prefix += strs[0][i]

        return prefix