'''
给定一个整数数组 nums 和一个目标值 target，请你在该数组中找出和为目标值的那 两个 整数，并返回他们的数组下标。
'''

def twoSum(self, nums: List[int], target: int) -> List[int]:
    right = len(nums) - 1
    while right > 0:
        for i in range(right):
            if nums[i] + nums[right] == target:
                return [i, right]
        right -= 1