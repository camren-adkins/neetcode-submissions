from bisect import bisect_left
class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        for x, num in enumerate(numbers):
            #print(bisect_left(numbers, (target - num)))
            if bisect_left(numbers, (target - num)) in range(len(numbers)) and numbers[bisect_left(numbers, (target - num))] == (target-num): #if sum pair in array
                if num + num != target:

                    return [x+1, bisect_left(numbers, (target - num))+1]
                else:
                    if x != bisect_left(numbers, (target - num)):
                        return sorted([x+1, bisect_left(numbers, (target - num))+1])
