# xor strings

def strings_xor(s, t):
  res = ""
  for i in range(len(s)):
      if s[i] == t[i]:
          res += '0'
      else:
          res += '1'

  return res

def strings_xor_v2(s, t):
  res = ['0' if s[i] == t[i] else '1' for i in range(len(s))]

  return "".join(res)

def strings_xor_v3(s, t):
  return "".join(['0' if a == b else '1' for a, b in zip(s, t)])

s = "10101"
t = "00101"
print(strings_xor_v3(s, t)) # should be 10000