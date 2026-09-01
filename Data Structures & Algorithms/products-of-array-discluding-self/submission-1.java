class Solution {
    public int[] productExceptSelf(int[] nums) {
        
        int length = nums.length;
        int[] prefixMult = new int[length];
        int[] suffixMult = new int[length];

        prefixMult[0] = 1;
        suffixMult[length - 1] = 1;
        for (int i = 1; i < length; i++) {
            prefixMult[i] = prefixMult[i - 1] * nums[i - 1];
            suffixMult[length - 1 - i] = suffixMult[length - i] * nums[length - i];
        }

        int[] output = new int[length];
        for (int i = 0; i < length; i++) {
            output[i] = prefixMult[i] * suffixMult[i];
        }

        // System.out.println(Arrays.toString(prefixMult) + " " + Arrays.toString(suffixMult));
        return output;
        /*
        1, 2, 4, 6
        1, 1, 2, 8
        48, 24, 6, 1

        -1, 0, 1, 2, 3
        1, -1, 0, 0, 0
        0, 6, 6, 3, 1
        */
    }
}  
