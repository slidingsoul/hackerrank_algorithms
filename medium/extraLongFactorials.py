# extra long factorials

def extraLongFactorials(n):
  if(n == 1 or n == 0):
    return 1
  return n * extraLongFactorials(n - 1)

def extraLongFactorials_v2(start: int) -> None:
  result = start
  for i in range(start - 1, 0, -1):
    result *= i
  print(result)

if __name__ == '__main__':
  # n = int(input().strip())

  print(extraLongFactorials_v2(25))