class Solution {
    public int longestConsecutive(int[] nums) {
        PriorityQueue queue = new PriorityQueue();
        for (int num : nums) {
            queue.add(num);
        }
        int longestCount = 0;
        int count = 0;
        int prev = 0;
        while (queue.peek() != null) {
            if (longestCount == 0) { //first
                count = 1;
                longestCount = 1;
                prev = (int) queue.poll();
            }
            else {
                if ((int) queue.peek() == (prev + 1)) {
                    count++;
                    if (count > longestCount) {
                        longestCount = count;
                    }
                }
                else {
                    if ((int) queue.peek() != prev) {
                        count = 1;
                    }
                }
                prev = (int) queue.poll();
            }
        }
        return longestCount;
    }
}
