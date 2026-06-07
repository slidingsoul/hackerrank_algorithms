# circular array rotation

def circularArrayRotation(a, k, queries):
  new_arr = a[:]
  for n in range(len(a)):
    a_num = a[n]
    new_pos = (n + k) % len(a)
    new_arr[new_pos] = a_num
  result = []
  for q in queries:
    result.append(new_arr[q])
  return result

a = [3, 4, 5]
k = 2
queries = [1, 2]

print(circularArrayRotation(a, k, queries))