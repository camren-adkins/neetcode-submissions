class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        values = set(nums)
        longestCount = 0
       
        while values:
            count = 0
            start = next(iter(values))
            current = start
            while current in values:
                count = count + 1
                values.remove(current)
                current = current + 1
            current = start - 1
            while current in values:
                count = count + 1
                values.remove(current)
                current = current - 1
            if count > longestCount: longestCount = count
        return longestCount