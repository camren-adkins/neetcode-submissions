class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        counts = dict()
        for num in nums:
            if num in counts:
                counts[num] = counts[num]+1
            else:
                counts[num] = 1
        output = list([item[0] for item in sorted(counts.items(), key=lambda count: count[1], reverse=True)])[:k]
        return output