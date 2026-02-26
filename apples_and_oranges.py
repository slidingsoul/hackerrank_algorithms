def countApplesAndOranges(s, t, a, b, apples, oranges):
  # Write your code here
  apples_fall = [x + a for x in apples]
  oranges_fall = [y + b for y in oranges]
  res_apples = len([i for i in apples_fall if s <= i <= t])
  res_oranges = len([j for j in oranges_fall if s <= j <= t])
  print(f"{res_apples}\n{res_oranges}")
  
def countApplesAndOranges_v2(s, t, a, b, apples, oranges):
  res_apples = sum(1 for dist in apples if s <= a + dist <= t)
  res_oranges = sum(1 for dist in oranges if s <= b + dist <= t)
  print(f"{res_apples}\n{res_oranges}")


s = 7
t = 10
a = 4
b = 12
apples = [2, 3, -4]
oranges = [3, -2, -4]

countApplesAndOranges_v2(s, t, a, b, apples, oranges) # 1 2