class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        if len(nums) == 0:
            return []
        res = []
        available = set(nums)
        self.helper(available, [], res)
        return res



    def helper(self, nums: Set[int], curr: List[int], res: List[List[int]]):
        if len(nums) == 0:
            res.append(curr.copy())
            return
        size = len(nums)
        nums_copy = nums.copy()
        for num in nums:
            nums_copy.remove(num)
            # curr_copy = curr.copy()
            # print(curr_copy)
            # print(num)
            # curr_copy.append(num)
            curr.append(num)
            self.helper(nums_copy, curr, res)
            nums_copy.add(num)
            curr.remove(num)


            