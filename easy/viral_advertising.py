# viral advertising

def viralAdvertising(n):
  shared = 5
  liked = shared // 2
  cumulative = liked
  for _ in range(n - 1):
    print(shared, liked, cumulative)
    shared = liked * 3
    liked = shared // 2
    cumulative += liked
  return cumulative

print(viralAdvertising(5))