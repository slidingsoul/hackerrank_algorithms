# compare the triplets
# solved a long time ago

def compareTriplets(a, b):
  n = len(a)
  alice, bob = 0, 0
  for i in range(n):
    if a[i] > b[i]:
      alice += 1
    elif a[i] < b[i]:
      bob += 1
  return [alice, bob]

a = [1, 2, 3]
b = [3, 2, 1]

print(compareTriplets(a, b))