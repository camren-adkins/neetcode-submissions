class Solution {
    public int[] productExceptSelf(int[] nums) {
        int length = nums.length;
        int[] pref = new int[length];
        int[] suff = new int[length];

        if (length > 0) {
            pref[0] = 1;
            suff[length - 1] = 1;
        }
        for (int i = 1; i < nums.length; i++) {
            pref[i] = nums[i-1] * pref[i-1];
            suff[length - 1 - i] = suff[length - i] * nums[length - i];
        }
        //System.out.print(Arrays.toString(pref) + " " + Arrays.toString(suff));
        int[] output = new int[length];

        for (int n = 0; n < length; n++) {
            output[n] = pref[n] * suff[n];
        }
        return output;
    }
}  
