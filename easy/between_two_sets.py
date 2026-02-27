# between two sets

def find_gcd(a, b):
  if (a % b == 0):
    return b
  return find_gcd(b, a % b)

def find_arr_gcd(arr):
  gcd = arr[0]
  for i in range(1, len(arr)):
    gcd = find_gcd(gcd, arr[i])
  return gcd

def find_arr_lcm(arr):
  lcm = arr[0]
  for i in range(1, len(arr)):
    el = arr[i]
    gcd_a_b = find_gcd(el, lcm)
    lcm = (el * lcm) // gcd_a_b
  return lcm

def getTotalX(a, b):
  lcm_a = find_arr_lcm(a)
  gcd_b = find_arr_gcd(b)
  res = []
  for i in range(lcm_a, gcd_b + 1, lcm_a):
    if gcd_b % i == 0:
      res.append(i)
  return len(res)

a = [2, 3, 6]
b = [42, 84]

print(getTotalX(a, b))