# 36
# 1,36  2,18  3,12  4,8  6,6
# -> 1, 2, 3, 4, 6, 12, 18, 36

# from math import sqrt, floor

# def is_prime(n):
#   floored_root = floor(sqrt(n))
  
#   if n < 2:
#     return False
  
#   for i in range(2, floored_root + 1):
#     if n % i == 0:
#       return False
    
  
#   return True


# from math import sqrt, floor

# def is_prime(num):
#   root = floor(sqrt(num))

#   if num == 1:
#     return False

#   for i in range(2, root + 1):
#     if num % i == 0:
#       return False
  
#   return True

# let n be the input number
# Time: O(sqrt(n))
# Space: O(1)

# approach: iterate up to the floor(sqrt) of num, check if num % i = 0 -> return false. else, return true

from math import floor, sqrt

def is_prime(num):
    if num < 2:
        return False

    root = floor(sqrt(num))

    for i in range(2, root + 1):
        if num % i == 0:
            return False
    
    return True

# time: O(sqrt(n))
# space: O(1)