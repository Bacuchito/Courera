#The following code can lead to an infinite loop. Fix the code so that it can finish successfully for all numbers.
# Note: Try running your function with the number 0 as the input, and see what you get!

def is_power_of_two(n):
  # Check if the number can be divided by two without a remainder
  while n % 2 == 0:
    if n <= 0:
      return False
    else: 
      n = n/2
      return True
    break
  # If after dividing by two the number is 1, it's a power of two
  if n == 1:
    return True
  return False
  

print(is_power_of_two(0)) # Should be False
print(is_power_of_two(1)) # Should be True
print(is_power_of_two(8)) # Should be True
print(is_power_of_two(9)) # Should be False


################################################################

# Fill in the empty function so that it returns the sum of all 
# the divisors of a number, without including it. A divisor is a number 
# that divides into another without a remainder.

def sum_divisors(n):
  # Return the sum of all divisors of n, not including n
  return sum([i for i in range(1, n)
                if n % i == 0])
                
print(sum_divisors(0))
# 0
print(sum_divisors(3)) # Should sum of 1
# 1
print(sum_divisors(36)) # Should sum of 1+2+3+4+6+9+12+18
# 55
print(sum_divisors(102)) # Should be sum of 2+3+6+17+34+51
# 114