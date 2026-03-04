# find digits

def findDigits(n):
  d1 = 10
  d2 = d1 // 10
  reducer = 0
  counter = 0
  while d2 <= n:
    res = ((n % d1) - reducer) // d2
    if res != 0 and n % res == 0:
      counter += 1
    d1 *= 10
    d2 = d1 // 10
    reducer = res
  return counter

n = 123456789

print(findDigits(n))