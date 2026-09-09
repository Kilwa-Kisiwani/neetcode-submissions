class Solution {
    public int[] productExceptSelf(int[] nums) {
        int[] output = new int[nums.length];
        int[] prefix = new int[nums.length];
        int[] suffix = new int[nums.length];
        for (int i=0; i<nums.length; i++) {
            if (i == 0) {
                prefix[0] = 1;
            } else if (i == 1) {
                prefix[1] = nums[0];
            } else {
                prefix[i] = prefix[i - 1] * nums[i - 1];
            }
        }
        for (int i=nums.length - 1; i>=0; i--) {
            if (i == nums.length - 1) {
                suffix[i] = 1;
            } else if (i == nums.length - 2){
                suffix[i] = nums[i + 1];
            } else {
                suffix[i] = nums[i + 1] * suffix[i+1];
            }
        }
        // System.out.println(Arrays.toString(prefix));
        // System.out.println(Arrays.toString(suffix));
        for (int i=0; i<nums.length; i++) {
            output[i] = suffix[i] * prefix[i];
        }
        return output;
    }
}  
