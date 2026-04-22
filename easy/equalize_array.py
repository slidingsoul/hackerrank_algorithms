# equalize the array

# cari maximum

from collections import Counter

def equalizeArray(arr):
  occurence = Counter(arr)
  mode_element = occurence.most_common(1)[0][0]
  min_deletion = 0
  for key, value in occurence.items():
    if key != mode_element:
      min_deletion += value
  return min_deletion

inputStr = "1 2 2 3"
arr = list(map(int, inputStr.strip().split(" ")))

print(equalizeArray(arr))