class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums) == 0:
            return 0
        elif len(nums) == 1:
            return nums[0]
        elif len(nums) == 2:
            return max(nums[0], nums[1])
        prefix = [0] * len(nums)
        prefix[0] = nums[0]
        prefix[1] = max(nums[0], nums[1])
        for i in range(2, len(nums)):
            # if robbing the ith house:
            prefix[i] = max(prefix[i-2] + nums[i], prefix[i-1])
        print(prefix)

        return max(prefix[-1], prefix[-2])