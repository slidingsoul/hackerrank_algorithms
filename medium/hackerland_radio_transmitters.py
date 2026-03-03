# hackerland radio transmitters

def hackerlandRadioTransmitters(x, k):
  x = sorted(x)
  transmitters = 0
  i = 0
  n = len(x)
  while i < n:
    transmitters += 1
    # find location for transmitter
    loc = x[i] + k
    while i < n and x[i] <= loc:
      i += 1
    loc = x[i - 1] + k
    while i < n and x[i] <= loc:
      i += 1
  return transmitters

k = 1
x = [1, 2, 3, 4, 5]

print(hackerlandRadioTransmitters(x, k))