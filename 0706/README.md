# 2026-07-06 객체지향, GUI, NumPy 기초 실습

이 폴더는 Python의 객체지향 문법과 간단한 GUI 프로그램 제작을 실습한 날짜별 기록입니다.

`class`로 객체를 만들고, `tkinter`로 메모장과 그림판 형태의 프로그램을 작성했으며, 마지막에는 `numpy` 배열의 기본 형태도 확인했습니다.

---

## 파일 구성

| 파일 | 배운 내용 |
|---|---|
| `1.ipynb` | `Television` 클래스를 이용한 객체 생성, 클래스 변수, 인스턴스 변수, 생성자, 메소드, `__str__` 실습 |
| `2.ipynb` | `tkinter` 메모장, 그림판 GUI, 이벤트 처리, 파일 열기/저장, `numpy` 배열 변환 실습 |

---

## 1. 클래스와 객체

`1.ipynb`에서는 `Television` 클래스를 만들었습니다.

```python
class Television:
    serial_number = 0

    def __init__(self, channel, volume, on):
        Television.serial_number += 1
        self.serial_number = Television.serial_number
        self.channel = channel
        self.volume = volume
        self.on = on
```

클래스는 객체를 만들기 위한 설계도입니다.

```python
tv1 = Television(1, 10, True)
tv2 = Television(2, 20, False)
tv3 = Television(3, 30, True)
```

위 코드에서는 같은 `Television` 클래스로 서로 다른 TV 객체 3개를 만들었습니다.

---

## 2. 클래스 변수와 인스턴스 변수

### 클래스 변수

```python
serial_number = 0
```

클래스 변수는 같은 클래스로 만든 객체들이 공유하는 값입니다.

이 실습에서는 TV 객체가 생성될 때마다 `Television.serial_number`를 1씩 증가시켜 객체 번호처럼 사용했습니다.

```python
Television.serial_number += 1
self.serial_number = Television.serial_number
```

### 인스턴스 변수

```python
self.channel = channel
self.volume = volume
self.on = on
```

인스턴스 변수는 객체마다 따로 가지는 값입니다.

예를 들어 `tv1`과 `tv2`는 같은 `Television` 클래스로 만들었지만 채널, 볼륨, 전원 상태가 다를 수 있습니다.

---

## 3. 생성자 `__init__`

`__init__`은 객체가 생성될 때 자동으로 실행되는 메소드입니다.

```python
def __init__(self, channel, volume, on):
    self.channel = channel
    self.volume = volume
    self.on = on
```

객체를 만들 때 넘긴 값이 생성자로 들어갑니다.

```python
tv1 = Television(1, 10, True)
```

이 코드는 다음 의미를 가집니다.

```text
channel = 1
volume = 10
on = True
```

---

## 4. 메소드와 self

클래스 안에 정의된 함수를 메소드라고 합니다.

```python
def set_channel(self, channel):
    self.channel = channel


def get_channel(self):
    return self.channel
```

`self`는 현재 객체 자신을 의미합니다.

```python
print(tv1.get_channel())
print(tv1.channel)
```

두 출력 모두 `tv1`의 채널 값을 확인하는 코드입니다.

---

## 5. 객체 출력 `__str__`

`__str__`은 객체를 `print()`로 출력할 때 어떤 문자열로 보일지 정하는 특수 메소드입니다.

```python
def __str__(self):
    return f"Television(channel={self.channel}, volume={self.volume}, on={self.on})"
```

그래서 아래처럼 객체 자체를 출력할 수 있습니다.

```python
print(tv1)
```

출력 예시:

```text
Television(channel=1, volume=10, on=True)
```

---

## 6. tkinter 메모장 만들기

`2.ipynb`에서는 `tkinter`를 이용해 메모장 프로그램을 작성했습니다.

```python
import os
import tkinter as tk
from tkinter import filedialog, messagebox
```

메모장은 `Notepad` 클래스로 구성했습니다.

```python
class Notepad:
    def __init__(self, root):
        self.root = root
        self.root.title("메모장")
        self.root.geometry("800x600")
        self.file_path = None
        self.create_widgets()
```

### 주요 기능

| 기능 | 관련 메소드 |
|---|---|
| 새 파일 | `new_file()` |
| 파일 열기 | `open_file()` |
| 저장 | `save_file()` |
| 다른 이름으로 저장 | `save_as()` |
| 실제 파일 쓰기 | `_write_file()` |
| 저장 여부 확인 | `_should_save()` |
| 잘라내기 | `cut_text()` |
| 복사 | `copy_text()` |
| 붙여넣기 | `paste_text()` |
| 전체 선택 | `select_all()` |
| 종료 처리 | `on_close()` |

---

## 7. tkinter 위젯과 메뉴

메모장에서는 텍스트 입력창, 스크롤바, 메뉴를 사용했습니다.

```python
self.text = tk.Text(self.root, undo=True, wrap="word")
self.text.pack(fill="both", expand=True)
```

스크롤바:

```python
scrollbar = tk.Scrollbar(self.text)
scrollbar.pack(side="right", fill="y")
self.text.config(yscrollcommand=scrollbar.set)
scrollbar.config(command=self.text.yview)
```

메뉴:

```python
menu = tk.Menu(self.root)
self.root.config(menu=menu)
```

파일 메뉴와 편집 메뉴를 나누어 GUI 프로그램다운 구조를 만들었습니다.

---

## 8. 단축키 바인딩

`bind_all()`을 이용해 키보드 단축키도 연결했습니다.

```python
self.root.bind_all("<Control-n>", lambda e: self.new_file())
self.root.bind_all("<Control-o>", lambda e: self.open_file())
self.root.bind_all("<Control-s>", lambda e: self.save_file())
self.root.bind_all("<Control-a>", lambda e: self.select_all())
```

즉, GUI는 버튼만 누르는 프로그램이 아니라 키보드 이벤트도 처리할 수 있습니다.

---

## 9. 파일 열기와 저장

파일 열기는 `filedialog.askopenfilename()`을 사용했습니다.

```python
path = filedialog.askopenfilename(
    defaultextension=".txt",
    filetypes=[("텍스트 파일", "*.txt"), ("모든 파일", "*.*")]
)
```

파일 저장은 `open(path, "w", encoding="utf-8")` 구조를 사용했습니다.

```python
with open(path, "w", encoding="utf-8") as f:
    f.write(self.text.get("1.0", tk.END))
```

여기서 `encoding="utf-8"`은 한글 저장을 위해 중요합니다.

---

## 10. tkinter 그림판 만들기

같은 노트북에서 `PaintApp` 클래스로 간단한 그림판도 만들었습니다.

```python
from tkinter import colorchooser

paint_window = tk.Toplevel(root)
paint_window.title("그림판")
paint_window.geometry("900x650")
```

그림판은 새 창인 `Toplevel`에 만들어졌습니다.

### 주요 기능

| 기능 | 관련 코드 |
|---|---|
| 색상 선택 | `colorchooser.askcolor()` |
| 지우개 토글 | `toggle_eraser()` |
| 캔버스 지우기 | `clear_canvas()` |
| 선 굵기 조절 | `Scale` 위젯 |
| 마우스로 그리기 | `<Button-1>`, `<B1-Motion>`, `<ButtonRelease-1>` 이벤트 |

---

## 11. Canvas 이벤트 처리

그림판에서는 마우스 이벤트를 이용했습니다.

```python
self.canvas.bind("<Button-1>", self.start_draw)
self.canvas.bind("<B1-Motion>", self.draw)
self.canvas.bind("<ButtonRelease-1>", self.stop_draw)
```

| 이벤트 | 의미 |
|---|---|
| `<Button-1>` | 마우스 왼쪽 버튼 클릭 시작 |
| `<B1-Motion>` | 왼쪽 버튼을 누른 채 이동 |
| `<ButtonRelease-1>` | 왼쪽 버튼에서 손을 뗌 |

선은 `create_line()`으로 그렸습니다.

```python
self.canvas.create_line(
    self.last_x, self.last_y, event.x, event.y,
    fill=self.current_color(),
    width=self.width,
    capstyle="round",
    smooth=True
)
```

---

## 12. 지우개 구현 방식

지우개는 실제로 선을 삭제하는 방식이 아니라, 현재 색상을 흰색으로 바꾸는 방식으로 구현했습니다.

```python
def current_color(self):
    return "white" if self.eraser else self.color
```

배경색이 흰색이기 때문에 흰색으로 그리면 지우개처럼 보입니다.

---

## 13. NumPy 배열 기초

마지막에는 Python 리스트를 NumPy 배열로 바꾸는 실습을 했습니다.

```python
import numpy as np

ftemp = [32, 63, 73, 82, 91, 100, 110, 120, 80, 140]
F = np.array(ftemp)

print(ftemp)
print(F)
```

리스트와 배열은 출력 모양부터 다릅니다.

```text
[32, 63, 73, 82, 91, 100, 110, 120, 80, 140]
[ 32  63  73  82  91 100 110 120  80 140]
```

NumPy 배열은 이후 데이터 분석, AI, 행렬 계산에서 많이 사용됩니다.

---

## 오늘 배운 핵심

- 클래스는 객체를 만들기 위한 설계도이다.
- 객체는 클래스로부터 생성된 실제 인스턴스이다.
- `__init__`은 객체 생성 시 자동 실행되는 생성자이다.
- `self`는 현재 객체 자신을 의미한다.
- 클래스 변수는 객체들이 공유하고, 인스턴스 변수는 객체마다 따로 가진다.
- `__str__`을 정의하면 객체를 출력할 때 보기 좋은 문자열로 표현할 수 있다.
- `tkinter`로 GUI 창, 메뉴, 버튼, 텍스트 입력창, 캔버스를 만들 수 있다.
- GUI 프로그램은 이벤트와 콜백 함수의 연결로 동작한다.
- `filedialog`와 `open()`을 이용해 파일 열기/저장을 구현할 수 있다.
- `Canvas`와 마우스 이벤트를 이용해 그림판 기능을 만들 수 있다.
- Python 리스트를 `np.array()`로 NumPy 배열로 바꿀 수 있다.

---

## 추가로 연습하면 좋은 문제

1. `Television` 클래스에 `volume_up()`과 `volume_down()` 메소드 추가하기
2. `Television` 객체를 5개 만들고 각각의 `serial_number` 출력하기
3. `Car` 클래스를 만들어 속도, 색상, 모델을 저장하기
4. 메모장에 글자 크기 변경 기능 추가하기
5. 메모장에 현재 파일 이름을 창 제목에 표시하기
6. 그림판에 선 색상 초기화 버튼 추가하기
7. 그림판에 사각형/원 그리기 기능 추가하기
8. 섭씨 온도 리스트를 NumPy 배열로 만들고 화씨 온도로 변환하기

---

## 한 줄 요약

2026-07-06에는 객체지향 문법을 이용해 데이터를 구조화하고, `tkinter`로 실제 창이 있는 메모장과 그림판을 만들어 보면서 GUI 프로그램의 기본 흐름을 연습했습니다.
