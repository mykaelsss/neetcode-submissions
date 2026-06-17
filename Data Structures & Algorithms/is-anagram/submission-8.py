class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        # First check if the lengths of the strings match, if not return False, continue otherwise
        # Next itterate over the s string and create a freq object for the chars
        # Finally itterate over t string and if a char is seen that s doesn't have return false or if char

        if len(s) != len(t):
            return False

        freq = {}

        for char in s:
            freq[char] = freq.get(char, 0) + 1

        for char in t:
            if char not in freq:
                return False
            freq[char] = freq.get(char) - 1

        for value in freq.values():
            if (value < 0):
                return False
        
        return True