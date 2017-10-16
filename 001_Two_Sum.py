'''
Given an array of integers, return indices of the two numbers such that they add up to a specific target.

You may assume that each input would have exactly one solution, and you may not use the same element twice.

Example:
Given nums = [2, 7, 11, 15], target = 9,

Because nums[0] + nums[1] = 2 + 7 = 9,
return [0, 1].
'''

class Solution:
	'''
	:class
	'''
    def twoSum_TLE(self, num, target):
        """
        built-in method .index
        :param num: list
        :param target: int
        :return: tuple, (index1, index2)
        """
        nums = num
        for ind1, val in enumerate(nums):
            try:
                ind2 = nums.index(target - val)
                return ind1+1, ind2+1
            except ValueError:
                continue

    def twoSum_TLE_2(self, num, target):
        nums = num
        for ind1, val in enumerate(nums):
            if target-val in nums:
                return ind1+1, nums.index(target-val)+1

    def twoSum(self, num, target):
        """
        Hash Map
        :param num: list
        :param target: int
        :return: tuple, (index1, index2)
        """
        hash_map = {}
        for ind, val in enumerate(num):
            hash_map[val] = ind

        for ind1, val in enumerate(num):
            if target-val in hash_map:
                ind2 = hash_map[target-val]
                if ind1 != ind2:
                    return ind1+1, ind2+1


if __name__ == "__main__":
    print(Solution().twoSum([3, 2, 4], 6))
