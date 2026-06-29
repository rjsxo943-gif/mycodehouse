# mycodehouse

Python 수업에서 배운 기초 문법과 실습 코드를 복습하기 위해 정리한 저장소입니다.

교재 기준: [점프 투 파이썬](https://wikidocs.net/book/1) 01장 ~ 04장 파이썬의 입출력까지

---

## 0. 현재 학습 범위

| 날짜 | 범위 | 핵심 내용 |
|---|---|---|
| 2026-06-26 | Python 기초 문법 | 입력, 형변환, 문자열 포매팅, 리스트, 튜플, 세트, 딕셔너리, `if` 조건문 |
| 2026-06-29 | 제어문 + 입출력 | `while`, `for`, `break`, `continue`, `range`, 별 찍기, 함수, 파일 입출력, `sys.argv` |

---

## 1. 실습 파일 정리

| 파일/폴더 | 내용 |
|---|---|
| `0622/` | 초기 Python 실습 파일 |
| `0626/stringEx.py` | `input()`, `int()`, 사칙연산, f-string 출력 |
| `0626/1.py` | 리스트 생성, 반복 입력, `append()`, 합계/평균/최솟값/최댓값 계산 |
| `0626/2.py` | 문자열 리스트 입력, 리스트 출력, 인덱싱 실습 |
| `0629/1.ipynb` | `while`, `for`, `continue`, `break`, 중첩 반복문, 별 찍기, 에러 유형 정리 |
| `0629/2.ipynb` | 함수, `return`, `*args`, `**kwargs`, `match case`, 지역/전역 변수, 독스트링, 파일 입출력 |
| `0629/34.py` | `while`문 나무 찍기 예제 |
| `0629/sys1.py` | 명령행 인자 `sys.argv` 기본 출력 |
| `0629/sys2.py` | 명령행 인자를 대문자로 변환해서 출력 |
| `0629/sys_count.py` | 명령행 인자 개수 세기 |
| `0629/sum_args.py` | 명령행 인자로 받은 숫자들의 합계 계산 |
| `command.md` | 자주 쓰는 명령어 정리 |
| `requirements.txt` | Python 실행 환경 패키지 목록 |

---

# 시험 복습용 핵심 정리

## 2. 입력과 형변환

`input()`은 사용자가 입력한 값을 문자열로 받습니다.

```python
a = input("숫자를 입력하세요: ")
print(type(a))  # str
```

숫자로 계산하려면 `int()` 또는 `float()`로 바꿔야 합니다.

```python
a = int(input("첫 번째 숫자: "))
b = int(input("두 번째 숫자: "))

print(a + b)
```

정리:

| 코드 | 의미 |
|---|---|
| `input()` | 사용자 입력 받기 |
| `int()` | 문자열을 정수로 변환 |
| `float()` | 문자열을 실수로 변환 |
| `str()` | 값을 문자열로 변환 |

주의:

```python
money = int(input("돈을 넣어 주세요: "))
```

여기서 아무것도 입력하지 않고 엔터를 치면 `ValueError`가 날 수 있습니다. 빈 문자열 `''`은 정수로 바꿀 수 없기 때문입니다.

---

## 3. 출력과 문자열 포매팅

### 3-1. f-string

```python
name = "건태"
age = 25

print(f"이름: {name}, 나이: {age}")
```

`f""` 안의 `{}`에는 변수나 계산식을 넣을 수 있습니다.

```python
a = 3
b = 4
print(f"{a} + {b} = {a + b}")
```

### 3-2. `%` 포매팅

```python
treeHit = 3
print("나무를 %d번 찍었습니다." % treeHit)
```

| 기호 | 의미 |
|---|---|
| `%d` | 정수 |
| `%s` | 문자열 |
| `%f` | 실수 |

### 3-3. `print()`의 `end`

`print()`는 기본적으로 출력 후 줄바꿈을 합니다.

```python
print("A")
print("B")
```

출력:

```text
A
B
```

줄바꿈 없이 출력하려면 `end`를 사용합니다.

```python
print("A", end=" ")
print("B")
```

출력:

```text
A B
```

---

## 4. 자료형 정리

| 자료형 | 예시 | 특징 |
|---|---|---|
| 숫자형 | `1`, `3.14` | 계산 가능 |
| 문자열 | `"hello"` | 글자 데이터 |
| 리스트 | `[1, 2, 3]` | 순서 있음, 값 변경 가능 |
| 튜플 | `(1, 2, 3)` | 순서 있음, 값 변경 불가 |
| 딕셔너리 | `{ "name": "kim" }` | key-value 구조 |
| 세트 | `{1, 2, 3}` | 중복 제거, 순서 고정 아님 |
| 불 | `True`, `False` | 참/거짓 |

### 리스트

```python
numbers = []
numbers.append(10)
numbers.append(20)

print(numbers)
```

자주 쓰는 함수:

| 함수 | 의미 |
|---|---|
| `append()` | 리스트 끝에 값 추가 |
| `len()` | 길이 |
| `sum()` | 합계 |
| `min()` | 최솟값 |
| `max()` | 최댓값 |
| `sorted()` | 정렬된 결과 반환 |

평균:

```python
scores = [80, 90, 100]
avg = sum(scores) / len(scores)
print(avg)
```

### 인덱싱

```python
fruits = ["apple", "banana", "melon"]

print(fruits[0])   # apple
print(fruits[-1])  # melon
```

Python 인덱스는 0부터 시작합니다.

---

## 5. 조건문 `if`

기본 구조:

```python
if 조건:
    조건이 참일 때 실행
elif 다른조건:
    앞 조건이 거짓이고 다른조건이 참일 때 실행
else:
    모든 조건이 거짓일 때 실행
```

예시:

```python
score = 90

if score >= 90:
    print("A")
elif score >= 80:
    print("B")
else:
    print("F")
```

### 비교 연산자

| 연산자 | 의미 |
|---|---|
| `==` | 같다 |
| `!=` | 같지 않다 |
| `>` | 크다 |
| `<` | 작다 |
| `>=` | 크거나 같다 |
| `<=` | 작거나 같다 |

### 논리 연산자

| 연산자 | 의미 |
|---|---|
| `and` | 둘 다 참이면 참 |
| `or` | 둘 중 하나라도 참이면 참 |
| `not` | 참/거짓 반전 |

### 윤년 판별 예제

```python
year = int(input("연도를 입력하세요: "))

if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
    print(f"{year}년은 윤년입니다.")
else:
    print(f"{year}년은 윤년이 아닙니다.")
```

핵심:

```python
%
```

`%`는 나머지를 구하는 연산자입니다.

---

## 6. 반복문 `while`

`while`은 조건이 참인 동안 반복합니다.

```python
treeHit = 0

while treeHit < 10:
    treeHit += 1
    print("나무를 %d번 찍었습니다." % treeHit)

    if treeHit == 10:
        print("나무 넘어갑니다.")
```

흐름:

```text
treeHit = 0
조건 검사: treeHit < 10
참이면 반복문 내부 실행
treeHit += 1
다시 조건 검사
```

주의:

```python
print("나무를 %d번 찍었습니다." % treeHit)
```

이 코드가 `while` 밖에 있으면 반복이 끝난 뒤 한 번 더 출력됩니다.

### `break`

반복문을 강제로 끝냅니다.

```python
coffee = 10

while True:
    money = int(input("돈을 넣어 주세요: "))

    if money == 300:
        print("커피를 줍니다.")
        coffee -= 1

    if coffee == 0:
        print("커피가 다 떨어졌습니다.")
        break
```

### `continue`

아래 코드를 건너뛰고 다음 반복으로 넘어갑니다.

```python
a = 0

while a < 10:
    a += 1
    if a % 2 == 0:
        continue
    print(a)
```

출력:

```text
1
3
5
7
9
```

---

## 7. 반복문 `for`

`for`는 리스트, 문자열, `range()` 같은 반복 가능한 객체를 하나씩 꺼내면서 반복합니다.

```python
for i in ["고", "저", "장", "단", "쉼"]:
    print(i, end=" ")
```

출력:

```text
고 저 장 단 쉼
```

### `range()`

```python
for i in range(1, 11):
    print(i)
```

| 코드 | 의미 |
|---|---|
| `range(10)` | 0부터 9까지 |
| `range(1, 11)` | 1부터 10까지 |
| `range(1, 11, 2)` | 1부터 10까지 2씩 증가 |
| `range(10, 0, -1)` | 10부터 1까지 감소 |

### 합계 구하기

```python
s = 0

for i in range(1, 101):
    s += i

print(s)  # 5050
```

### 조건과 반복 같이 쓰기

```python
s = 0

for i in range(1, 101):
    if i % 2 == 1:
        s += i

print(s)  # 2500
```

---

## 8. 중첩 반복문

반복문 안에 반복문이 들어갈 수 있습니다.

```python
i = 2

while i <= 3:
    j = 1
    while j <= 9:
        print(f"{i:3} x {j:3} = {i*j:3}")
        j += 1
    i += 1
```

바깥 반복문은 단을 담당하고, 안쪽 반복문은 1부터 9까지의 곱을 담당합니다.

---

## 9. 별 찍기 패턴

### 9-1. 기본 직각삼각형

```python
n = 5

for i in range(1, n + 1):
    for j in range(i):
        print("*", end=" ")
    print()
```

### 9-2. 반대 방향 직각삼각형

```python
n = 5

for i in range(1, n + 1):
    for j in range(n - i):
        print(" ", end=" ")

    for j in range(i):
        print("*", end=" ")

    print()
```

### 9-3. 정삼각형

```python
n = 5

for i in range(1, n + 1):
    for j in range(n - i):
        print(" ", end=" ")

    for j in range(2 * i - 1):
        print("*", end=" ")

    print()
```

핵심 공식:

| 모양 | 공백 개수 | 별 개수 |
|---|---|---|
| 직각삼각형 | 없음 | `i` |
| 반대 직각삼각형 | `n - i` | `i` |
| 정삼각형 | `n - i` | `2 * i - 1` |
| 마름모 위쪽 | `n - i` | `2 * i - 1` |
| 마름모 아래쪽 | `n - i` | `2 * i - 1`, 단 `i`를 감소 |

### 9-4. 마름모

```python
n = 5

# 위쪽
for i in range(1, n + 1):
    for j in range(n - i):
        print(" ", end=" ")

    for j in range(2 * i - 1):
        print("*", end=" ")

    print()

# 아래쪽
for i in range(n - 1, 0, -1):
    for j in range(n - i):
        print(" ", end=" ")

    for j in range(2 * i - 1):
        print("*", end=" ")

    print()
```

---

## 10. 함수

함수는 자주 쓰는 코드를 이름 붙여 재사용하는 문법입니다.

```python
def add(a, b):
    return a + b

result = add(3, 4)
print(result)
```

구조:

```python
def 함수이름(매개변수):
    실행할 코드
    return 결과값
```

| 용어 | 의미 |
|---|---|
| 함수 | 기능을 묶어 둔 코드 |
| 매개변수 | 함수가 값을 받을 때 쓰는 변수 |
| 인수 | 함수를 호출할 때 실제로 넣는 값 |
| `return` | 함수 결과를 밖으로 돌려줌 |

### 여러 개의 입력값 받기: `*args`

```python
def addMany(*args):
    result = 0
    for i in args:
        result += i
    return result

print(addMany(1, 2, 3, 4, 5))
```

`*args`는 여러 개의 값을 튜플처럼 받습니다.

### 키워드 입력값 받기: `**kwargs`

```python
def print_kwargs(**kwargs):
    print(kwargs)

print_kwargs(name="홍길동", age=25)
```

출력:

```text
{'name': '홍길동', 'age': 25}
```

`**kwargs`는 key-value 형태의 값을 딕셔너리처럼 받습니다.

### 여러 결과 반환

```python
def add_and_mul(a, b):
    return a + b, a * b

result = add_and_mul(3, 4)
print(result)  # (7, 12)
```

Python 함수는 여러 값을 반환하면 튜플로 묶어서 반환합니다.

---

## 11. 변수의 범위: 지역 변수와 전역 변수

함수 안에서 만든 변수는 기본적으로 함수 안에서만 의미가 있습니다.

```python
a = 1

def vartest(a):
    a = a + 1
    return a

a = vartest(a)
print(a)
```

`global`을 쓰면 함수 안에서 바깥 변수를 직접 바꿀 수 있습니다.

```python
a = 1

def vartest():
    global a
    a = a + 1

vartest()
print(a)
```

하지만 복습 기준으로는 `global`보다 `return`으로 값을 돌려받는 방식을 먼저 익히는 것이 좋습니다.

---

## 12. 독스트링

독스트링은 함수 설명문입니다.

```python
def add(a, b):
    """
    두 숫자를 더하는 함수

    Parameters:
    a: 첫 번째 숫자
    b: 두 번째 숫자

    Returns:
    두 숫자의 합
    """
    return a + b

print(add.__doc__)
print(add.__name__)
```

| 코드 | 의미 |
|---|---|
| `함수.__doc__` | 함수 설명문 확인 |
| `함수.__name__` | 함수 이름 확인 |

---

## 13. `match case`

`match case`는 여러 경우 중 하나를 선택할 때 사용합니다.

```python
choice = input("Enter choice (1/2/3/4): ")

match choice:
    case '1':
        print("Add")
    case '2':
        print("Subtract")
    case '3':
        print("Multiply")
    case '4':
        print("Divide")
    case _:
        print("Invalid input")
```

`case _:`는 `if-elif-else`의 `else`와 비슷합니다.

계산기 예시:

```python
def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def multiply(a, b):
    return a * b

def divide(a, b):
    if b == 0:
        return "Error: Division by zero"
    return a / b

choice = input("Enter choice (1/2/3/4): ")
num1 = float(input("Enter first number: "))
num2 = float(input("Enter second number: "))

match choice:
    case '1':
        print(add(num1, num2))
    case '2':
        print(subtract(num1, num2))
    case '3':
        print(multiply(num1, num2))
    case '4':
        print(divide(num1, num2))
    case _:
        print("Invalid input")
```

---

## 14. 파일 입출력

파일을 만들거나 쓰려면 `open()`을 사용합니다.

```python
f = open("새파일.txt", "w", encoding="utf-8")
f.write("안녕하세요, 파이썬!")
f.close()
```

| 모드 | 의미 |
|---|---|
| `"w"` | 쓰기 모드. 기존 내용은 덮어씀 |
| `"r"` | 읽기 모드 |
| `"a"` | 추가 모드. 기존 내용 뒤에 추가 |

### `encoding="utf-8"`

UTF-8은 글자를 파일에 저장할 때 쓰는 문자 인코딩 방식입니다.

한글을 파일에 저장하거나 읽을 때는 다음처럼 쓰는 것이 안전합니다.

```python
f = open("새파일.txt", "w", encoding="utf-8")
f.write("안녕하세요")
f.close()
```

읽기:

```python
f = open("새파일.txt", "r", encoding="utf-8")
data = f.read()
f.close()

print(data)
```

### 폴더가 없을 때 자동 생성

```python
import os

os.makedirs("C:/doit", exist_ok=True)

f = open("C:/doit/새파일.txt", "w", encoding="utf-8")
f.close()
```

`exist_ok=True`는 폴더가 이미 있어도 에러가 나지 않게 합니다.

---

## 15. 프로그램의 입출력: `sys.argv`

`sys.argv`는 터미널에서 파이썬 파일을 실행할 때 같이 넘긴 값을 코드 안에서 받는 방법입니다.

```python
# sys1.py
import sys

args = sys.argv[1:]

for i in args:
    print(i)
```

실행:

```powershell
python sys1.py hello python 123
```

출력:

```text
hello
python
123
```

핵심:

| 코드 | 의미 |
|---|---|
| `sys.argv[0]` | 실행한 파일 이름 |
| `sys.argv[1]` | 첫 번째 인자 |
| `sys.argv[1:]` | 파일 이름을 제외한 나머지 인자 전체 |

### 인자 개수 세기

```python
# sys_count.py
import sys

args = sys.argv[1:]

print("입력한 값들:", args)
print("입력한 개수:", len(args))
```

### 숫자 합계 구하기

```python
# sum_args.py
import sys

args = sys.argv[1:]

total = 0

for i in args:
    total += int(i)

print("합계:", total)
```

실행:

```powershell
python sum_args.py 10 20 30
```

출력:

```text
합계: 60
```

`sys.argv`로 들어오는 값은 문자열이므로 숫자 계산을 하려면 `int()` 또는 `float()`로 바꿔야 합니다.

---

## 16. 에러 유형

| 에러 유형 | 의미 | 예시 |
|---|---|---|
| Syntax Error | 문법 자체가 틀림 | 괄호 빠짐, 이상한 문자 입력 |
| Runtime Error | 실행 중 문제 발생 | 0으로 나누기, 잘못된 형변환 |
| Semantic Error | 실행은 되지만 의도와 다른 결과 | 연산자 잘못 사용 |

### 전각 문자 오류

```python
print("*", end=" ")１２３
```

이런 식으로 코드 뒤에 전각 숫자나 전각 영어가 들어가면 오류가 납니다.

정상:

```python
print("*", end=" ")
```

코딩할 때는 입력 상태가 `Ａ`가 아니라 `A`인지 확인하는 것이 좋습니다.

---

## 17. VS Code 디버깅 기본

반복문이 한 번에 끝나는 것이 아니라 한 줄씩 보고 싶으면 브레이크포인트를 사용합니다.

| 키 | 의미 |
|---|---|
| `F5` | 디버그 시작 / 다음 브레이크포인트까지 실행 |
| `F10` | 한 줄씩 실행 |
| `F11` | 함수 안으로 들어가기 |
| `Shift + F5` | 디버그 종료 |

반복문 디버깅 예시:

```python
treeHit = 0

while treeHit < 10:
    treeHit += 1
    print("나무를 %d번 찍었습니다." % treeHit)
```

`treeHit += 1` 줄 왼쪽에 빨간 점을 찍고 `F5`를 누른 뒤 `F10`으로 한 줄씩 보면 `treeHit` 값이 `0 -> 1 -> 2 ...`로 바뀌는 것을 볼 수 있습니다.

---

# 시험 전 체크리스트

## 반드시 설명할 수 있어야 하는 것

- `input()`으로 받은 값이 왜 문자열인지
- `int()`와 `float()`를 언제 쓰는지
- 리스트와 튜플의 차이
- 리스트 인덱스가 왜 0부터 시작하는지
- `if`, `elif`, `else`의 실행 순서
- `while`과 `for`의 차이
- `break`와 `continue`의 차이
- `range(1, 10)`이 왜 1부터 9까지인지
- 중첩 반복문에서 바깥 반복문과 안쪽 반복문의 역할
- 함수에서 `return`이 하는 일
- `*args`와 `**kwargs`의 차이
- 지역 변수와 전역 변수의 차이
- 파일 열기 모드 `w`, `r`, `a`의 차이
- `encoding="utf-8"`을 쓰는 이유
- `sys.argv[1:]`가 의미하는 것

## 손코딩으로 연습할 문제

1. 숫자 5개를 입력받아 합계와 평균 출력하기
2. 점수를 입력받아 A/B/C/F 학점 출력하기
3. 1부터 100까지 합 구하기
4. 1부터 100까지 홀수의 합 구하기
5. 6의 배수만 더하기
6. 구구단 2단부터 9단까지 출력하기
7. 별로 직각삼각형 출력하기
8. 별로 정삼각형 출력하기
9. `add`, `subtract`, `multiply`, `divide` 함수로 계산기 만들기
10. `sys.argv`로 숫자를 받아 합계 출력하기

---

## 한 줄 요약

지금까지 배운 흐름은 다음과 같습니다.

```text
값 입력 -> 자료형 변환 -> 조건 판단 -> 반복 처리 -> 함수로 묶기 -> 파일/터미널과 입출력하기
```

이 흐름을 이해하면 점프 투 파이썬 04장까지의 핵심은 거의 잡은 것입니다.
