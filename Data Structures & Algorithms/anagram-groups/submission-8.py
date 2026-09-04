class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        output = []
        anagrams = dict()
        for word in strs:
            charCount = dict()
            for char in word:
                if char in charCount:
                    charCount[char] = charCount[char] + 1
                else:
                    charCount[char] = 1
            if frozenset(charCount.items()) in anagrams:
                output[anagrams[frozenset(charCount.items())]].append(word)
            else:
                anagrams[frozenset(charCount.items())] = len(output)
                output.append([word])
        return output