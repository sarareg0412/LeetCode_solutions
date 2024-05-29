class Solution:
    def longestPalindrome(self, s: str) -> int:
        queue = []

        count = 0

        for c in s:
            if c in queue:
                queue.remove(c)
                count += 2
            else:
                queue.append(c)

        if(len(queue)>0):
            return 1+count
        else:
                return count
            
        