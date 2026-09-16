class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if (len(s) == 0):
            return 0
        curr_max_len = 1
        l, r = 0, 1
        curr_len = 1
        used = {s[l]}
        while(r < len(s)):
            # print(len(s))
            # print(f"at r={r}, s[r]={s[r]}, l={l}, s[l]={s[l]}, set={used}")
            if s[r] not in used:
                curr_len += 1
                used.add(s[r])
                r+=1
                # print(f"GOOD: {s[l:r]}")
            else:
                if curr_len > curr_max_len:
                    curr_max_len = curr_len
                new_l = s[l:r].index(s[r]) + 1 + l
                # print(s[l:r].index(s[r]))
                used -= set(s[l:new_l])
                used.add(s[r])
                curr_len = r - new_l + 1
                l = new_l
                r+=1
                # print(f"BAD: shrinked to {s[l:r]}, l={l}, r={r}, curr_len={curr_len}")
        if curr_len > curr_max_len:
            curr_max_len = curr_len

        return curr_max_len