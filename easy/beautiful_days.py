# beautiful days at the movies

def reverseDigits(digits):
  result = 0
  while digits > 0:
    last_digit = digits % 10
    result = result * 10 + last_digit
    digits //= 10
  return result

def beautifulDays(i, j, k):
  days = 0
  for start in range(i, j + 1):
    reversed_start = reverseDigits(start)
    result = abs(start - reversed_start) / k
    rounded_result = int(result)
    if result == rounded_result:
      days += 1
  return days

print(beautifulDays(20, 23, 6))