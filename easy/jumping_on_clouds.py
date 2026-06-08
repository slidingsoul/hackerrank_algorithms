# jumping on clouds

def jumpingOnClouds(c):
  # print(c)
  jumps = 0
  current = 0
  while current < len(c):
    two_steps_ahead = current + 2
    one_step_ahead = current + 1
    if current == len(c) - 2:
      jumps += 1
      break
    if two_steps_ahead >= len(c) or one_step_ahead >= len(c):
      break
    if c[two_steps_ahead] == 1:
      current = one_step_ahead
    else:
      current = two_steps_ahead
    jumps += 1
  return jumps

def jumpingOnClouds_v2(c):
  jumps = 0
  n = len(c)
  current = 0

  while current < n - 1:
    if current + 2 < n and c[current + 2] == 0:
      current += 2
    else:
      current += 1
    jumps += 1
  return jumps

clouds = "0 0 1 0 0 1 0"
arr = list(map(int, clouds.split()))
print(jumpingOnClouds(arr))