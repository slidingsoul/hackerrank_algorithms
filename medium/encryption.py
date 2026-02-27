# encryption

import math

def encryption(s):
  s = s.strip().replace(" ", "")
  sqrt = len(s) ** (0.5)
  row = math.floor(sqrt)
  column = math.ceil(sqrt)
  row = row if row * column >= len(s) else row + 1
  temp = []
  res = ""
  start = 0
  end = column
  for _ in range(row):
    sliced = s[start:end]
    temp.append(sliced)
    start += column
    end += column
  print(temp)
  for i in range(column):
    for strs in temp:
      if i < len(strs):
        res += strs[i]
    res += " "
  return res

def encryption_v2(s):
  s = s.strip().replace(" ", "")
  L = len(s)
  cols = math.ceil(math.sqrt(L))
  res = []
  for i in range(cols):
    word = s[i::cols]
    res.append(word)
  return " ".join(res)


s = "chillout"

print(encryption_v2(s))