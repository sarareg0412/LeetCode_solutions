class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        left = 0
        right = 0
        max_len = 0

        while right < len(s):
            c = s[right]
            if c not in s[left:right]:
                right +=1
                if len(s[left:right]) > max_len:
                    max_len = len(s[left:right])
            else:
                left +=1

        return max_len
            