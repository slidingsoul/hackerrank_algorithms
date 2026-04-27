# queen's attack II

def queensAttack(n, k, y_q, x_q, obstacles):
  left_attacks = x_q - 1
  right_attacks = n - x_q
  down_attacks = y_q - 1
  up_attacks = n - y_q

  upleft_attacks = min(up_attacks, left_attacks)
  upright_attacks = min(up_attacks, right_attacks)
  downleft_attacks = min(down_attacks, left_attacks)
  downright_attacks = min(down_attacks, right_attacks)

  for obstacle in obstacles:
    x_obs = obstacle[1]
    y_obs = obstacle[0]
    if y_obs == y_q and x_obs < x_q:
      valid_attacks = (x_q - x_obs - 1)
      if valid_attacks < left_attacks:
        left_attacks = x_q - x_obs - 1


    elif y_obs == y_q and x_obs > x_q:
      valid_attacks = (x_obs - x_q - 1)
      if valid_attacks < right_attacks:
        right_attacks = x_obs - x_q - 1


    elif x_obs == x_q and y_obs < y_q:
      valid_attacks = (y_q - y_obs - 1)
      if valid_attacks < down_attacks:
        down_attacks = y_q - y_obs - 1


    elif x_obs == x_q and y_obs > y_q:
      valid_attacks = (y_obs - y_q - 1)
      if valid_attacks < up_attacks:
        up_attacks = y_obs - y_q - 1


    elif x_obs < x_q and y_obs > y_q:
      in_diag = (x_q - x_obs == y_obs - y_q)
      valid_attacks = (y_obs - y_q - 1)
      if in_diag and valid_attacks < upleft_attacks:
        upleft_attacks = y_obs - y_q - 1


    elif x_obs < x_q and y_obs < y_q:
      in_diag = (x_q - x_obs == y_q - y_obs)
      valid_attacks = (y_q - y_obs - 1)
      if in_diag and valid_attacks < downleft_attacks:
        downleft_attacks = y_q - y_obs - 1


    elif x_obs > x_q and y_obs > y_q:
      in_diag = (x_obs - x_q == y_obs - y_q)
      valid_attacks = (y_obs - y_q - 1)
      if in_diag and valid_attacks < upright_attacks:
        upright_attacks = y_obs - y_q - 1


    elif x_obs > x_q and y_obs < y_q:
      in_diag = (x_obs - x_q == y_q - y_obs)
      valid_attacks = (y_q - y_obs - 1)
      if in_diag and valid_attacks < downright_attacks:
        downright_attacks = y_q - y_obs - 1


  all_attacks = left_attacks + right_attacks + up_attacks + down_attacks + upleft_attacks + downleft_attacks + upright_attacks + downright_attacks
  return all_attacks


string = """
100 100
48 81
54 87
64 97
42 75
32 65
42 87
32 97
54 75
64 65
48 87
48 75
54 81
42 81
45 17
14 24
35 15
95 64
63 87
25 72
71 38
96 97
16 30
60 34
31 67
26 82
20 93
81 38
51 94
75 41
79 84
79 65
76 80
52 87
81 54
89 52
20 31
10 41
32 73
83 98
87 61
82 52
80 64
82 46
49 21
73 86
37 70
43 12
94 28
10 93
52 25
50 61
52 68
52 23
60 91
79 17
93 82
12 18
75 64
69 69
94 74
61 61
46 57
67 45
96 64
83 89
58 87
76 53
79 21
94 70
16 10
50 82
92 20
40 51
49 28
51 82
35 16
15 86
78 89
41 98
70 46
79 79
24 40
91 13
59 73
35 32
40 31
14 31
71 35
96 18
27 39
28 38
41 36
31 63
52 48
81 25
49 90
32 65
25 45
63 94
89 50
43 41
"""
string = string.split("\n")[1:-1]
first_multi_input = string[0].split()
n = int(first_multi_input[0])
k = int(first_multi_input[1])
second_multi_input = string[1].split()
y_q = int(second_multi_input[0])
x_q = int(second_multi_input[1])
obstacles = []
for arr in string[2:]:
  arr = list(map(int, arr.split()))
  obstacles.append(arr)
print(queensAttack(n, k, y_q, x_q, obstacles))