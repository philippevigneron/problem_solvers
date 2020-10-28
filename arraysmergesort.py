from datetime import datetime
from random import randrange
import sys

size = int(sys.argv[1])

def generate_random_array(size):
  ar = []
  start = 0
  for i in range(size):
    if len(ar)!=0: start = ar[-1]
    ar.append(randrange(start, start+10))
  return ar

def gosort1():
  print('Method 1')
  ar1 = generate_random_array(size)
  ar2 = generate_random_array(size)
  if size <= 50: print(ar1,ar2)
  start = datetime.now()
  current = 0
  for i in range(len(ar2)):
    for j in range(len(ar1)-current):
      if (ar2[i] < ar1[j]): 
        ar1.insert(j,ar2[i])
        break
      if j == (len(ar1)-1): ar1.append(ar2[i])
  #print(ar1)
  end = datetime.now()
  print('Computation time: ',round((end-start).total_seconds(),3))

def gosort2():
  print('Method 2')
  ar1 = generate_random_array(size)
  ar2 = generate_random_array(size)
  if size <= 50: print(ar1,ar2)
  start = datetime.now()
  j = -1
  for i in range(len(ar2)):
    while j < (len(ar1)-1):
      j += 1
      if (ar2[i] < ar1[j]): 
        ar1.insert(j,ar2[i])
        break
    if j == (len(ar1)-1): ar1.append(ar2[i])
  #print(ar1)
  end = datetime.now()
  print('Computation time: ',round((end-start).total_seconds(),3))

def gosort3():
  print('Method 3')
  ar1 = generate_random_array(size)
  ar2 = generate_random_array(size)
  if size <= 50: print(ar1,ar2)
  start = datetime.now()
  res = []
  i = j = 0
  for k in range(len(ar1) + len(ar2)):
    if (i < len(ar1) and j < len(ar2)) and ar1[i] < ar2[j]:
      res.append(ar1[i])
      i += 1
    else:
      if j < len(ar2):
        res.append(ar2[j])
        j += 1
      if i < len(ar1):
        res.append(ar1[i])
        i += 1
  #print(res)
  end = datetime.now()
  print('Computation time: ', round((end - start).total_seconds(), 3))

gosort1()
gosort2()
gosort3()
