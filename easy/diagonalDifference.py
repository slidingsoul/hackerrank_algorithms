# diagonal difference

def diagonalDifference(arr):
  # Write your code here
  left_sum = 0
  right_sum = 0
  for i in range(len(arr[0])):
    left_sum += arr[i][i]

  k = len(arr[0]) - 1
  for j in range(len(arr[0])):
    right_sum += arr[j][k]
    k -= 1
  return abs(left_sum - right_sum)

def diagonalDifference_v2(arr):
  left_sum = 0
  right_sum = 0
  n = len(arr)

  for i in range(n):
    left_sum += arr[i][i]
    right_sum += arr[i][n - 1 - i]

  return abs(left_sum - right_sum)

def diagonalDifference_v3(arr: list[list[int]]) -> int:
  square_size = len(arr)
  left_to_right_diag, right_to_left_diag = 0, 0
  for i in range(square_size):
    left_to_right_diag += arr[i][i]
    right_to_left_diag += arr[i][square_size - i - 1]
  absolute_difference = abs(left_to_right_diag - right_to_left_diag)
  return absolute_difference


arr = [[11, 2, 4], [4, 5, 6], [10, 8, -12]]

print(diagonalDifference_v3(arr))