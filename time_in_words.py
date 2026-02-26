hours = {
  1: "one",
  2: "two",
  3: "three",
  4: "four",
  5: "five",
  6: "six",
  7: "seven",
  8: "eight",
  9: "nine",
  10: "ten",
  11: "eleven",
  12: "twelve",
}

minutes = {
  1: "one",
  2: "two",
  3: "three",
  4: "four",
  5: "five",
  6: "six",
  7: "seven",
  8: "eight",
  9: "nine",
  10: "ten",
  11: "eleven",
  12: "twelve",
  13: "thirteen",
  14: "fourteen",
  15: "quarter",
  16: "sixteen",
  17: "seventeen",
  18: "eighteen",
  19: "nineteen",
  20: "twenty",
  21: "twenty one",
  22: "twenty two",
  23: "twenty three",
  24: "twenty four",
  25: "twenty five",
  26: "twenty six",
  27: "twenty seven",
  28: "twenty eight",
  29: "twenty nine",
  30: "half"
}

oclock = "o' clock"

def timeInWords(h, m):
  res = ""
  min_string = ""
  if m > 1 and m != 15 and (60 - m) != 15:
    min_string = " minutes"
  elif m == 1:
    min_string = " minute"
  if m == 0:
    res =  f"{hours[h]} {oclock}"
  else:
    if m > 30:
      minute = 60 - m
      res = f"{minutes[minute]}{min_string} to {hours[h + 1]}"
    elif m < 30:
      res = f"{minutes[m]}{min_string} past {hours[h]}"
    elif m == 30:
      res = f"{minutes[m]} past {hours[h]}"
    else:
      res = f"{hours[h]} o'clock"
  return res

h = 5
m = 45

print(timeInWords(h, m))