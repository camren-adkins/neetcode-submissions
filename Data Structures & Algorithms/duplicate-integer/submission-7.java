class Solution {
    public boolean hasDuplicate(int[] nums) {
        boolean duplicate = false;
        int i = 0;
        ArrayList<Integer> ints = new ArrayList<Integer>();
        for (int k = 0; k < nums.length; k++) {
            System.out.print(nums[k] + " ");
        }
        System.out.println();
        while((!duplicate) && (i < nums.length)) {
            for (int j = 0; j < ints.size(); j++) {
            
            
            duplicate = (ints.get(j) == nums[i]);
            if (duplicate)
            return true;
            System.out.print(duplicate + " ");
            }
            ints.add(nums[i]);
            i++;
        }
        return duplicate;
    }
}
