# sales by match

from collections import Counter

def sockMerchant(n, ar):
  count = 0
  sock_counters = Counter(ar)
  for _, value in sock_counters.items():
    count += value // 2
  return count

def sockMerchant_v2(n, ar):
  return sum(v // 2 for v in Counter(ar).values())

n = 7
ar = [1, 2, 1, 2, 1, 3, 2]

print(sockMerchant_v2(n, ar)) # 2