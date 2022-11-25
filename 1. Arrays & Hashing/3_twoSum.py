class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        numsD = {}
        for i in range(len(nums)):
            complement = target - nums[i]
            if complement in numsD.keys():
                return numsD[complement],i
            numsD[nums[i]] = i