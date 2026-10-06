class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        #input: list of strings
        #output: list of lists of grouped anagrams

        # Define default dictionary to hold all lists
        groupedAnagrams = defaultdict(list)

        # Iterate through each string in the list and define a 26-index array to track each string
        for string in strs:
            count = [0] * 26 # 26-index array to represent each character from 'a' through 'z'

        # Iterate through each character in the string to increment by mapping ordinal value to index
            for char in string:
                count[ord(char) - ord('a')] += 1 # i.e. [1, 0, 2, 1, ...]

        # Append each 26-index array to default dict
            groupedAnagrams[tuple(count)].append(string)

        # Cast default dictionary into a list to match return type
        return list(groupedAnagrams.values())
        