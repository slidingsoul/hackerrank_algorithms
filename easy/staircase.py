# staircase

def staircase(n):
  for i in range(n - 1, -1, -1):
    curr = ""
    for j in range(n):
      if i <= j:
        curr += "#"
      else:
        curr += " "
    print(curr)

def staircase_v2(n):
  for i in range(n, 0, -1):
    spaces = " " * (i - 1)
    hashes = "#" * (n - i + 1)
    print(f"{spaces}{hashes}")

def staircase_v3(height: int) -> None:
  for i in range(height):
    spaces = height - i - 1
    hashtags = i + 1
    print(" " * spaces, end="")
    print("#" * hashtags)

n = 6
staircase_v3(n)