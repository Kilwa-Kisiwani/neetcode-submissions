class Solution {
    public int longestConsecutive(int[] nums) {
        Arrays.sort(nums);
        int currMax = 0;
        int curr = 0;

        for (int i=0; i<nums.length; i++) {
            // System.out.println("i = " + i + " : " + nums[i]);
            if (i == 0) {
                curr = 1;
            }
            else if (nums[i] == nums[i-1]) {
                continue;
            }
            else if (nums[i] != nums[i-1] + 1) {
                if (currMax < curr) {
                    currMax = curr;
                }
                curr = 1;
            } else {
                curr ++;
            }
            // System.out.println("curr:" + curr + ", currMax: " + currMax);
        }
        if (curr > currMax) {
            currMax = curr;
        }
        return currMax;
    }
}
