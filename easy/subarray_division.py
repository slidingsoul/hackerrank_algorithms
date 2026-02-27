# subarray division

def birthday(s, d, m):
  length = len(s)
  res = 0
  if length == 1 and length == m:
    return 1
  for i in range(length - m + 1):
    segment = []
    for j in range(i, i + m):
      segment.append(s[j])
    print(segment)
    if sum(segment) == d:
      res += 1
  return res

s = [4,]
d = 4
m = 1

print(birthday(s, d, m))