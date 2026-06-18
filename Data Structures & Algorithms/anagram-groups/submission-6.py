class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        anagrams = {}

        for word in strs:
            sortedWord = ''.join(sorted(word))

            anagrams[sortedWord] = anagrams.get(sortedWord, [])
            anagrams[sortedWord].append(word)

        return list(anagrams.values())