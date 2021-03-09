
"""
Things to Review
Be comfortable with subarrays
Parallel Logic when operating on 2D arrays
Array Libraries
"""


# Objective: Reorder its entries so that the even entries appear first

# A = [2,5,3,9,8,1,7,6,4]
# def even_odd(A):
#   next_even, next_odd = 0, len(A) - 1   #Set next_odd equal to len(A) - 1 so it matches next_even to 0 on the while loop
#   while next_even < next_odd:
#     print(A)
#     if A[next_even] % 2 == 0:   #Start at index 0. 
#       print('what number:', A[next_even])
#       next_even += 1    #Enumerates to next index up
#       print(next_even)
#       print('It was even')
    
#     else:
#       A[next_even], A[next_odd] = A[next_odd], A[next_even]   #Creates the swap so the even number is ahead of odd number
#       print(A[next_even], A[next_odd])
#       next_odd -= 1   #Enumerates to next index down
#       print(next_odd)
#       print('It was odd')

#   print('A:', A)


# even_odd(A)

# Dutch National Flag Problem
#Starting over again

# Given an array of integers and one integer( A), write a function to find a pair of numbers in the given array that the sum of the two numbers is the closest to A in this array.  

n = [1, 2, 0, 5, 9]
answer = 4

def find_closest_pair(n):
  current_pair, compare_pair = (n[0] + n[1]), (n[0] + n[2])
  if answer - compare_pair < answer - current_pair:
    compare_pair = current_pair
  else:
    compare_pair = (n[0] + n[3])

  print(current_pair)

find_closest_pair(n)