class Solution:
    def trap(self, height: List[int]) -> int:
        res = 0
        prefix = [0] * len(height)
        suffix = [0] * len(height)
        currMax = 0
        for i in range(len(height)):
            if i == 0:
                prefix[i] = 0
                currMax = height[i]
            else:
                prefix[i] = currMax
                if currMax < height[i]:
                    currMax = height[i]
        currMax = 0
        for i in range(len(height)-1, -1, -1):
            if i == len(height) - 1:
                suffix[i] = 0
                currMax = height[i]
            else:
                suffix[i] = currMax
                if currMax < height[i]:
                    currMax = height[i]
        # print(prefix)
        # print(suffix)
        for i in range(len(height)):
            tmp = min(prefix[i], suffix[i])
            if (height[i] > tmp):
                continue
            res += tmp - height[i]
        return res