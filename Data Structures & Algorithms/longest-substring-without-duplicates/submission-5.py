class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if (len(s) == 0):
            return 0
        curr_max_len = 1
        l, r = 0, 1
        curr_len = 1
        used = {s[l]}
        while(r < len(s)):
            if s[r] not in used:
                curr_len += 1
                used.add(s[r])
                r+=1
            else:
                if curr_len > curr_max_len:
                    curr_max_len = curr_len
                new_l = s[l:r].index(s[r]) + 1 + l
                used -= set(s[l:new_l])
                used.add(s[r])
                curr_len = r - new_l + 1
                l = new_l
                r+=1
        if curr_len > curr_max_len:
            curr_max_len = curr_len

        return curr_max_len