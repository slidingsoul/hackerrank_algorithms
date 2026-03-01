# climbing the leaderboard
def climbingLeaderboard(ranked, player):
  ranked = sorted(set(ranked), reverse=True)
  j = len(ranked) - 1
  result = []
  for i in range(len(player)):
    while j >= 0 and player[i] >= ranked[j]:
        j -= 1
    result.append(j + 2)
  return result
