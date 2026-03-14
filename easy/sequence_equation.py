# sequence equation

def permutationEquation(p):
  inversed_dic = {value: index + 1 for index, value in enumerate(p)}
  result = []
  for i in range(1, len(inversed_dic) + 1):
    result.append(inversed_dic[inversed_dic[i]])
  return result

def permutationEquation_v2(p):
  result = []
  n = len(p)
  for i in range(1, n + 1):
    result.append(p.index(p.index(i) + 1) + 1)
  return result

p = [5, 2, 1, 3, 4]
print(permutationEquation_v2(p))