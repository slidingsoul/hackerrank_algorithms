# utopian tree

def utopianTree(n):
  start = 1
  for i in range(1, n + 1):
    if i % 2 == 0:
      start += 1
    else:
      start *= 2
  return start

print(utopianTree(4))