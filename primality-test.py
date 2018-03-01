#与えられた数が素数かどうかを判定します

import sys
import math

N = int(sys.argv[1])
p = 0
n = 0

for i in range(2, N):
  if pow(i, N) % N == i % N:
    p += 1
  else:
    n += 1

if p > n:
  print("素数だよ")
else:
  print("素数じゃないよ")
