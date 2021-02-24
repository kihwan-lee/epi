import math
"""
Things to Review 
Operators: Arithmetic, Comparison, Logical, Bitwise, and Assignment
Caching: Putting something into a temporary storage area that stores the used items for easy access
Math & Random libraries
"""

def reverse(x):
    result, x_remaining = 0, abs(x)
    while x_remaining:    #while x_remaining is >= than 0
        result = result * 10 + x_remaining % 10   #Takes the last digit and adds it to the end of result
        x_remaining //=10   #Takes away the digit in the ten's place of integer
        print('x_remaining is', x_remaining)
        print('result:', result)
    return -result if x < 0 else result   #-result will make a negative integer a positive integer
    

# reverse(1132)
# print(113 % 10)
# print(11 % 10)
# print(1 % 10)


def is_palindrome_number(x):
  if x <= 0:
    return x == 0
  
  num_digits = math.floor(math.log10(x)) + 1    #Number of digits in the integer given
  print(num_digits)
  msd_mask = 10**(num_digits - 1)   #Most significant digit
  print(msd_mask)

  for i in range(int(num_digits) // 2):
    if x // msd_mask != x % 10:   #Compares numbers, if same, continue, if not same, return False
      print(x // msd_mask)
      print(x % 10)
      print('False')
      return False
    
    x %= msd_mask   #Remove the most significant digit of x
    print('x:', x)
    x //= 10    #Remove the least significant digit of x
    print('x:', x)
    msd_mask //= 100    #Reduces the most significant digit by 00 so that it's equal to the number of digits in integer
    print('msd_mask:', msd_mask)
  print('True')

is_palindrome_number(1234564321)

#Note