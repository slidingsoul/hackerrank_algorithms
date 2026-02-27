# forming a magic square

magicSquares = [
  [[8, 1, 6], [3, 5, 7], [4, 9, 2]],
  [[6, 1, 8], [7, 5, 3], [2, 9, 4]],
  [[4, 9, 2], [3, 5, 7], [8, 1, 6]],
  [[2, 9, 4], [7, 5, 3], [6, 1, 8]],
  [[8, 3, 4], [1, 5, 9], [6, 7, 2]],
  [[4, 3, 8], [9, 5, 1], [2, 7, 6]],
  [[2, 7, 6], [9, 5, 1], [4, 3, 8]],
  [[6, 7, 2], [1, 5, 9], [8, 3, 4]]
]

def formingMagicSquare(s):
  # Write your code here
  min_cost = float('inf')
  for arr in magicSquares:
    cost = abs(arr[0][0] - s[0][0]) + abs(arr[0][1] - s[0][1]) + abs(arr[0][2] - s[0][2]) + abs(arr[1][0] - s[1][0]) + abs(arr[1][1] - s[1][1]) + abs(arr[1][2] - s[1][2])+ abs(arr[2][0] - s[2][0]) + abs(arr[2][1] - s[2][1]) + abs(arr[2][2] - s[2][2])
    if cost < min_cost:
      min_cost = cost
  return min_cost

def formingMagicSquare_v2(s):
  min_cost = float('inf')
  for m in magicSquares:
    cost = 0
    for i in range(3):
      for j in range(3):
        cost += abs(m[i][j] - s[i][j])
    if cost < min_cost:
      min_cost = cost
  return min_cost

arr = [[4, 8, 2], [4, 5, 7], [6, 1, 6]]

print(formingMagicSquare_v2(arr))