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

n = 6
staircase_v2(n)