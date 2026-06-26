# mycodehouse

Python 수업에서 배운 기초 문법과 실습 코드를 정리하는 저장소입니다.

## 학습 기록

### 2026-06-26: Python 기초 문법

오늘은 Python의 기본 입력 처리, 문자열 포매팅, 리스트 사용법, 컨테이너 자료형, 조건문 `if`를 실습했습니다.

## 실습 파일

| 파일 | 내용 |
|---|---|
| `0626/stringEx.py` | 사용자 입력, 정수 변환, 사칙연산, f-string 출력 |
| `0626/1.py` | 리스트 생성, 반복 입력, `append()`, 평균/합계/최솟값/최댓값 계산 |
| `0626/2.py` | 문자열 리스트 입력, 리스트 출력, 인덱싱 실습 |

---

## 1. 입력과 형변환

`input()` 함수로 사용자 입력을 받을 수 있습니다.

단, `input()`으로 받은 값은 기본적으로 문자열이기 때문에 숫자 계산을 하려면 `int()`를 사용해 정수로 변환해야 합니다.

```python
a = int(input("Enter first number: "))
b = int(input("Enter second number: "))

print(f"You entered: {a} and {b}")
print(f"a + b = {a + b}")
print(f"a - b = {a - b}")
print(f"a * b = {a * b}")
print(f"a / b = {a / b}")
```

## 2. 문자열 포매팅

출력문 안에 변수나 값을 넣기 위해 f-string을 사용했습니다.

```python
print(f"a + b = {a + b}")
```

f-string은 문자열 앞에 `f`를 붙이고, `{}` 안에 변수나 계산식을 넣는 방식입니다.

기존 방식인 `%` 포매팅과 `.format()`도 사용할 수 있지만, 요즘 Python에서는 f-string이 가장 직관적이고 많이 사용됩니다.

```python
print("I eat %d apples and %d oranges." % (3, 5))
print("I eat {0} apples and {1} oranges".format(3, 5))
print(f"I eat {3} apples and {5} oranges")
```

## 3. 리스트와 반복문

여러 개의 값을 저장하기 위해 리스트를 사용했습니다.

```python
y = []

for i in range(5):
    a = int(input("5개의 정수값을 입력하시오: "))
    y.append(a)
```

`append()`는 리스트의 마지막에 값을 추가하는 함수입니다.

`for i in range(5)`는 같은 동작을 5번 반복한다는 의미입니다.

## 4. 리스트 내장 함수

입력받은 숫자 리스트를 이용해 합계, 평균, 최솟값, 최댓값을 계산했습니다.

```python
print(f"mean = {sum(y) / len(y)}, sum = {sum(y)}, min = {min(y)}, max = {max(y)}")
```

사용한 함수는 다음과 같습니다.

| 함수 | 의미 |
|---|---|
| `sum()` | 리스트 안의 값들의 합 |
| `len()` | 리스트의 길이 |
| `min()` | 리스트 안의 최솟값 |
| `max()` | 리스트 안의 최댓값 |

평균은 다음과 같이 계산할 수 있습니다.

```python
mean = sum(y) / len(y)
```

## 5. 리스트 인덱싱

리스트에 저장된 값은 인덱스를 이용해 꺼낼 수 있습니다.

```python
fruits = []

for i in range(5):
    fruit = input("enter a fruit: ")
    fruits.append(fruit)

print(fruits)
print(fruits[-1])
print(fruits[3])
```

`fruits[-1]`은 리스트의 마지막 요소를 의미합니다.

`fruits[3]`은 네 번째 요소를 의미합니다. Python의 인덱스는 0부터 시작하기 때문입니다.

예를 들어 리스트가 다음과 같다면,

```python
fruits = ["apple", "banana", "orange", "melon", "grape"]
```

인덱스는 다음과 같이 대응됩니다.

| 값 | 인덱스 |
|---|---|
| `"apple"` | `0` |
| `"banana"` | `1` |
| `"orange"` | `2` |
| `"melon"` | `3` |
| `"grape"` | `4` 또는 `-1` |

---

## 6. 컨테이너 자료형

컨테이너 자료형은 여러 데이터를 하나의 변수에 담아 관리하는 자료형입니다.

Python에서 자주 사용하는 컨테이너 자료형은 다음과 같습니다.

| 자료형 | 예시 | 특징 |
|---|---|---|
| 리스트 `list` | `[1, 2, 5, 8]` | 순서가 있고 값 변경 가능 |
| 튜플 `tuple` | `(1, 2)` | 순서가 있고 값 변경 불가 |
| 세트 `set` | `{'h', 'e', 'l', 'o'}` | 중복을 허용하지 않고 순서가 고정되지 않음 |
| 딕셔너리 `dict` | `{1: 'a', 2: 'b'}` | key와 value를 한 쌍으로 저장 |

### 리스트 예시

```python
numbers = [1, 2, 5, 8]
print(numbers)
print(sorted(numbers, reverse=True))
```

출력 예시:

```text
[1, 2, 5, 8]
[8, 5, 2, 1]
```

리스트는 순서가 있으므로 정렬하거나 인덱스로 접근할 수 있습니다.

### 세트 예시

```python
text = "hello"
print(set(text))
```

출력 예시:

```text
{'e', 'h', 'l', 'o'}
```

`hello`에는 `l`이 두 번 들어 있지만, 세트는 중복을 제거하므로 `l`이 한 번만 저장됩니다.

### 딕셔너리 예시

```python
data = {
    1: "a",
    2: "b",
    (1, 2): "c"
}

print(data)
```

출력 예시:

```text
{1: 'a', 2: 'b', (1, 2): 'c'}
```

딕셔너리는 `key: value` 형태로 데이터를 저장합니다.

튜플 `(1, 2)`은 값을 바꿀 수 없기 때문에 딕셔너리의 key로 사용할 수 있습니다.

반대로 리스트는 값이 바뀔 수 있으므로 딕셔너리의 key로 사용할 수 없습니다.

---

## 7. Python 예약어

Python에는 이미 문법적으로 정해진 단어들이 있습니다.

이런 단어를 예약어 또는 키워드라고 합니다.

```python
import keyword

print(keyword.kwlist)
```

출력 예시:

```text
['False', 'None', 'True', 'and', 'as', 'assert', 'async', 'await', 'break',
 'class', 'continue', 'def', 'del', 'elif', 'else', 'except', 'finally',
 'for', 'from', 'global', 'if', 'import', 'in', 'is', 'lambda', 'nonlocal',
 'not', 'or', 'pass', 'raise', 'return', 'try', 'while', 'with', 'yield']
```

예약어는 변수 이름으로 사용할 수 없습니다.

예를 들어 `if`, `for`, `while`, `class` 같은 단어는 Python 문법에서 이미 사용 중이기 때문입니다.

---

## 8. 조건문 if

조건문은 특정 조건이 참인지 거짓인지에 따라 실행할 코드를 나누는 문법입니다.

기본 구조는 다음과 같습니다.

```python
if 조건:
    조건이 참일 때 실행할 코드
else:
    조건이 거짓일 때 실행할 코드
```

예시:

```python
weather = "rain"

if weather == "rain":
    print("ㅠㅠ walk")
else:
    print("Good")
```

출력 예시:

```text
ㅠㅠ walk
```

## 9. if - else 예시

조건에 따라 서로 다른 문장을 출력할 수 있습니다.

```python
time = "night"

if time == "night":
    print("Good night")
else:
    print("Good morning")
```

출력 예시:

```text
Good night
```

---

## 10. 나이 조건문

나이에 따라 성인 여부를 판단할 수 있습니다.

```python
age = 20

if age >= 20:
    print("성인")
else:
    print("미성년자")
```

출력 예시:

```text
성인
```

여기서 사용한 비교 연산자는 `>=`입니다.

`age >= 20`은 age가 20 이상이면 참이 됩니다.

---

## 11. 교통수단 조건문

조건에 따라 이동 방법을 출력할 수 있습니다.

```python
money = 0

if money >= 1500:
    print("버스타기")
else:
    print("걸어가")
```

출력 예시:

```text
걸어가
```

조건문은 상황에 따라 프로그램의 흐름을 바꿀 때 사용합니다.

---

## 12. 학점 조건문

점수에 따라 학점을 출력할 수 있습니다.

```python
score = 90

if score >= 90:
    print("A")
elif score >= 80:
    print("B")
elif score >= 70:
    print("C")
else:
    print("F")
```

출력 예시:

```text
A
```

`elif`는 이전 조건이 거짓일 때 다음 조건을 검사하는 문법입니다.

여러 조건을 순서대로 검사할 때 사용합니다.

---

## 13. 윤년 판별

윤년은 다음 조건으로 판별할 수 있습니다.

- 연도가 4로 나누어떨어지면 윤년 가능성이 있습니다.
- 하지만 100으로 나누어떨어지면 평년입니다.
- 단, 400으로 나누어떨어지면 윤년입니다.

조건식으로 쓰면 다음과 같습니다.

```python
year = int(input("연도를 입력하세요: "))

if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
    print(f"{year}년은 윤년입니다.")
else:
    print(f"{year}년은 윤년이 아닙니다.")
```

출력 예시:

```text
4351454561354652465786765424년은 윤년입니다.
```

입력한 수가 매우 크더라도 Python의 정수형은 큰 수를 처리할 수 있기 때문에 계산이 가능합니다.

---

## 14. 오늘 배운 핵심 정리

| 개념 | 설명 |
|---|---|
| `input()` | 사용자 입력을 받는 함수 |
| `int()` | 문자열을 정수로 변환하는 함수 |
| f-string | 문자열 안에 변수나 계산식을 넣는 출력 방식 |
| 리스트 | 여러 값을 순서대로 저장하는 자료형 |
| 튜플 | 값을 바꿀 수 없는 자료형 |
| 세트 | 중복을 허용하지 않는 자료형 |
| 딕셔너리 | key와 value를 한 쌍으로 저장하는 자료형 |
| 예약어 | Python 문법에서 이미 정해진 단어 |
| 조건문 | 조건에 따라 실행 흐름을 바꾸는 문법 |
| `if` | 조건이 참일 때 실행 |
| `elif` | 앞 조건이 거짓일 때 다음 조건 검사 |
| `else` | 모든 조건이 거짓일 때 실행 |
| `%` | 나머지를 구하는 연산자 |
| `and` | 두 조건이 모두 참일 때 참 |
| `or` | 둘 중 하나라도 참이면 참 |
| `!=` | 같지 않다는 의미 |

---

## 정리

오늘은 Python에서 사용자 입력을 받고, 입력값을 정수로 변환한 뒤, 사칙연산을 수행하는 방법을 배웠습니다.

또한 리스트를 사용해 여러 개의 데이터를 저장하고, 반복문과 내장 함수를 활용해 데이터를 처리하는 기본 흐름을 익혔습니다.

추가로 리스트, 튜플, 세트, 딕셔너리 같은 컨테이너 자료형의 차이를 배웠고, `if`, `elif`, `else` 조건문을 통해 상황에 따라 프로그램의 흐름을 바꾸는 방법을 연습했습니다.

특히 윤년 판별 예제를 통해 비교 연산자, 논리 연산자, 나머지 연산자 `%`를 함께 사용하는 방법을 익혔습니다.
