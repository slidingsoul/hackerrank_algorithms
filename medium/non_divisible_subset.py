# non divisible subset
def nonDivisibleSubset(k, s):
  remainder = [0] * k
  for i in s:
    remainder[i % k] += 1
  max_num = min(remainder[0], 1)
  if k % 2 == 0:
    max_num += min(remainder[k // 2], 1)
  for i in range(1, k // 2 + 1):
    if i != k - i:
      max_num += max(remainder[i], remainder[k - i])
  return max_num


s = [278, 576, 496, 727, 410, 124, 338, 149, 209, 702, 282, 718, 771, 575, 436]
# s = [4,]
k = 7

print(nonDivisibleSubset(k, s))