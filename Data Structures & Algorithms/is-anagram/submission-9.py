class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False

        freqS = {}
        freqT = {}

        for i in range(len(s)):
            charS, charT = s[i], t[i]
            freqS[charS] = freqS.get(charS, 0) + 1
            freqT[charT] = freqT.get(charT, 0) + 1
        
        if len(freqS) != len(freqT):
            return False

        for key,value in freqS.items():
            if key not in freqT:
                return False

            tVal = freqT[key]
            
            if tVal != value:
                return False

        # for char in s:
        #     freq[char] = freq.get(char, 0) + 1

        # for char in t:
        #     if char not in freq:
        #         return False
        #     freq[char] = freq.get(char) - 1

        # for value in freq.values():
        #     if (value < 0):
        #         return False
        
        return True