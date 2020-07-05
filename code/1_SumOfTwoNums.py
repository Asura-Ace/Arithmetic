'''
题目：
给定一个整数数组 nums 和一个目标值 target，请你在该数组中找出和为目标值的那 两个 整数，并返回他们的数组下标。
'''

"""
在nums最后设置一个指针right，遍历它之前的nums中的所有元素，如果找到则输出，否则right前移 -> 4172ms
"""
def twoSum(self, nums: List[int], target: int) -> List[int]:
    right = len(nums) - 1
    while right > 0:
        for i in range(right):
            if nums[i] + nums[right] == target:
                return [i, right]
        right -= 1

"""
在上述算法中增加一个判断 -> 600ms
"""
def twoSum(self, nums: List[int], target: int) -> List[int]:
    right = len(nums) - 1
    while right > 0:
    	if target - nums[right] in nums[:right]: # 如果right之前的元素中没有想找的元素就跳过
	        for i in range(right):
	            if nums[i] + nums[right] == target:
	                return [i, right]
        right -= 1

"""
用Python的list.index代替for循环 -> 572ms
"""
def twoSum(self, nums: List[int], target: int) -> List[int]:
    right = len(nums) - 1
    while right > 0:
        if target - nums[right] in nums[:right]:
            return [nums[:right].index(target - nums[right]), right]
        right -= 1

"""
字典hash搜索 -> 64ms ps:这字典的搜索也太快了吧
"""
def twoSum(self, nums: List[int], target: int) -> List[int]:
    hashmap = {}
    for i, num in enumerate(nums):
        hashmap[num] = i
    for i, num in enumerate(nums):
        j = hashmap.get(target - num)
        if j is not None and j != i:
            return [i, j]

"""
字典hash搜索改进版：随着元素的加入逐渐搜索 ->64ms 性能没有提升，是因为字典搜索得太快了么？
"""
def twoSum(self, nums: List[int], target: int) -> List[int]:
    hashmap = {}
    for i, num in enumerate(nums):
        if hashmap.get(target - num) is not None:
            return [i, hashmap.get(target - num)]
        hashmap[num] = i