class Solution:
    def isPalindrome(self, s: str) -> bool:
        first = 0 # first character index in the string
        last = len(s) - 1 # last character index in the string

        while first < last:
            while first < last and not self.isAlNum(s[first]):
                first += 1
            while last > first and not self.isAlNum(s[last]):
                last -= 1

            if s[first].lower() != s[last].lower():
                return False

            first += 1
            last -= 1

        return True

    def isAlNum(self, c: char) -> bool:
        return (ord('A') <= ord(c) <= ord('Z') or
                ord('a') <= ord(c) <= ord('z') or
                ord('0') <= ord(c) <= ord('9'))