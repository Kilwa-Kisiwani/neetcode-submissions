class Solution:
    def climbStairs(self, n: int) -> int:
        cache = [1, 2]

        if n <= 2:
            return cache[n-1]
        
        for i in range(3, n):
            temp = cache[1]
            cache[1] = cache[0] + cache[1]
            cache[0] = temp
        return cache[0] + cache[1]
