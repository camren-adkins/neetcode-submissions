class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        counts = dict()
        for num in nums:
            counts[num] = counts[num] + 1 if num in counts else 1
            # if num in counts:
            #     counts[num] = counts[num] + 1
            # else:
            #     counts[num] = 1
        output = list(item[0] for item in sorted(list(counts.items()), key=lambda count: count[1], reverse=True))[:k]
        #output = list([item[0] for item in output])[:k]
        return output
            