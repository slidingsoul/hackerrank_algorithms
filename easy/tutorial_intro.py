# intro to tutorial challenges

def introTutorial(V, arr):
  left = 0
  right = len(arr) - 1
  while left <= right:
    mid = (left + right) // 2
    if arr[mid] == V:
      return mid
    elif arr[mid] < V:
      left = mid + 1
    elif arr[mid] > V:
      right = mid - 1
  return -1

V = 4
arr = [1, 4, 5, 7, 9, 12]

print(introTutorial(V, arr))