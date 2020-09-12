'''Given an array of integers, return indices of the two numbers such that they add up to a specific target.

You may assume that each input would have exactly one solution, and you may not use the same element twice.

Example:

Given nums = [2, 7, 11, 15], target = 9,

Because nums[0] + nums[1] = 2 + 7 = 9,
return [0, 1].

9 - 2 = 7 -> {7:0} // value:index pair
9 - 7 = 2 -> {7:0, 2:1}
9 - 11 = -2 -> {7:0, 2:1, 2:2}
9 - 15 = -6 -> {7:0, 2:1, -2:2, -6:3}

nums[i], i
'''
# O(n) - Linear Time Solution


given_nums = [2, 7, 11, 15]
target = 9

def two_sums(nums, target):
	# handle edge cases
	if len(nums) <= 1:
		return False
	# define a dictionary
	dict = {}
	#loop through the numbers list
	for i in range(len(given_nums)):
		#is the entry that we're on in the dictionary?
		if given_nums[i] in dict:
			# if yes, it returns given_nums[i], i
			return [dict[given_nums[i]], i]
		else:
			# otherwise, the dict entry target - nums[i] is equal to the index at which this occurred
			dict[target - given_nums[i]] = i
	
print(two_sums(given_nums, target)) # prints [0,1]

