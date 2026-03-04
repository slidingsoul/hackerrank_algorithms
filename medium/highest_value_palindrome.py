# highest value palindrome
# NOT DONE YET 13/33 cases are still failed!

def highestValuePalindrome(s, n, k):
  ints = [int(n) for n in s]
  left, right = 0, n - 1
  change_locations = []
  if n == 1:
    return "9"
  while left <= right:
    if ints[left] != ints[right]:
      change_locations.append([left, right])
    left += 1
    right -= 1
  if len(change_locations) > k:
    return "-1"
  if len(change_locations) == 0 and k > 1:
    left, right = 0, n - 1
    while left <= right:
      if ints[left] != 9 and ints[right] != 9:
        change_locations.append([left, right])
      left += 1
      right -= 1
    for i, j in change_locations:
      while k % 2 != 0 and k > 1:
        ints[i] = 9
        ints[j] = 9
        k //= 2
      if k == 1:
        if ints[i] > ints[j]:
          ints[j] = ints[i]
        else:
          ints[i] = ints[j]
        k -= 1
  for i, j in change_locations:
    while k % 2 != 0 and k > 1:
      ints[i] = 9
      ints[j] = 9
      k //= 2
    if k == 1:
      if ints[i] > ints[j]:
        ints[j] = ints[i]
      else:
        ints[i] = ints[j]
      k -=1
  return ''.join(str(i) for i in ints)

def highestValuePalindrome_v2(s, n, k):
  ints = [int(n) for n in s]
  left, right = 0, n - 1
  change_locations = []
  isPalindrome = True
  if n == 1:
    return "9"
  while left < right:
    if ints[left] != ints[right]:
      change_locations.append([left, right])
    left += 1
    right -= 1
  if len(change_locations) > k:
    return "-1"
  if len(change_locations) > 0:
    isPalindrome = False
  if isPalindrome:
    left_2 = 0
    right_2 = n - 1
    while left_2 < right_2 and k > 0 and k % 2 == 0:
      if ints[left_2] != 9 and ints[right_2] != 9:
        ints[left_2] = 9
        ints[right_2] = 9
        k -= 2
      left_2 += 1
      right_2 -=1
  else:
    for i, j in change_locations:
      if k <= 0:
        break
      if k > 1 and k % 2 == 0:
        ints[i] = 9
        ints[j] = 9
        k -= 2
      else:
        if ints[i] > ints[j]:
          ints[j] = ints[i]
        else:
          ints[i] = ints[j]
        k -=1
    left_3 = 0
    right_3 = n - 1
    while left_3 < right_3 and k > 0 and k % 2 == 0:
      ints[right_3] = 9
      ints[left_3] = 9
      left_3 += 1
      right_3 += 1
      k -= 2
  return ''.join(str(i) for i in ints)



n = 5
k = 1
s = '12321'


print(highestValuePalindrome_v2(s, n, k))