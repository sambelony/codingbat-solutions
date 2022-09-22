"""Return the number of even ints in the given array."""
def count_evens(nums):
  count = 0
  for num in nums:
    if num % 2 == 0:
      count += 1
  return count

"""Given an array length 1 or more of ints, return the difference between the largest and smallest values in the array."""
def big_diff(nums):
  return max(nums) - min(nums)

"""Return the "centered" average of an array of ints, which we'll say is the mean average of the values,
except ignoring the largest and smallest values in the array.
If there are multiple copies of the smallest value, ignore just one copy, and likewise for the largest value."""
def centered_average(nums):
  return (sum(nums) - max(nums) - min(nums))/(len(nums)-2)

"""Return the sum of the numbers in the array, returning 0 for an empty array. 
Except the number 13 is very unlucky, so it does not count and numbers that come immediately after a 13 also do not count."""
def sum13(nums):
  sums = 0
  for i in range(len(nums)):
    if nums[i] == 13 or i != 0 and nums[i - 1] == 13:
      continue
    else:
      sums += nums[i]
  return sums

"""Return the sum of the numbers in the array, except ignore sections of numbers starting with a 6 and extending to the next 7
(every 6 will be followed by at least one 7). Return 0 for no numbers."""
def sum67(nums):
  i = 0
  numbers_between = 0
  while 6 in nums[i:] and 7 in nums[i:]:
    numbers_between += sum(nums[i:][nums[i:].index(6):nums[i:].index(7) + 1:])
    i = nums.index(7, i) + 1
  return sum(nums) - numbers_between

"""Given an array of ints, return True if the array contains a 2 next to a 2 somewhere."""
def has22(nums):
  for i in range(len(nums) - 1):
    if nums[i] == 2 and nums[i + 1] == 2:
      return True
  return False