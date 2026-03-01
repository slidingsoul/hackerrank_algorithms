# the hurdle race

def hurdleRace(k, height):
    return max(height) - k if (max(height) - k) > 0 else 0
