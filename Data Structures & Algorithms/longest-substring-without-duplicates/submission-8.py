class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if (len(s) == 0):
            return 0
        max_len = 0
        l, r = 0, 0
        used = set()
        while(r < len(s)):
            # print(f"l={l}, r={r}, max_len={max_len}, set={used}")
            if s[r] not in used:
                used.add(s[r])
                max_len = max(max_len, r-l+1)
            else:
                max_len = max(max_len, r - l)
                while(l < r):
                    if s[l] != s[r]:
                        used.remove(s[l])
                        l+=1
                    else:
                        l+=1
                        break
            r+=1
        return max_len