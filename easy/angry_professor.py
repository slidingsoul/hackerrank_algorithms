# angry professor

def angryProfessor(k, a):
  onTime= 0
  for student in a:
    if student <= 0:
      onTime += 1
  return "NO" if onTime >= k else "YES"

k = 2
a = "0 -1 2 1"
a = list(map(int, a.split()))

print(angryProfessor(k, a))