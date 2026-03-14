# almost sorted
# courtesy of https://www.youtube.com/watch?v=SyVUe7h4zho

from copy import *

def almostSorted(arr):
  sorted_arr = deepcopy(arr)
  sorted_arr.sort()
  n = len(arr)
  # case 1, if already sorted in the first place
  if arr == sorted_arr:
    print("yes")
    return
  # case 2, if need to be swapped once
  l = r = -1
  for i in range(n):
    if arr[i] > arr[i + 1]:
      l = i
      break
  for i in range(n - 1, 0, -1):
    if arr[i] < arr[i - 1]:
      r = i
      break
  temp = deepcopy(arr)
  temp[l], temp[r] = temp[r], temp[l]
  if temp == sorted_arr:
    print("yes")
    print(f"swap {l + 1} {r + 1}")
    return
  # case 3, if need to reverse segment
  temp2 = deepcopy(arr)

  temp2 = temp2[:l] + temp2[l:r + 1][::-1] + temp2[r + 1:]

  if temp2 == sorted_arr:
    print("yes")
    print(f"reverse {l + 1} {r + 1}")
    return
  # array is not "almost sorted"
  print("no")


arr = [1, 5, 4, 3, 2, 6]

almostSorted(arr)
