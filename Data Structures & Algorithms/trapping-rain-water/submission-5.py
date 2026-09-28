class Solution:
    def trap(self, height: List[int]) -> int:
        pointer = 0
        firstLeft = False
        firstRight = False
        leftBar = 0
        leftBarIndex = 0
        rightBar = 0
        currentVol = 0
        totalVol = 0
        width = 0
        while pointer < len(height):
            if not firstLeft and height[pointer] != 0: #init first left bar
                firstLeft = True
                leftBar = height[pointer]
                leftBarIndex = pointer
            else:
                if height[pointer] >= leftBar:
                    totalVol = totalVol + currentVol
                    currentVol = 0
                    width = 0
                    leftBar = height[pointer]
                    leftBarIndex = pointer
                else:
                    width = width + 1
                    currentVol = currentVol + leftBar - height[pointer]
                #print("Height:", height[pointer], "CV:", currentVol, "TV:", totalVol)    
            pointer = pointer + 1
        
        #print("LB:", leftBar, "LBI:", leftBarIndex)
        rightPointer = len(height) - 1
        currentVol = 0
        while rightPointer >= leftBarIndex:
            if not firstRight and height[rightPointer] != 0: #init first right bar
                firstRight = True
                rightBar = height[rightPointer]
            else:
                if height[rightPointer] >= rightBar:
                    totalVol = totalVol + currentVol
                    currentVol = 0
                    width = 0
                    rightBar = height[rightPointer]
                else:
                    width = width + 1
                    currentVol = currentVol + rightBar - height[rightPointer]
            #print("Height:", height[rightPointer], "CV:", currentVol, "TV:", totalVol)    
            rightPointer = rightPointer - 1
        #print(leftBar, leftBarIndex)

        return totalVol


