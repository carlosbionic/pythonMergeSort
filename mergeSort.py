#######################
### MERGE ALGORITHM ###
#######################

import numpy as np

def mergesort (arr): # Sort array 'arr'
 
  n = len(arr)

  if (n == 1):
    return arr
  
  l1 = arr[0:int(n/2)]
  l2 = arr[int(n/2):n]

  l1 = mergesort(l1)
  l2 = mergesort(l2)

  return merge(l1,l2)

def merge (a,b): # Merge two lists

  c = []

  while (len(a)!=0 and len(b)!=0):

    if (a[0] > b[0]):
      c.append(b[0])
      b.remove(b[0])
    else:
      c.append(a[0])
      a.remove(a[0])

  while (len(a)!=0):
    
    c.append(a[0])
    a.remove(a[0])

  while (len(b)!=0):
    
    c.append(b[0])
    b.remove(b[0])

  return c

a = -12.
b = 12.
N = 7

# Generates a random array of N elements between a and b

arr = np.random.rand(N)*(b-a) + a

arr=list(arr) # Generates a list from an array

print(arr)
print( mergesort(arr) )

