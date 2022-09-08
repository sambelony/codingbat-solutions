"""Given a string, return a string where for every char in the original, there are two chars."""
def double_char(str):
  return ''.join([i*2 for i in str])

"""Return the number of times that the string "hi" appears anywhere in the given string."""
def count_hi(str):
  return str.count('hi')

"""Return True if the string "cat" and "dog" appear the same number of times in the given string."""
def cat_dog(str):
  return str.count('cat') == str.count('dog')

"""Return the number of times that the string "code" appears anywhere in the given string,
except we'll accept any letter for the 'd', so "cope" and "cooe" count."""
def count_code(str):
  count = 0
  for i in range(len(str)):
    if i < (len(str) - 3) and str[i] + str[i+1] == 'co' and str[i+3] == 'e':
      count += 1
  return count

"""Given two strings, return True if either of the strings appears at the very end of the other string,
ignoring upper/lower case differences (in other words, the computation should not be "case sensitive")."""
def end_other(a, b):
    return a[-len(b):].lower() == b.lower() if len(a) > len(b) else b[-len(a):].lower() == a.lower()

"""Return True if the given string contains an appearance of "xyz" where the xyz is not directly preceeded by a period (.).
So "xxyz" counts but "x.xyz" does not."""
def xyz_there(str):
  for i in range(len(str)):
    if i <= (len(str) - 3) and str[i - 1] != '.' and str[i:i + 3] == 'xyz':
      return True
    else:
        continue
  return False
