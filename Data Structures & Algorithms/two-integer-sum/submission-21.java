class Solution {
    public int[] twoSum(int[] nums, int target) {
        
                System.out.println(Arrays.toString(nums));

        int[] numsSorted = Arrays.copyOf(nums, nums.length);
        Arrays.sort(numsSorted);
        int i = 0;
        int j = nums.length - 1;
        int lower;
        int upper;
                System.out.println(Arrays.toString(nums));

        while(i != j) {
            System.out.println("loop");
            
        lower = numsSorted[i];
        upper = numsSorted[j];
        //System.out.println("lower: " + lower + " upper: " + upper);
        int lowerIndex = 0;
        int upperIndex = 0;
        if ((lower + upper) == target) {
            System.out.println("found target");
            for (int a = 0; a < nums.length; a ++) {
                        System.out.println("lower: " + lower + " upper: " + upper + " " + nums[a]);

                if ((nums[a] == lower) || (nums[a] == upper)) {
                        lowerIndex = a;
                        System.out.println("LI: " + lowerIndex);
                        break;
                }
            }
            for (int b = nums.length - 1; b >= 0; b--) {
                if ((nums[b] == lower) || (nums[b] == upper)) {
                        upperIndex = b;
                        break;
                }
            }
            int[] ret = {lowerIndex, upperIndex};
            return ret;
        }
        else {
            //System.out.println("i: " + i + " j: " + j);
            //System.out.println("lower: " + lower + " upper: " + upper);
            if((lower + upper) < target) {
                i++;
            }
            else {
                j--;
            }
        } 
        }
        int [] a = {};
        return (a);
        
    }
}
