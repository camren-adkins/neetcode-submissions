class Solution {
    public int longestConsecutive(int[] nums) {
        
        Set<Integer> numSet = Arrays.stream(nums).boxed().collect(Collectors.toSet());
        int longestCount = 0;
        for (int value: numSet) {
            int count = 0;
            if (!numSet.contains(value - 1)){
                int current = value;
                while (numSet.contains(current)){
                    count++;
                    current++;
                }
                if (count > longestCount) longestCount = count;
            }
        }
        return longestCount;
        
    }
}
