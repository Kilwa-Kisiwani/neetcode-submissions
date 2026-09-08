class Solution {
    public List<List<Integer>> threeSum(int[] nums) {
        Arrays.sort(nums);
        List<List<Integer>> result = new LinkedList<>();
        for (int i=0; i<nums.length; i++) {
            if (i > 0 && nums[i] == nums[i - 1]) continue;
            int curr = nums[i];
            int l = i+1;
            int r = nums.length - 1;
            while (l < r) {
                if (nums[l] + nums[r] < -curr) {
                    l++;
                } else if (nums[l] + nums[r] > -curr) {
                    r--;
                } else {
                    List<Integer> list = new LinkedList<>();
                    list.add(nums[l]);
                    list.add(nums[r]);
                    list.add(nums[i]);
                    result.add(list);
                    l++;
                    r--;
                    while (l < r && nums[l] == nums[l - 1]) l++;
                    while (l < r && nums[r] == nums[r + 1]) r--;
                }
            }
        }
        return result;
    }
}
