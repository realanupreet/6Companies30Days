class Solution:
    def minOperations(self, nums: List[int], numsDivide: List[int]) -> int:
        nums.sort()
        g = gcd(*numsDivide)
        for i, x in enumerate(nums):
            if g % x == 0: return i
        return -1