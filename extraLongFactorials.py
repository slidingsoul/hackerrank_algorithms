def extraLongFactorials(n):
  if(n == 1 or n == 0):
    return 1
  return n * extraLongFactorials(n - 1)

if __name__ == '__main__':
  n = int(input().strip())

  print(extraLongFactorials(n))