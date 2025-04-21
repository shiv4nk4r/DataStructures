# https://leetcode.com/problems/two-sum/?envType=problem-list-v2&envId=9colawc6

def twoSum(self, nums, target):
    """
    :type nums: List[int]
    :type target: int
    :rtype: List[int]
    """
    dict = {}
    for i in range(0, len(nums)):
        if nums[i] in dict:
            return [dict[nums[i]], i]
        else:
            dict[target - nums[i]] = i
    return []