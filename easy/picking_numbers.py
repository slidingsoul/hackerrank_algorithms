# picking numbers

def pickingNumbers(a):
  longest = 0
  sorted_a = sorted(a)
  left = 0
  right = 0
  while left < len(sorted_a) and right < len(sorted_a):
    counter = 0
    right = left
    while right < len(sorted_a):
      if abs(sorted_a[left] - sorted_a[right]) > 1:
        left = right
        break
      else:
        counter += 1
      right += 1
    if counter > longest:
      longest = counter
  return longest

def pickingNumbers_v2(a):
  longest, left, right = 0, 0, 0
  sorted_a = sorted(a)
  while left < len(sorted_a) and right < len(sorted_a):
    while right + 1 < len(sorted_a) and abs(sorted_a[left] - sorted_a[right + 1]) <= 1:
      right += 1
    window_size = right - left + 1
    if window_size > longest:
      longest = window_size
    left = right + 1
    right = left
  return longest

a = [1, 2, 2, 3, 1, 2]


print(pickingNumbers_v2(a))