# avg_args_safe.py
import sys

args = sys.argv[1:]

if len(args) == 0:
    print("숫자를 하나 이상 입력하세요.")
else:
    total = 0

    for i in args:
        total += int(i)

    avg = total / len(args)

    print("합계:", total)
    print("평균:", f"{avg:.2f}")
    