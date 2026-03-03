# electronics shop

import bisect

def getMoneySpent(keyboards, drives, b):
  curr_val = -1
  for i in range(len(keyboards)):
    for j in range(len(drives)):
      if curr_val <= keyboards[i] + drives[j] <= b:
        curr_val = keyboards[i] + drives[j]
  return curr_val

def getMoneySpent_v2(keyboards, drives, b):
  drives.sort()
  best = -1
  for k in keyboards:
    remain = b - k
    idx = bisect.bisect_right(drives, remain) - 1
    if idx >= 0:
      best = max(best, k + drives[idx])
  return best

def getMoneySpent_v3(keyboards, drives, b):
  keyboards.sort()
  drives.sort()

  i = 0                      # keyboard termurah
  j = len(drives) - 1        # drive termahal
  best = -1

  while i < len(keyboards) and j >= 0:
    total = keyboards[i] + drives[j]

    if total > b:
      # terlalu mahal → turunkan drive
      j -= 1
    else:
      # valid → update best dan coba keyboard lebih mahal
      best = max(best, total)
      i += 1

  return best

b = 10
keyboards = [3, 1]
drives = [5, 2, 8]

print(getMoneySpent_v2(keyboards, drives, b))