class Solution {
    public boolean hasDuplicate(int[] nums) {
        Set<Integer> known = new HashSet<>();
        for (int i=0; i<nums.length; i++) {
            if (!known.add(nums[i])) {
                return true;
            }
        }
        return false;
    }
}