# counting valleys

def countingValleys(steps, path):
  # Write your code here
  sea_level = 0
  current_level = 0
  valley_tentative = False
  num_of_valley = 0
  for char in path:
    if char == "U":
      current_level += 1
    elif char == "D":
      current_level -= 1
    if current_level < sea_level:
      valley_tentative = True
    if current_level >= sea_level and valley_tentative:
      num_of_valley += 1
      valley_tentative = False
  return num_of_valley
