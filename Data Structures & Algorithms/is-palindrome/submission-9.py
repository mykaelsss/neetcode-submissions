class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = s.replace(" ", "").lower()

        i = 0
        j = len(s) - 1

        while i < j:
            charI = s[i]
            charJ = s[j]
            print(charI, charJ)
            if not charI.isalnum():
                i += 1
                continue
            if not charJ.isalnum():
                j -= 1
                continue
            if charI != charJ:
                return False
            else:
                i += 1
                j -= 1

        return True