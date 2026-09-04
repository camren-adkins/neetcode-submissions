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
            charKey = frozenset(charCount.items())
            if charKey in anagrams:
                #print("Found", output)
                output[anagrams[charKey]].append(word)
            else:
                #print("Put", output)
                anagrams[charKey] = len(output)
                #print(anagrams[charKey])
                output.append([word])
        #print(output)
        
        return output