# sherlock and valid string

from collections import Counter

def isValid(s):
  dic = Counter(s)
  freq_dic = {}
  for value in dic.values():
    if value not in freq_dic:
      freq_dic[value] = 1
    else:
      freq_dic[value] += 1
  mode = [k for k, v in freq_dic.items() if v == max(list(freq_dic.values()))][0]
  # case 1: each char has the same freq
  if len(freq_dic) == 1:
    return "YES"
  # case 2: need to remove one occurence only
  temp = freq_dic.copy()
  temp.pop(mode)
  # this is a case when I need to only remove 1 character from 1 occurence only
  if len(temp) == 1 and list(temp.values())[0] == 1 and list(temp.keys())[0] == 1:
    return "YES"
  to_be_removed = 0
  # need to substract from the mode otherwise
  for k, v in temp.items():
    if v != 1:
      to_be_removed += abs(v - mode)
    else:
      to_be_removed += abs(k - mode)
  if to_be_removed == 1:
    return "YES"
  else:
    return "NO"

def isValid_v2(s):
  cnt = Counter(s)
  print(cnt)
  print(set(cnt.values()))
  if len(set(cnt.values())) == 1:
    return "YES"
  elif len(set(cnt.values())) > 2:
    return "NO"
  else:
    for key in cnt:
      cnt[key] -= 1
      temp = list(cnt.values())
      try:
        temp.remove(0)
      except:
        pass
      if len(set(temp)) == 1:
        return "YES"
      else:
        cnt[key] += 1
    return "NO"

s = "aabbccddeefghi"

print(isValid_v2(s))