class Solution {
    public int[] productExceptSelf(int[] nums) {
        //2 or more 0's: output all 0's
        //one 0: output will be all 0's, except the 0 value which will be product
        //no 0's: standard output

        int[] output = new int[nums.length];
        int firstZero = 0;
        boolean first = true;
        int product = 1;
        for (int i = 0; i < nums.length; i++) {
            if (nums[i] == 0) {
                if (first) {
                    firstZero = i;
                    first = false;
                }
                else{
                    return output;
                }
            }
            else {
                product *= nums[i];
            }
        }

        if (!first) {
        output[firstZero] = product;
        return output;
        }

        for (int i = 0; i < nums.length; i++) {
            nums[i] = product / nums[i];
        }

    return nums;
    }

    
}  
