class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        d = dict()
        #if divisible by two save possible dupe
        duplicate = 1.5 #arbitray non-int
        if target % 2 == 0:
            duplicate = target / 2
        firstDupe = True
        
        #sets each value to a hash with the value and index, checks duplicate values
        for idx, x in enumerate(nums):
            if x == duplicate:
                if firstDupe:
                    firstDupe = False
                else:
                    print('using dupe')
                    return [d.get(duplicate), idx]
            d[x] = idx

        for x in d:
            if target - x in d and d[x] != d[target - x]:
                print('test')
                return [d[x], d[target - x]]

        print(d)
        return [d[target/2], d[target/2]]

            