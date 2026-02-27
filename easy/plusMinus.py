# plus minus

def plusMinus(arr):
  length = len(arr)
  pos, neg, zero = 0, 0, 0
  for i in range(length):
    if arr[i] > 0:
      pos += 1
    elif arr[i] < 0:
      neg += 1
    else:
      zero += 1
  print(f"{(pos/length):.6f}\n{(neg/length):.6f}\n{(zero/length):.6f}")



arr = [-4, 3, -9, 0, 4, 1]

plusMinus(arr)