# 2026-06-29 제어문, 함수, 파일/터미널 입출력 실습

이 폴더는 Python의 흐름 제어와 함수 사용을 본격적으로 연습한 날짜별 기록입니다.

단순 계산 코드에서 한 단계 넘어가서 `while`, `for`, `break`, `continue`, 함수, 가변 인수, 키워드 인수, 파일 생성, 터미널 인자 처리까지 실습했습니다.

---

## 파일 구성

| 파일 | 배운 내용 |
|---|---|
| `1.ipynb` | 조건식, 논리 연산자, `while`, `break`, `continue`, 입력 오류, 에러 유형 정리 |
| `2.ipynb` | 함수형 계산기, `return`, `*args`, `**kwargs`, 딕셔너리 순회, 튜플 반환, 지역/전역 변수, 독스트링, 파일 생성 |
| `34.py` | `while`문을 이용한 나무 찍기 예제 |
| `sys1.py` | `sys.argv`로 터미널 인자 받아 출력 |
| `sys2.py` | 터미널 인자를 대문자로 변환하여 출력 |
| `sys_count.py` | 터미널 인자 목록과 개수 출력 |
| `sum_args.py` | 터미널 인자로 받은 숫자들을 정수 변환 후 합계 계산 |

---

## 1. 조건식과 논리 연산자

`1.ipynb`에서는 조건문에서 사용하는 비교 연산자와 논리 연산자를 정리했습니다.

```text
<, <=, >=, >, ==, !=, in, not, is, is not
not, and, or
```

조건문은 프로그램이 상황에 따라 다른 코드를 실행하게 해줍니다.

```python
if 조건:
    실행할 코드
else:
    다른 코드
```

---

## 2. while 반복문

`while`은 조건이 참인 동안 계속 반복합니다.

```python
treeHit = 0
while treeHit < 10:
    treeHit += 1
    print("나무를 %d번 찍었습니다." % treeHit)
    if treeHit == 10:
        print("나무 넘어갑니다.")
```

중요한 점은 반복 조건을 바꿔주는 코드가 반드시 필요하다는 것입니다.

```python
treeHit += 1
```

이런 증가 코드가 없으면 무한 반복에 빠질 수 있습니다.

---

## 3. break와 continue

### break

`break`는 반복문을 즉시 종료합니다.

```python
if coffee == 0:
    print("커피가 다 떨어졌습니다. 판매를 중지 합니다.")
    break
```

### continue

`continue`는 아래 코드를 건너뛰고 다음 반복으로 넘어갑니다.

```python
a = 0
while a < 10:
    a = a + 1
    if a % 2 == 0:
        continue
    print(a)
```

이 코드는 홀수만 출력합니다.

```text
1
3
5
7
9
```

---

## 4. 에러 유형 정리

실습 중 에러도 같이 정리했습니다.

| 에러 유형 | 의미 | 예시 |
|---|---|---|
| Syntax Error | 문법 자체가 틀림 | 괄호 누락, 콜론 누락, 잘못된 기호 |
| Runtime Error | 실행 중 문제 발생 | 빈 문자열을 `int()`로 변환, 0으로 나누기 |
| Semantic Error | 실행은 되지만 의도와 다름 | 들여쓰기 위치 오류, 연산자 선택 오류 |

예를 들어 `int(input())`에서 아무것도 입력하지 않고 엔터를 치면 `ValueError`가 발생할 수 있습니다.

---

## 5. 함수로 계산기 만들기

`2.ipynb`에서는 사칙연산을 함수로 분리했습니다.

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
```

여기서 중요한 점은 나누기 함수에서 0으로 나누는 경우를 따로 처리했다는 것입니다.

```python
if b == 0:
    return "Error: Division by zero"
```

---

## 6. match case

여러 선택지 중 하나를 고르는 구조로 `match case`를 사용했습니다.

```python
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

`case _:`는 `if-elif-else`에서 `else`와 비슷한 역할입니다.

---

## 7. 가변 인수 `*args`

`*args`는 함수에 들어오는 여러 값을 튜플처럼 받을 때 사용합니다.

```python
def addMany(*args):
    result = 0
    for i in args:
        result += i
    return result
```

호출할 때 인수 개수가 달라도 처리할 수 있습니다.

```python
print(addMany(1, 2))
print(addMany(1, 2, 3, 4, 5))
```

---

## 8. 키워드 인수 `**kwargs`

`**kwargs`는 key-value 형태의 값을 딕셔너리처럼 받습니다.

```python
def print_kwargs(**kwargs):
    print(kwargs)
```

```python
print_kwargs(name='홍길동', age=25, city='서울', job='개발자')
```

딕셔너리 순회도 함께 연습했습니다.

```python
for key in dict1:
    print(f"{key}: {dict1[key]}")
```

---

## 9. 여러 값 반환하기

Python 함수는 여러 값을 반환하면 튜플 형태로 묶어서 돌려줍니다.

```python
def add_and_mul(a, b):
    return a + b, a * b

result = add_and_mul(3, 4)
```

결과:

```text
(7, 12)
```

---

## 10. 지역 변수, 전역 변수, global

함수 안에서 만든 변수는 기본적으로 함수 안에서만 의미가 있습니다.

```python
a = 1

def vartest(a):
    a = a + 1
    return a

a = vartest(a)
print(a)
```

전역 변수를 함수 안에서 직접 바꾸려면 `global`을 사용할 수 있습니다.

```python
a = 1

def vartest():
    global a
    a = a + 1

vartest()
print(a)
```

다만 복습 기준으로는 `global`보다 `return`으로 값을 돌려받는 방식을 먼저 익히는 것이 좋습니다.

---

## 11. 독스트링

독스트링은 함수 설명문입니다.

```python
def add(a, b):
    """
    두 숫자를 더하는 함수

    Parameters:
    a (int, float): 첫 번째 숫자
    b (int, float): 두 번째 숫자

    Returns:
    int, float: 두 숫자의 합
    """
    return a + b
```

확인 방법:

```python
print(add.__doc__)
print(add.__name__)
```

---

## 12. 파일 생성

`open()`을 이용해 새 파일을 만드는 실습을 했습니다.

```python
f = open("새파일.txt", "w")
f.close()
```

폴더가 없을 때는 `os.makedirs()`로 먼저 만들 수 있습니다.

```python
import os

os.makedirs("C:/doit", exist_ok=True)
f = open("C:/doit/새파일.txt", "w")
f.close()
```

---

## 13. 터미널 인자 `sys.argv`

`sys.argv`는 터미널에서 Python 파일을 실행할 때 뒤에 붙인 값을 코드 안에서 받는 방법입니다.

```python
import sys

args = sys.argv[1:]
for i in args:
    print(i)
```

### 관련 파일

| 파일 | 실행 예시 | 설명 |
|---|---|---|
| `sys1.py` | `python 0629/sys1.py hello python` | 인자를 그대로 출력 |
| `sys2.py` | `python 0629/sys2.py hello python` | 인자를 대문자로 출력 |
| `sys_count.py` | `python 0629/sys_count.py a b c` | 인자 목록과 개수 출력 |
| `sum_args.py` | `python 0629/sum_args.py 10 20 30` | 숫자 인자의 합계 출력 |

`sys.argv`로 들어오는 값은 문자열이므로 숫자로 계산하려면 `int()` 또는 `float()`로 바꿔야 합니다.

---

## 오늘 배운 핵심

- `while`은 조건이 참인 동안 반복한다.
- 반복 조건을 바꾸지 않으면 무한 루프가 될 수 있다.
- `break`는 반복문 종료, `continue`는 다음 반복으로 이동이다.
- 함수는 반복되는 코드를 이름 붙여 재사용하는 방법이다.
- `return`은 함수의 결과를 밖으로 돌려준다.
- `*args`는 여러 인수를 튜플처럼 받는다.
- `**kwargs`는 키워드 인수를 딕셔너리처럼 받는다.
- 여러 값을 반환하면 튜플로 묶인다.
- 함수 설명은 독스트링으로 남길 수 있다.
- `sys.argv`를 사용하면 터미널 입력값을 코드로 받을 수 있다.
- 파일은 `open()`으로 만들거나 열 수 있다.

---

## 추가로 연습하면 좋은 문제

1. 숫자를 계속 입력받다가 0을 입력하면 종료하고 합계 출력하기
2. 1부터 100까지 홀수만 출력하기
3. `add`, `sub`, `mul`, `div` 함수로 계산기 만들기
4. `*args`를 이용해 입력된 숫자들의 평균 구하기
5. `**kwargs`를 이용해 학생 프로필 출력하기
6. `sys.argv`로 이름을 받아 인사말 출력하기
7. 터미널 인자로 받은 숫자 중 최댓값 출력하기
8. 파일을 생성하고 문자열을 저장한 뒤 다시 읽어오기

---

## 한 줄 요약

2026-06-29에는 조건과 반복으로 프로그램의 흐름을 제어하고, 함수를 이용해 코드를 구조화하며, 터미널과 파일을 통해 프로그램 바깥과 데이터를 주고받는 방법을 연습했습니다.
