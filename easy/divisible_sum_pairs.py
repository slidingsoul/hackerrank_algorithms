# divisible sum pairs
def divisibleSumPairs(n, k, ar):
  count = 0
  for i in range(n):
    for j in range(i + 1, n):
      if (ar[i] + ar[j]) % k == 0:
        count += 1
  return count


n = 6
k = 5
arr = [1, 2, 3, 4, 5, 6]

print(divisibleSumPairs(n, k, arr))