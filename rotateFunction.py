class Solution:
    def maxRotateFunction(self, nums: List[int]) -> int:
        s=sum(nums)
        d=sum(element * index for index,element in enumerate(nums))
        sol=d
        for pivot in range(len(nums)-1,-1,-1):
            d+=s-len(nums)*nums[pivot]
            sol=max(d,sol)
        return sol