# max min
# sliding window and greedy algorithm

def maxMin(k, arr):
  arr = sorted(arr)
  n = len(arr)
  lowest = float('inf')
  for i in range(n - k + 1):
    curr = arr[i + k - 1] - arr[i]
    if curr < lowest:
      lowest = curr
  return lowest

k = 4
arr = [1, 2, 3, 4, 10, 20, 30, 40, 100, 200]

print(maxMin(k, arr))