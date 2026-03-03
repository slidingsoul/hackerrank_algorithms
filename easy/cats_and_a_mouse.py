# cat and a mouse

def catAndMouse(x, y, z):
  distance_a = abs(z - x)
  distance_b = abs(z - y)

  if distance_a == distance_b:
    return "Mouse C"
  elif distance_a < distance_b:
    return "Cat A"
  else:
    return "Cat B"

x = 1
y = 3
z = 2

print(catAndMouse(x, y, z))