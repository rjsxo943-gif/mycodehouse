# mycodehouse

Python 수업과 부트캠프 실습 코드를 날짜별로 정리하는 개인 학습 저장소입니다.

기초 문법을 단순히 따라 치는 것에서 끝내지 않고, 입력/출력, 조건문, 반복문, 함수, 자료구조, 객체지향, 간단한 GUI 프로그램까지 직접 실습한 내용을 모아두는 용도입니다.

---

## 현재 학습 흐름

```text
값 입력 → 자료형 변환 → 조건 판단 → 반복 처리 → 함수로 분리 → 파일/터미널 입출력 → 객체/클래스 → GUI 실습
```

| 날짜 | 학습 범위 | 핵심 키워드 |
|---|---|---|
| 2026-06-26 | Python 기초 문법 | `input`, `int`, `float`, `str`, f-string, 리스트, 인덱싱, 합계/평균 |
| 2026-06-29 | 제어문과 함수 | `if`, `while`, `for`, `break`, `continue`, 중첩 반복문, 함수, `*args`, `**kwargs`, `match case`, 파일 입출력, `sys.argv` |
| 2026-07-06 | 객체지향과 GUI | 클래스, 인스턴스 변수, 클래스 변수, `__init__`, `__str__`, `tkinter`, 메모장, 그림판, `numpy` 배열 |

---

## 폴더 / 파일 구성

| 경로 | 내용 |
|---|---|
| `0622/` | 초기 Python 실습 파일 |
| `0626/stringEx.py` | 정수 입력, 형변환, 사칙연산, f-string 출력 |
| `0626/1.py` | 정수 5개 입력, 리스트 저장, 합계/평균/최솟값/최댓값 계산 |
| `0626/2.py` | 문자열 리스트 입력, 리스트 출력, 음수 인덱싱 실습 |
| `0629/1.ipynb` | `while`, `break`, `continue`, 반복문 흐름, 입력 오류, 에러 유형 정리 |
| `0629/2.ipynb` | 함수형 계산기, `return`, `*args`, `**kwargs`, `match case`, 함수 실습 |
| `0629/34.py` | `while`문을 이용한 나무 찍기 예제 |
| `0629/sys1.py` | 터미널 인자 `sys.argv` 기본 출력 |
| `0629/sys2.py` | 터미널 인자를 대문자로 변환해 출력 |
| `0629/sys_count.py` | 터미널 인자 개수 세기 |
| `0629/sum_args.py` | 터미널 인자로 받은 숫자들의 합계 계산 |
| `0706/1.ipynb` | `Television` 클래스로 객체 생성, 클래스 변수, 메소드, 문자열 표현 실습 |
| `0706/2.ipynb` | `tkinter` 기반 메모장/그림판 GUI 실습, `numpy` 배열 기초 |
| `command.md` | 자주 쓰는 터미널 명령어 정리 |
| `requirements.txt` | Python 패키지 목록 정리용 파일 |

---

## 주요 실습 내용

### 1. 입력과 형변환

`input()`으로 받은 값은 문자열이므로 숫자 계산을 하려면 `int()` 또는 `float()`로 변환해야 합니다.

```python
a = int(input("Enter first number: "))
b = int(input("Enter second number: "))

print(f"a + b = {a + b}")
print(f"a - b = {a - b}")
print(f"a * b = {a * b}")
print(f"a / b = {a / b}")
```

### 2. 리스트와 기본 통계

리스트에 값을 추가하고, `sum`, `len`, `min`, `max`를 이용해 기본 통계를 계산했습니다.

```python
numbers = []

for i in range(5):
    value = int(input("5개의 정수값을 입력하시오: "))
    numbers.append(value)

print(numbers)
print(f"mean = {sum(numbers) / len(numbers)}")
print(f"sum = {sum(numbers)}")
print(f"min = {min(numbers)}")
print(f"max = {max(numbers)}")
```

### 3. 조건문과 반복문

`if`, `while`, `for`를 사용해서 프로그램 흐름을 제어하는 연습을 했습니다.

```python
a = 0

while a < 10:
    a += 1
    if a % 2 == 0:
        continue
    print(a)
```

반복문에서는 다음 차이를 구분하는 것이 핵심입니다.

| 문법 | 의미 |
|---|---|
| `break` | 반복문을 즉시 종료 |
| `continue` | 아래 코드를 건너뛰고 다음 반복으로 이동 |
| `while` | 조건이 참인 동안 반복 |
| `for` | 반복 가능한 객체를 순서대로 꺼내며 반복 |

### 4. 함수

계산 로직을 함수로 분리하고, `return`으로 결과를 돌려받는 연습을 했습니다.

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

추가로 여러 개의 인자를 받는 `*args`, 키워드 인자를 받는 `**kwargs`도 실습했습니다.

```python
def add_many(*args):
    result = 0
    for value in args:
        result += value
    return result


def print_kwargs(**kwargs):
    print(kwargs)
```

### 5. 터미널 인자 처리

`sys.argv`를 이용해 터미널에서 입력한 값을 Python 코드 안으로 가져오는 연습을 했습니다.

```python
# 0629/sum_args.py
import sys

args = sys.argv[1:]
total = 0

for i in args:
    total += int(i)

print("합계:", total)
```

실행 예시:

```powershell
python 0629/sum_args.py 10 20 30
```

출력:

```text
합계: 60
```

### 6. 객체와 클래스

`class`를 이용해서 관련 있는 데이터와 기능을 하나로 묶는 연습을 했습니다.

```python
class Television:
    serial_number = 0

    def __init__(self, channel, volume, on):
        Television.serial_number += 1
        self.serial_number = Television.serial_number
        self.channel = channel
        self.volume = volume
        self.on = on

    def __str__(self):
        return f"Television(channel={self.channel}, volume={self.volume}, on={self.on})"

    def set_channel(self, channel):
        self.channel = channel

    def get_channel(self):
        return self.channel
```

핵심 정리:

| 개념 | 의미 |
|---|---|
| 클래스 | 객체를 만들기 위한 설계도 |
| 인스턴스 | 클래스로부터 실제 생성된 객체 |
| 인스턴스 변수 | 객체마다 따로 가지는 값 |
| 클래스 변수 | 같은 클래스로 만든 객체들이 공유하는 값 |
| 메소드 | 클래스 안에 정의된 함수 |
| `self` | 현재 객체 자신을 가리키는 이름 |
| `__init__` | 객체가 생성될 때 자동으로 실행되는 생성자 |

### 7. GUI 프로그램 실습

`tkinter`를 이용해 간단한 메모장과 그림판 형태의 GUI 프로그램을 작성했습니다.

주요 기능:

- 새 파일 만들기
- 파일 열기
- 저장 / 다른 이름으로 저장
- 잘라내기 / 복사 / 붙여넣기
- 전체 선택
- 그림판 색상 선택
- 지우개 기능
- 선 굵기 조절
- 캔버스 지우기

---

## 실행 방법

### 1. 저장소 내려받기

```powershell
git clone https://github.com/rjsxo943-gif/mycodehouse.git
cd mycodehouse
```

### 2. 가상환경 생성 및 실행

```powershell
python -m venv .venv
.\.venv\Scripts\Activate.ps1
```

### 3. Python 파일 실행

```powershell
python 0626/stringEx.py
python 0629/sum_args.py 10 20 30
```

### 4. 노트북 실행

VS Code에서 `.ipynb` 파일을 열거나 Jupyter를 사용할 수 있습니다.

```powershell
jupyter notebook
```

### 5. GUI 예제 실행 참고

`0706/2.ipynb`의 GUI 예제는 `tkinter`를 사용합니다. Windows 기본 Python 환경에서는 보통 바로 실행됩니다.

`numpy` 예제를 실행하려면 환경에 `numpy`가 필요합니다.

```powershell
pip install numpy
```

---

## 복습 체크리스트

아래 항목을 설명할 수 있으면 현재 저장소의 기초 학습 흐름을 어느 정도 이해한 것입니다.

- `input()`으로 받은 값이 왜 문자열인지
- `int()`, `float()`, `str()`의 차이
- 리스트에 값을 추가하고 꺼내는 방법
- 인덱스가 0부터 시작하는 이유
- `if`, `elif`, `else`의 실행 순서
- `while`과 `for`의 차이
- `break`와 `continue`의 차이
- `range(1, 10)`이 1부터 9까지인 이유
- 함수에서 `return`이 하는 일
- `*args`와 `**kwargs`의 차이
- 지역 변수와 전역 변수의 차이
- `sys.argv[1:]`의 의미
- 클래스와 객체의 차이
- `self`와 `__init__`의 역할
- 클래스 변수와 인스턴스 변수의 차이
- `tkinter`로 GUI 창을 만드는 기본 구조

---

## 다음 개선 예정

- 날짜별 폴더마다 간단한 `README.md` 추가
- 노트북 실습 중 완성도가 높은 코드는 `.py` 파일로 분리
- `requirements.txt`에 실제 필요한 패키지 정리
- GUI 예제를 실행 가능한 단일 Python 파일로 정리
- Git/GitHub 명령어 실수 기록과 해결법 정리

---

## 한 줄 요약

이 저장소는 Python 기초 문법에서 시작해 함수, 터미널 입출력, 객체지향, GUI 프로그램까지 확장해 가는 개인 실습 기록입니다.
