# mycodehouse

Python 수업과 부트캠프 실습 코드를 날짜별로 정리하는 개인 학습 저장소입니다.

기초 문법을 단순히 따라 치는 것에서 끝내지 않고, 입력/출력, 조건문, 반복문, 함수, 자료구조, 객체지향, GUI 프로그램, 외부 라이브러리, TTS, 머신러닝 기초까지 직접 실습한 내용을 기록합니다.

---

## 현재 학습 흐름

```text
값 입력 → 자료형 변환 → 조건 판단 → 반복 처리 → 함수로 분리 → 파일/터미널 입출력 → 객체/클래스 → GUI 실습 → 외부 라이브러리 활용 → TTS → 머신러닝 기초와 시각화
```

| 날짜 | 학습 범위 | 핵심 키워드 |
|---|---|---|
| 2026-06-26 | Python 기초 문법 | `input`, `int`, `float`, `str`, f-string, 리스트, 인덱싱, 합계/평균 |
| 2026-06-29 | 제어문과 함수 | `if`, `while`, `for`, `break`, `continue`, 중첩 반복문, 함수, `*args`, `**kwargs`, `match case`, 파일 입출력, `sys.argv` |
| 2026-07-06 | 객체지향과 GUI | 클래스, 인스턴스 변수, 클래스 변수, `__init__`, `__str__`, `tkinter`, 메모장, 그림판, `numpy` 배열 |
| 2026-07-07 | 외부 라이브러리와 머신러닝 기초 | `pip`, 가상환경, `gTTS`, TTS, `.mp3`, `pandas`, `scikit-learn`, Iris 데이터셋, SVM, `plotly` 3D 시각화 |

---

## 폴더 / 파일 구성

| 경로 | 내용 |
|---|---|
| `0622/` | 초기 Python 실습 파일 |
| `0626/` | 입력, 형변환, 리스트, 문자열, 기초 통계 실습 |
| `0629/` | 조건문, 반복문, 함수, 터미널 인자, 파일 입출력 실습 |
| `0706/` | 객체지향, 클래스, `tkinter` 메모장/그림판, `numpy` 기초 실습 |
| `0707/` | 외부 라이브러리, TTS, Iris 데이터셋, SVM 분류, 3D 시각화 실습 |
| `source/` | 실습에 사용한 보조 소스 파일 폴더 |
| `command.md` | 자주 쓰는 터미널/Git 명령어 정리 |
| `requirements.txt` | Python 패키지 목록 정리용 파일 |

---

## 날짜별 README

| 날짜 | README | 요약 |
|---|---|---|
| 2026-06-26 | `0626/README.md` | Python 입력, 형변환, 리스트, 문자열 기초 |
| 2026-06-29 | `0629/README.md` | 제어문, 반복문, 함수, 터미널 인자 처리 |
| 2026-07-06 | `0706/README.md` | 객체지향과 GUI 프로그램 실습 |
| 2026-07-07 | `0707/README.md` | TTS, 외부 라이브러리, 머신러닝 분류와 시각화 |

---

## 주요 실습 내용

### 1. Python 기초 문법

`input()`으로 값을 입력받고, `int()`, `float()`, `str()`로 자료형을 변환하는 연습을 했습니다.

```python
a = int(input("Enter first number: "))
b = int(input("Enter second number: "))

print(f"a + b = {a + b}")
print(f"a - b = {a - b}")
print(f"a * b = {a * b}")
print(f"a / b = {a / b}")
```

리스트에 값을 저장하고 `sum`, `len`, `min`, `max`를 이용해 기본 통계를 계산했습니다.

```python
numbers = []

for i in range(5):
    value = int(input("5개의 정수값을 입력하시오: "))
    numbers.append(value)

print(f"mean = {sum(numbers) / len(numbers)}")
print(f"sum = {sum(numbers)}")
print(f"min = {min(numbers)}")
print(f"max = {max(numbers)}")
```

### 2. 조건문과 반복문

`if`, `while`, `for`, `break`, `continue`를 이용해 프로그램 흐름을 제어했습니다.

```python
a = 0

while a < 10:
    a += 1
    if a % 2 == 0:
        continue
    print(a)
```

| 문법 | 의미 |
|---|---|
| `break` | 반복문을 즉시 종료 |
| `continue` | 아래 코드를 건너뛰고 다음 반복으로 이동 |
| `while` | 조건이 참인 동안 반복 |
| `for` | 반복 가능한 객체를 순서대로 꺼내며 반복 |

### 3. 함수와 터미널 인자

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

`sys.argv`를 이용해 터미널에서 넘긴 값을 Python 코드 안에서 처리했습니다.

```python
import sys

args = sys.argv[1:]
total = 0

for i in args:
    total += int(i)

print("합계:", total)
```

### 4. 객체지향과 GUI

`class`를 이용해 관련 있는 데이터와 기능을 하나로 묶는 연습을 했습니다.

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
```

`tkinter`를 이용해서 메모장과 그림판 형태의 GUI 프로그램도 실습했습니다.

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

### 5. 외부 라이브러리와 TTS

Python 기본 기능만으로 부족한 기능은 외부 라이브러리를 설치해서 사용했습니다.

```powershell
pip install gtts
```

`gTTS`를 이용해 텍스트를 `.mp3` 음성 파일로 저장하는 TTS 실습을 했습니다.

```python
from gtts import gTTS

text = "오늘 배운 내용을 음성으로 저장합니다."
tts = gTTS(text=text, lang="ko")
tts.save("news_Son.mp3")
```

이 과정에서 `pip install`, 가상환경, 패키지 설치 오류, 생성 파일 관리의 필요성을 함께 확인했습니다.

### 6. 머신러닝 기초와 시각화

`scikit-learn`의 Iris 데이터셋을 이용해 SVM 분류 모델을 학습하고 새로운 샘플을 예측했습니다.

```python
import pandas as pd
import plotly.express as px
from sklearn.datasets import load_iris
from sklearn import svm

iris = load_iris()

df = pd.DataFrame(
    iris.data,
    columns=['sepal_length', 'sepal_width', 'petal_length', 'petal_width']
)

df['target'] = iris.target
df['species'] = df['target'].apply(lambda x: iris.target_names[x])

s = svm.SVC(gamma=0.1, C=10)
s.fit(iris.data, iris.target)

new_d = [
    [6.4, 3.2, 6.0, 2.5],
    [7.1, 3.1, 4.7, 1.35]
]

res = s.predict(new_d)

print("새로운 2개 샘플의 부류 번호는", res)
print("새로운 2개 샘플의 부류 이름은", iris.target_names[res])

fig = px.scatter_3d(
    df,
    x='sepal_length',
    y='sepal_width',
    z='petal_width',
    color='species'
)

fig.show(renderer="browser")
```

오늘 발생한 핵심 오류는 `pandas`와 `plotly`의 역할을 혼동한 것이었습니다.

```python
df = pd.data.iris()
fig = pd.scatter_3d(...)
```

위 코드는 동작하지 않습니다. `pandas`는 표 형태 데이터 처리용이고, 3D 그래프는 `plotly.express`의 `px.scatter_3d()`를 사용해야 합니다.

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

### 5. 필요한 패키지 설치 예시

```powershell
pip install numpy pandas scikit-learn plotly gtts
```

---

## 복습 체크리스트

아래 항목을 설명할 수 있으면 현재 저장소의 기초 학습 흐름을 어느 정도 이해한 것입니다.

- `input()`으로 받은 값이 왜 문자열인지
- `int()`, `float()`, `str()`의 차이
- 리스트에 값을 추가하고 꺼내는 방법
- `if`, `elif`, `else`의 실행 순서
- `while`과 `for`의 차이
- `break`와 `continue`의 차이
- 함수에서 `return`이 하는 일
- `*args`와 `**kwargs`의 차이
- `sys.argv[1:]`의 의미
- 클래스와 객체의 차이
- `self`와 `__init__`의 역할
- 클래스 변수와 인스턴스 변수의 차이
- `tkinter`로 GUI 창을 만드는 기본 구조
- `pip install`과 `import`의 차이
- 가상환경을 쓰는 이유
- TTS가 무엇인지
- `fit()`과 `predict()`의 차이
- `pandas`, `scikit-learn`, `plotly`의 역할 차이

---

## 다음 개선 예정

- 날짜별 폴더마다 간단한 `README.md` 유지
- 노트북 실습 중 완성도가 높은 코드는 `.py` 파일로 분리
- `requirements.txt`에 실제 필요한 패키지 정리
- GUI 예제를 실행 가능한 단일 Python 파일로 정리
- Git/GitHub 명령어 실수 기록과 해결법 정리
- `.mp3` 같은 생성 결과물을 Git에 계속 올릴지 기준 정리

---

## 한 줄 요약

이 저장소는 Python 기초 문법에서 시작해 함수, 터미널 입출력, 객체지향, GUI 프로그램, 외부 라이브러리, TTS, 머신러닝 기초까지 확장해 가는 개인 실습 기록입니다.
