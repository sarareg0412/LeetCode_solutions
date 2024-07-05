class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        triples = []

        for i in range(len(nums)-2):
            if nums[i]>0:
                break
            
            if i > 0 and nums[i] == nums[i-1]:
                continue
            
            l = i+1
            r = len(nums) - 1

            while l<r:
                triple = [nums[i], nums[l], nums[r]]
                if sum(triple) < 0:
                    l += 1
                elif sum(triple) > 0:
                    r -= 1
                else:
                    triples.append(triple)
                    while l<r and nums[l] == triple[1]:
                            l +=1
                    while l<r and nums[r] == triple[2]:
                            r -=1

        return triples

        