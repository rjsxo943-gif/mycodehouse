# 2026-07-07 TTS, 외부 라이브러리, 머신러닝 기초 실습

이 폴더는 Python 외부 라이브러리를 설치하고 사용하는 과정, 텍스트를 음성 파일로 변환하는 TTS 실습, 그리고 `scikit-learn`의 Iris 데이터셋을 이용한 머신러닝 기초 실습을 정리한 날짜별 기록입니다.

오늘의 핵심은 단순 문법 연습에서 한 단계 넘어가, 외부 패키지를 불러오고 데이터셋을 모델에 학습시킨 뒤 결과를 예측·시각화하는 흐름을 경험한 것입니다.

---

## 파일 구성

| 파일 | 배운 내용 |
|---|---|
| `1.ipynb` | Python 외부 라이브러리 사용, 파일/실행 환경 관련 실습 |
| `chap15.ipynb` | 교재 또는 수업 챕터 기반 실습 정리 |
| `ml.ipynb` | Iris 데이터셋, `pandas` DataFrame, SVM 분류 모델, 예측, 3D 시각화 실습 |
| `../source/` | 실습에 사용한 소스 파일 또는 보조 자료 폴더 |
| `../news_Son.mp3` | TTS 실습으로 생성한 음성 파일 결과물 |

> 참고: `mp3` 같은 생성 결과물은 용량이 커질 수 있으므로, 계속 Git에 올릴 필요가 없다면 `.gitignore`에 `*.mp3`를 추가해도 됩니다.

---

## 1. 외부 라이브러리 설치와 사용

Python 기본 문법만으로는 할 수 있는 일이 제한됩니다. 그래서 필요한 기능은 외부 라이브러리를 설치해서 사용합니다.

예를 들어 텍스트를 음성으로 바꾸기 위해 `gTTS`를 설치할 수 있습니다.

```powershell
pip install gtts
```

설치한 라이브러리는 `import`로 불러옵니다.

```python
from gtts import gTTS
```

이 과정에서 중요한 점은 현재 실행 중인 Python 환경과 `pip install`이 설치하는 환경이 같아야 한다는 것입니다.

현재 터미널 프롬프트가 다음처럼 보이면:

```powershell
(.venv) (base) PS C:\Users\rjsxo\bootcamp\mycodehouse>
```

`venv`와 `conda base`가 동시에 표시되고 있는 상태입니다. 이때는 패키지가 어느 환경에 설치되는지 헷갈릴 수 있으므로, 가능하면 하나의 가상환경 기준으로 정리하는 것이 좋습니다.

---

## 2. TTS(Text To Speech) 실습

TTS는 텍스트를 음성으로 변환하는 기능입니다.

기본 흐름은 다음과 같습니다.

```python
from gtts import gTTS

text = "오늘 배운 내용을 음성으로 저장합니다."
tts = gTTS(text=text, lang="ko")
tts.save("news_Son.mp3")
```

이 코드는 문자열 `text`를 한국어 음성으로 변환한 뒤 `news_Son.mp3` 파일로 저장합니다.

### 핵심 개념

| 개념 | 의미 |
|---|---|
| TTS | Text To Speech, 텍스트를 음성으로 변환하는 기술 |
| `gTTS` | Google Text-to-Speech 기반 Python 라이브러리 |
| `save()` | 변환된 음성을 파일로 저장하는 메소드 |
| `.mp3` | 음성 결과 파일 형식 |

---

## 3. 라이브러리 설치 오류 경험

`playsound` 설치 중 빌드 오류가 발생할 수 있습니다.

이런 오류는 코드가 틀렸다기보다, 패키지 버전·Python 버전·빌드 도구 문제인 경우가 많습니다.

이때 해결 방향은 다음과 같습니다.

1. 꼭 필요한 라이브러리인지 확인한다.
2. 대체 라이브러리를 찾는다.
3. `pip`, Python 버전, 가상환경 상태를 확인한다.
4. 단순 재생 목적이면 운영체제 기본 명령이나 다른 패키지로 우회한다.

즉, 외부 라이브러리를 쓸 때는 `설치 → import → 실행` 중 어디서 실패했는지 분리해서 보는 습관이 중요합니다.

---

## 4. Iris 데이터셋 로드

머신러닝 실습에서는 `scikit-learn`의 Iris 데이터셋을 사용했습니다.

```python
from sklearn.datasets import load_iris

iris = load_iris()
```

Iris 데이터셋은 붓꽃의 꽃받침과 꽃잎 길이/너비를 이용해 품종을 분류하는 대표적인 예제 데이터입니다.

입력 데이터는 4개의 특징값으로 구성됩니다.

| 특징 | 의미 |
|---|---|
| `sepal_length` | 꽃받침 길이 |
| `sepal_width` | 꽃받침 너비 |
| `petal_length` | 꽃잎 길이 |
| `petal_width` | 꽃잎 너비 |

정답 라벨은 3개의 품종입니다.

```python
iris.target_names
```

---

## 5. pandas DataFrame 만들기

`iris.data`는 숫자 배열 형태입니다. 사람이 보기 좋게 정리하기 위해 `pandas`의 `DataFrame`으로 바꿨습니다.

```python
import pandas as pd

iris = load_iris()

 df = pd.DataFrame(
    iris.data,
    columns=['sepal_length', 'sepal_width', 'petal_length', 'petal_width']
)
```

실제 코드에서는 들여쓰기 오류가 없어야 하므로 아래처럼 작성합니다.

```python
df = pd.DataFrame(
    iris.data,
    columns=['sepal_length', 'sepal_width', 'petal_length', 'petal_width']
)
```

품종 이름도 추가할 수 있습니다.

```python
df['target'] = iris.target
df['species'] = df['target'].apply(lambda x: iris.target_names[x])
```

---

## 6. SVM 모델 학습

SVM은 데이터를 분류하는 머신러닝 알고리즘 중 하나입니다.

```python
from sklearn import svm

s = svm.SVC(gamma=0.1, C=10)
s.fit(iris.data, iris.target)
```

여기서 핵심은 다음과 같습니다.

| 코드 | 의미 |
|---|---|
| `svm.SVC()` | 분류용 SVM 모델 생성 |
| `gamma` | 데이터 하나의 영향 범위와 관련된 파라미터 |
| `C` | 오분류를 얼마나 허용할지 조절하는 파라미터 |
| `fit()` | 입력 데이터와 정답을 이용해 모델 학습 |

---

## 7. 새로운 샘플 예측

학습이 끝난 모델은 새로운 데이터를 보고 품종을 예측할 수 있습니다.

```python
new_d = [
    [6.4, 3.2, 6.0, 2.5],
    [7.1, 3.1, 4.7, 1.35]
]

res = s.predict(new_d)
print("새로운 2개 샘플의 부류는", res)
```

예측 결과는 숫자로 나옵니다.

```python
print(iris.target_names[res])
```

이렇게 하면 숫자 라벨을 실제 품종 이름으로 바꿔 확인할 수 있습니다.

---

## 8. pandas와 Plotly 역할 구분

오늘 발생한 대표 오류는 다음과 같습니다.

```python
df = pd.data.iris()
fig = pd.scatter_3d(...)
```

이 코드는 동작하지 않습니다.

이유는 `pandas`에는 `data.iris()`도 없고 `scatter_3d()`도 없기 때문입니다.

역할을 나누면 다음과 같습니다.

| 라이브러리 | 역할 |
|---|---|
| `pandas` | 표 형태 데이터 처리 |
| `sklearn.datasets` | 예제 데이터셋 로드 |
| `sklearn.svm` | 머신러닝 모델 생성/학습/예측 |
| `plotly.express` | 그래프와 시각화 |

즉, 3D 그래프는 `plotly.express`로 그려야 합니다.

```python
import plotly.express as px

fig = px.scatter_3d(
    df,
    x='sepal_length',
    y='sepal_width',
    z='petal_width',
    color='species'
)

fig.show(renderer="browser")
```

---

## 9. 최종 머신러닝 실습 코드 예시

```python
import pandas as pd
import plotly.express as px
from sklearn.datasets import load_iris
from sklearn import svm

# 1. 데이터셋 로드
iris = load_iris()

# 2. DataFrame 생성
df = pd.DataFrame(
    iris.data,
    columns=['sepal_length', 'sepal_width', 'petal_length', 'petal_width']
)

df['target'] = iris.target
df['species'] = df['target'].apply(lambda x: iris.target_names[x])

# 3. SVM 모델 학습
s = svm.SVC(gamma=0.1, C=10)
s.fit(iris.data, iris.target)

# 4. 새로운 데이터 예측
new_d = [
    [6.4, 3.2, 6.0, 2.5],
    [7.1, 3.1, 4.7, 1.35]
]

res = s.predict(new_d)

print("새로운 2개 샘플의 부류 번호는", res)
print("새로운 2개 샘플의 부류 이름은", iris.target_names[res])

# 5. 3D 시각화
fig = px.scatter_3d(
    df,
    x='sepal_length',
    y='sepal_width',
    z='petal_width',
    color='species'
)

fig.show(renderer="browser")
```

---

## 오늘 배운 핵심

- 외부 라이브러리는 `pip install`로 설치하고 `import`로 불러온다.
- 가상환경이 여러 개 겹치면 패키지 설치 위치가 헷갈릴 수 있다.
- TTS는 텍스트를 음성 파일로 변환하는 기술이다.
- `gTTS`를 이용하면 문자열을 `.mp3` 파일로 저장할 수 있다.
- `scikit-learn`의 `load_iris()`로 머신러닝 예제 데이터를 불러올 수 있다.
- `pandas`는 표 형태 데이터를 다루는 라이브러리이다.
- SVM은 분류 문제에 사용할 수 있는 머신러닝 모델이다.
- `fit()`은 학습, `predict()`는 예측이다.
- `pandas`와 `plotly`는 역할이 다르다.
- 3D 산점도는 `plotly.express.scatter_3d()`로 그린다.

---

## 추가로 연습하면 좋은 문제

1. `new_d`에 새로운 붓꽃 샘플 5개를 추가해서 예측하기
2. 예측 결과를 숫자가 아니라 품종 이름으로만 출력하기
3. `gamma`, `C` 값을 바꿔가며 예측 결과가 달라지는지 확인하기
4. `petal_length`를 포함한 다른 3개 조합으로 3D 그래프 그리기
5. `pandas` DataFrame에서 `head()`, `tail()`, `describe()` 출력하기
6. TTS로 직접 작성한 문장을 `.mp3` 파일로 저장하기
7. 생성된 `.mp3` 파일을 Git에 올릴지 말지 기준 정하기
8. 오늘 발생한 오류 메시지를 `error-log.md`로 정리하기

---

## 한 줄 요약

2026-07-07에는 Python 외부 라이브러리 사용 경험을 확장하고, TTS로 음성 파일을 생성했으며, Iris 데이터셋과 SVM을 이용해 머신러닝 분류와 3D 시각화의 기본 흐름을 연습했습니다.
