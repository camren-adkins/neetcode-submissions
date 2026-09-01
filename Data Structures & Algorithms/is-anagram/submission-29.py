class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        sDic = dict()
        for char in s:
            if char in sDic:
                sDic[char] = sDic[char] + 1
            else:
                sDic[char] = 1
        
        tDic = dict()
        for char in t:
            if char in tDic:
                tDic[char] = tDic[char] + 1
            else:
                tDic[char] = 1
        print(sDic)
        print(tDic)
        return sDic == tDic