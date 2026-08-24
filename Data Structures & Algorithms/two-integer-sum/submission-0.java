class Solution {
    public int[] twoSum(int[] nums, int target) {
        Map<Integer, Integer> known = new HashMap<>();
        for (int i=0; i<nums.length; i++) {
            if (known.containsKey(target - nums[i])) {
                return new int[]{known.get(target-nums[i]), i};
            }
            if (!known.containsKey(nums[i])) {
                known.put(nums[i], i);
            }

        }
        return new int[]{0, 0};
    }
}
