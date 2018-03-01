#fizzbuzzの問題

import sys

N = int(sys.argv[1])

if N % 2 == 0:
  print("Mario", end="")
if N % 5 == 0:
  print("Luigi", end="")

print()
