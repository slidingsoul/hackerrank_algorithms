# breaking the records

def breakingRecords(scores):
  minimum = scores[0]
  maximum = scores[0]
  min_count = 0
  max_count = 0
  for i in range(1, len(scores)):
    el = scores[i]
    if el > maximum:
      max_count += 1
      maximum = el
    if el < minimum:
      min_count += 1
      minimum = el

  return [max_count, min_count]

scores = [3, 4, 21, 36, 10, 28, 35, 5, 24, 42]

print(breakingRecords(scores))