class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        counts = dict()
        for num in nums:
            if num in counts:
                counts[num] = counts[num] + 1
            else:
                counts[num] = 1
        #print(counts)
        #sorted_by_age = sorted(students, key=lambda student: student[2])

        #print(list(counts.items()))
        output = []
        output = sorted(list(counts.items()), key=lambda count: count[1], reverse=True)
        output = list([item[0] for item in output])[:k]
        #output = list(sorted(counts, key=lambda count: count[1]))
        #print(output)
        #print(sorted(counts.keys()))
        #output = list(sorted(counts.keys(), reverse=True))[:k]
        #print(*(num[0] for num in counts.items()))
        #output.append(*nums[0] for num in counts.items())
        #print(list(*num[0] for num in counts.items())[:k])
        #print(output)
        #output = list(num[0] for num in sorted(counts.items(), reverse=True))[:k]
        return output
            