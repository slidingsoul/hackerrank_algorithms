# mini-max sum

def miniMaxSum(arr):
  n = len(arr)
  sorted_arr = sorted(arr)
  miniSum = sum([sorted_arr[i] for i in range(0, n - 1)])
  maxSum = sum([sorted_arr[i] for i in range(1, n)])
  print(miniSum, maxSum)

def miniMaxSum_v2(arr):
  total = sum(arr)
  miniSum = total - max(arr)
  maxSum = total - min(arr)
  print(miniSum, maxSum)

arr = [1, 2, 3, 4, 5]

miniMaxSum(arr)