class Solution:
    def countNicePairs(self, nums: List[int]) -> int:
        d={}
        for i in range(len(nums)):
            diff = nums[i]-int(str(nums[i])[::-1])
            if diff not in d:
                d[diff] = 1
            else:
                d[diff] +=1
        s=0
        for i in d.values():
            s+=(i*(i-1)//2)

        return s%(10**9+7)