# save the prisoner!

def saveThePrisoner(n, m, s):
  orders = []
  i = 0
  current = s
  while i < m:
    if current > n:
      current = 1
    orders.append(current)
    current += 1
    i += 1
  return orders[-1]

def saveThePrisoner_v2(n, m, s):
  return (s + m - 2) % n + 1

n = 352926151 # number of prisoner
m = 380324688  # piece of candies
s = 94730870 # start at chair

print(saveThePrisoner_v2(n, m, s))