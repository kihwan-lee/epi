
"""
Things to Review
Be comfortable with subarrays
Parallel Logic when operating on 2D arrays
Array Libraries
"""


# Objective: Reorder its entries so that the even entries appear first

A = [2,5,3,9,8,1,7,6,4]
def even_odd(A):
  next_even, next_odd = 0, len(A) - 1   #Set next_odd equal to len(A) - 1 so it matches next_even to 0 on the while loop
  while next_even < next_odd:
    print(A)
    if A[next_even] % 2 == 0:   #Start at index 0. 
      print('what number:', A[next_even])
      next_even += 1    #Enumerates to next index up
      print(next_even)
      print('It was even')
    
    else:
      A[next_even], A[next_odd] = A[next_odd], A[next_even]   #Creates the swap so the even number is ahead of odd number
      print(A[next_even], A[next_odd])
      next_odd -= 1   #Enumerates to next index down
      print(next_odd)
      print('It was odd')

  print('A:', A)


even_odd(A)

# Dutch National Flag Problem

#Analysis

#The key to understanding the problem is to analyze the array.

my_list = [1024, 3, True, 6.5] 
my_list.append(False) 
print(my_list) 
my_list.insert(2,4.5) 
print(my_list) 
print(my_list.pop()) 
print(my_list) 
print(my_list.pop(1)) 
print(my_list)
my_list.pop(2) 
print(my_list) 
my_list.sort() 
print(my_list) 
my_list.reverse() 
print(my_list) 
print(my_list.count(6.5)) 
print(my_list.index(4.5)) 
my_list.remove(6.5) 
print(my_list)
del my_list[0] 
print(my_list)

# Understanding range and list functions
range(10)
list(range(10))



# Sets
my_set = {False, 3, 4.5, 6, 'cat'}
your_set = {99,3,100}
my_set.union(your_set)
my_set | your_set
my_set.intersection(your_set) 
my_set & your_set 
my_set.difference(your_set) 
my_set - your_set
{3,100}.issubset(your_set) 
{3,100} <= your_set
my_set.add("house")
my_set
my_set.remove(4.5)
my_set
my_set.pop()
my_set
my_set.clear()
my_set


# Input and Output 
# Input and Output 
