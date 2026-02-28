# fibonacci modified

import sys

sys.set_int_max_str_digits(0)
def fibonacciModified(t1, t2, n):
  sequence = {1: t1, 2: t2}
  for i in range(3, n+1):
    sequence[i] = sequence[i - 2] + (sequence[i - 1] ** 2)
  return sequence[n]
    
t1 = 1
t2 = 1
n = 20

print(fibonacciModified(t1, t2, n))
