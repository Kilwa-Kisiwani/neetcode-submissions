class Solution:

    def encode(self, strs: List[str]) -> str:
        final_str = ""
        for string in strs:
            final_str += '#'
            final_str += str(len(string))
            final_str += '#'
            final_str += string
        # print(final_str)
        return final_str

    def decode(self, s: str) -> List[str]:
        res = []
        index = 0
        while index < len(s):
            curr_len = ""
            for i in range(index+1, len(s)):
                if s[i] == '#':
                    index = i+1
                    break
                curr_len += s[i]
            if int(curr_len) == 0:
                res.append("")
            else:
                res.append(s[index: index+int(curr_len)])
                index += int(curr_len)

        return res
                