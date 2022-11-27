class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # implementing neetcodes solution

        # make a counter of occurrences for each unique value in nums
        count = {}
        for num in nums:
            count[num] = 1 + count.get(num, 0)

        # create a list (freqs) of lists of the same length as nums
        # iterate through counter and append the number to the index of its count
        freqs = [[] for i in range(len(nums))]
        for n in count:
            freqs[count[n] - 1].append(n)

        # finally, create a res list and iterate backward through freqs
        # keep adding elements of each list from freqs until the length(res) == k
        # return res
        res = []
        for j in freqs[::-1]:
            for c in range(len(j)):
                res.append(j[c])
                if len(res) == k:
                    return res

###############################################################################################################
###############################################################################################################
###############################################################################################################

# my solution from
# count = {}
# for i in nums:
#     if i in count:
#         count[i] += 1
#     else:
#         count[i] = 1
# occurances = [[] for j in range(len(nums))]
# for num in count:
#     occurances[count[num]-1].append(num)
# res = []
# for r in occurances[::-1]:
#     if len(r) > 0:
#         for val in r:
#             res.append(val)
#         k -= len(r)
#     if k == 0:
#         return res
#     # if k < 0:
#     #     print("not a unique solution")
