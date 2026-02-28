# number line jumps

def kangaroo(x1, v1, x2, v2):
  yes = "YES"
  no = "NO"
  if (v1 >= v2 and x1 > x2) or (v2 >= v1 and x2 > x1):
    return no
  else:
    position_difference = abs(x1 - x2)
    speed_difference = abs(v1 - v2)
    if position_difference % speed_difference == 0:
      return yes
    else:
      return no
x1 = 21
v1 = 6
x2 = 47
v2 = 3

print(kangaroo(x1, v1, x2, v2))