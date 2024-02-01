"""
CMPS 2200  Recitation 1
"""

### the only imports needed are here
import tabulate
import time
###

def linear_search(mylist, key):
  """ done. """
  for i,v in enumerate(mylist):
    if v == key:
      return i
  return -1


def binary_search(mylist, key):
  """ done. """
  return _binary_search(mylist, key, 0, len(mylist)-1)

def _binary_search(mylist, key, left, right):
  if right < left:
      return -1
  mid = (left + right) // 2
  if mylist[mid] == key:
      return mid
  elif mylist[mid] > key:
      return _binary_search(mylist, key, left, mid - 1)
  else:
      return _binary_search(mylist, key, mid + 1, right)

def time_search(search_fn, mylist, key):
  start_time = time.time()
  search_fn(mylist, key)
  end_time = time.time()
  return (end_time - start_time) * 1000 


def compare_search(sizes=[1e1, 1e2, 1e3, 1e4, 1e5, 1e6, 1e7]):
  results = []
  for n in sizes:
    mylist = list(range(int(n)))
    key = -1  
    linear_time = time_search(linear_search, mylist, key)
    binary_time = time_search(binary_search, mylist, key)
    results.append((n, linear_time, binary_time))
  return results






def print_results(results):
  """ done """
  print(tabulate.tabulate(results,
              headers=['n', 'linear', 'binary'],
              floatfmt=".3f",
              tablefmt="github"))

