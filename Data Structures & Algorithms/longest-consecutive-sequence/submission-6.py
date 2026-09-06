class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        heapq.heapify(nums)
        count = 0
        longestCount = 0
        prev = 0

        if nums:
            count = 1
            longestCount = 1
            prev = heapq.heappop(nums)
        
        while nums:
            #print(nums[0])
            #print('Count ', count, 'LCount', longestCount)
            if prev == (nums[0] - 1):
                count += 1
                prev = heapq.heappop(nums)
                if (count > longestCount):
                    longestCount = count
            else:
                if prev != nums[0]:
                    count = 1
                prev = heapq.heappop(nums)

        return longestCount