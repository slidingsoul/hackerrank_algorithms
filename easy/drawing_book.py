# drawing book

def pageCount(n, p):
  start = 1
  end = n
  even_counter = 0
  start_flipped = 0
  end_flipped = 0
  if p == 1:
    return 0
  if p == n:
    return 0
  if n % 2 == 1 and (p == n - 1):
    return 0
  while start < p:
    start += 1
    even_counter += 1
    if even_counter % 2 == 1:
      start_flipped += 1
  even_counter = 0
  if n % 2 == 1:
    while end > p:
      end -= 1
      even_counter += 1
      if even_counter % 2 == 0 and n % 2 == 1:
        end_flipped += 1
  else:
    while end > p:
      end -= 1
      even_counter += 1
      if even_counter % 2 == 1:
        end_flipped += 1
  return min(start_flipped, end_flipped)

def pageCount_v2(n, p):
  from_front = p // 2
  from_back = (n // 2) - (p // 2)
  return min(from_front, from_back)

n = 6
p = 5

print(pageCount_v2(n, p))