class Solution:
    def longestPalindrome(self, s: str) -> int:
        queue = []

        count = 0
        s = sorted(s)
        
        for c in s:
            if c in queue:
                queue.pop(-1)
                count += 2
            else:
                queue.append(c)

        if(len(queue)>0):
            return 1+count
        else:
                return count
            
        