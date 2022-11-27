class Solution:
    # neetcode did this one differently but I think my solution works well since it is same space and time complexity
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        product = 1
        num_zeros = 0
        for n in range(len(nums)):
            nums[n] = int(nums[n])
            if nums[n] != 0:
                product *= nums[n]
            else:
                num_zeros += 1

        res = [0 for l in range(len(nums))]
        if num_zeros >= 2:
            return res
        for i in range(len(nums)):
            if num_zeros == 1:
                if nums[i] == 0:
                    res[i] = product
            # if no zeros
            else:
                res[i] = int(product/nums[i])
        return res