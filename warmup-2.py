"""Given a string and a non-negative int n, return a larger string that is n copies of the original string."""
def string_times(str, n):
  return str*n

"""Given a string and a non-negative int n, we'll say that the front of the string is the first 3 chars,
 or whatever is there if the string is less than length 3. Return n copies of the front."""
 def front_times(str, n):
  return str[:3]*n

"""Given a string, return a new string made of every other char starting with the first, so "Hello" yields "Hlo"."""
def string_bits(str):
  return str[::2]

"""Given a non-empty string like "Code" return a string like "CCoCodCode"."""
def string_splosion(str):
  new_str = ""
  for n in range(len(str) + 1):
    new_str = new_str + str[:n]
  return new_str

"""Given a string, return the count of the number of times that a substring length 2 appears in the string and also
as the last 2 chars of the string, so "hixxxhi" yields 1 (we won't count the end substring)."""
def last2(str):
  count = -1
  for i in range(len(str) + 1):
    if str[-2:] == str[i:i+2]:
      count += 1
  return count

"""Given an array of ints, return the number of 9's in the array."""
def array_count9(nums):
  return nums.count(9)

"""Given an array of ints, return True if one of the first 4 elements in the array is a 9.
The array length may be less than 4."""
def array_front9(nums):
  return nums[:4].count(9) > 0

"""Given an array of ints, return True if the sequence of numbers 1, 2, 3 appears in the array somewhere."""
def array123(nums):
  count = 0
  for c in range(len(nums) - 2):
    if [1,2,3] == nums[c:c+3]:
      count += 1
  return count > 0

"""Given 2 strings, a and b, return the number of the positions where they contain the same length 2 substring.
So "xxcaazz" and "xxbaaz" yields 3, since the "xx", "aa", and "az" substrings appear in the same place in both strings."""
def string_match(a, b):
  count = 0
  c = ""
  if len(a) < len(b):
    c = a
  else:
    c = b
  for i in range(len(c) - 1):
    if a[i:i+2] == b[i:i+2]:
      count += 1
  return count
