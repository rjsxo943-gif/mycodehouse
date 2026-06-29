# sum_args.py
import sys

args = sys.argv[1:]

total = 0

for i in args:
    total += int(i)

print("합계:", total)