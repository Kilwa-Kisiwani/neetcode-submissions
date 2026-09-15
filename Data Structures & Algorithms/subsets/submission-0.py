class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        res = []
        self.helper(nums, 0, [], res)
        return res


    def helper(self, nums: List[int], index: int, curr: List[int], res: List[List[int]]):
        if index == len(nums):
            res.append(curr)
            return
        next1 = curr.copy()
        next2 = curr.copy()
        next2.append(nums[index])
        self.helper(nums, index+1, next1, res)
        self.helper(nums, index+1, next2, res)