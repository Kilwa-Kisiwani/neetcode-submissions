class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        res = []
        candidates.sort()
        # print(candidates)
        def helper(candidates: List[int], target: int, curr: int, curr_progress: List[int], index: int, res: List[List[int]]):
            # print(curr, curr_progress, index, res)
            for i in range(index, len(candidates)):
                if (i>0 and candidates[i] == candidates[i-1] and i > index):
                    continue
                curr_progress.append(candidates[i])
                curr += candidates[i]
                if curr == target:
                    res.append(curr_progress.copy())
                elif curr > target:
                    curr_progress.pop(-1)
                    return
                else:
                    helper(candidates, target, curr, curr_progress, i+1, res)
                curr_progress.pop(-1)
                curr -= candidates[i]
            return

        helper(candidates, target, 0, [], 0, res)
        return res