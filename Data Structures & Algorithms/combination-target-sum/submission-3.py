class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        res_set = set()
        res = []
        nums = sorted(nums)
        self.helper(nums, target, 0, res_set, [], 0)

        for element in res_set:
            res.append(list(element))
        return res
        
    def helper(self, nums: List[int], target: int, curr: int, res_set: set, curr_progress: list, index: int) -> None:
        for i in range(index, len(nums)):
            num = nums[i]
            curr += num
            curr_progress.append(num)
            if curr == target:
                res_set.add(tuple(sorted(curr_progress)))
            elif curr > target:
                curr_progress.pop(-1)
                return
            else:
                self.helper(nums, target, curr, res_set, curr_progress, i)
            curr_progress.pop(-1)
            curr -= num
        return