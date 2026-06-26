# mycodehouse

Python 수업에서 배운 기초 문법과 실습 코드를 정리하는 저장소입니다.

## 2026-06-26 학습 내용

오늘은 Python의 기본 입력 처리, 문자열 포매팅, 리스트 사용법을 실습했습니다.

## 실습 파일

| 파일 | 내용 |
|---|---|
| `0626/stringEx.py` | 사용자 입력, 정수 변환, 사칙연산, f-string 출력 |
| `0626/1.py` | 리스트 생성, 반복 입력, `append()`, 평균/합계/최솟값/최댓값 계산 |
| `0626/2.py` | 문자열 리스트 입력, 리스트 출력, 인덱싱 실습 |

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

## 정리

오늘은 Python에서 사용자 입력을 받고, 입력값을 정수로 변환한 뒤, 사칙연산을 수행하는 방법을 배웠습니다.

또한 리스트를 사용해 여러 개의 데이터를 저장하고, 반복문과 내장 함수를 활용해 데이터를 처리하는 기본 흐름을 익혔습니다.

이번 실습을 통해 다음 내용을 익혔습니다.

- `input()`으로 사용자 입력 받기
- `int()`로 문자열을 정수로 변환하기
- f-string으로 출력문 작성하기
- 리스트 생성과 `append()` 사용하기
- `for` 반복문 사용하기
- `sum()`, `len()`, `min()`, `max()` 활용하기
- 리스트 인덱싱과 음수 인덱싱 이해하기
