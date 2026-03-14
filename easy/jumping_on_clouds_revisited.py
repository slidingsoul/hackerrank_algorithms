# jumping on the clouds: revisited

ENERGY_LEVEL = 100

def jumpingOnClouds(c, k):
  e = ENERGY_LEVEL
  n = len(c)
  modulus = n
  start = True
  i = 0
  while start:
    current = c[(i + k) % modulus]
    if current == 1:
      e -= 2
    e -= 1
    if (i + k) % modulus == 0:
      break
    i += k
  return e

c = [0, 0, 1, 0, 0, 1, 1, 0]
k = 2

print(jumpingOnClouds(c, k))