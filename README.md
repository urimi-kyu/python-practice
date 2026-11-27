# 파이썬 연습 (자동 채점)

PyCharm으로 문제를 풀고 **GitHub Desktop**으로 올리면, **GitHub가 자동으로 채점**해 줍니다.
채점은 GitHub 서버에서 하기 때문에 내 PC에 따로 설치할 것은 없어요.

```
set01/
  problems.md     ← 문제 설명
  solution01.py   ← 여기에 코드를 작성
  test_set01.py   ← 채점 파일 (고치지 마세요)
set02/            ← 2세트 (20문제) — 파일 구성은 1세트와 같아요
  problems.md
  solution02.py
  test_set02.py
set03/            ← 3세트 (20문제) — 알고리즘, 튜플, 딕셔너리 리스트
  problems.md
  solution03.py
  test_set03.py
set04/            ← 4세트 (5문제, 하루치) — Counter, 딕셔너리, 에라토스테네스의 체
  problems.md
  solution04.py
  test_set04.py
set05/            ← 5세트 (5문제, 하루치) — 스택, 큐, deque
  problems.md
  solution05.py
  test_set05.py
set06/            ← 6세트 (5문제, 하루치) — 정렬과 key, 이진 탐색
  problems.md
  solution06.py
  test_set06.py
set07/            ← 7세트 (5문제, 하루치) — 슬라이딩 윈도우, 누적합
  problems.md
  solution07.py
  test_set07.py
set08/            ← 8세트 (5문제, 하루치) — 2차원 리스트, BFS/DFS 기초
  problems.md
  solution08.py
  test_set08.py
answers/          ← 모범 답안 (다 풀고 나서 확인하세요)
  answer04.py
  answer05.py
  answer06.py
  answer07.py
  answer08.py
.github/workflows/python-test.yml  ← 자동 채점 설정
.gitignore        ← 올리지 않을 파일 목록
```

---

## 처음 한 번만: 준비하기

### 1) 폴더 위치 정하기
이 폴더 전체를 찾기 쉬운 곳에 둡니다. 예: `C:\codiiiing\python-practice`
> 탐색기에서 `.github` 폴더가 안 보여도 괜찮아요. 숨김 폴더처럼 보일 뿐 그대로 있어요.

### 2) PyCharm에서 이 폴더 열기
1. PyCharm → **File → Open** → 이 폴더를 선택합니다.
2. 인터프리터(Python)를 고르라는 안내가 뜨면, 갖고 계신 PyPy를 고릅니다.
   (`C:\codiiiing\pypy3.7-v7.3.4-win64\pypy3.exe`)

### 3) GitHub Desktop에 로그인
GitHub Desktop → **File → Options → Accounts**에서 GitHub 계정으로 로그인되어 있는지 확인합니다.
(계정이 없으면 https://github.com 에서 먼저 회원가입하세요)

### 4) 이 폴더를 저장소로 만들기
1. GitHub Desktop → **File → Add local repository**를 누릅니다.
2. **Choose...**로 이 폴더(예: `C:\codiiiing\python-practice`)를 고릅니다.
3. "This directory does not appear to be a Git repository" 안내가 뜨면 그 안의 **create a repository** 링크를 누릅니다.
   (안내 없이 바로 추가되면 이미 저장소인 거예요. 5단계로 넘어가세요)
4. 설정은 이렇게 둡니다.
   - **Initialize this repository with a README**: ❌ 체크하지 않기 (이미 있어요)
   - **Git ignore**: `None` (이미 있어요)
   - **License**: `None`
5. **Create repository**를 누릅니다.

### 5) GitHub에 올리기 (Publish)
1. 위쪽 **Publish repository** 버튼을 누릅니다.
2. Name은 `python-practice` 그대로 둡니다.
3. **Keep this code private**
   - 체크 해제(공개): 자동 채점을 무제한 무료로 쓸 수 있어요.
   - 체크(비공개): 매달 무료 사용량이 있어서 연습용으로는 충분해요.
4. **Publish repository**를 누릅니다.

### 6) 채점이 돌아가는지 확인
GitHub Desktop 메뉴 **Repository → View on GitHub**를 누르면 저장소 웹페이지가 열려요.
위쪽 **Actions** 탭에 **파이썬 채점**이 보이면 성공이에요.
> 아직 문제를 안 풀었으니 ❌가 나오는 게 정상이에요.

---

## 매번: 문제 풀고 채점받기

1. PyCharm에서 `set01/solution01.py`를 열고, 함수 안의 `pass`를 지우고 코드를 작성한 뒤 저장합니다.
2. (선택) 파일 맨 아래 `if __name__ == "__main__":` 부분에 `print(...)`를 써 두고 초록색 ▶ 버튼으로 실행해 봅니다.
3. GitHub Desktop을 보면 왼쪽 **Changes** 탭에 고친 파일이 보여요.
   오른쪽에는 바뀐 줄이 초록색(추가)과 빨간색(삭제)으로 표시돼요.
4. 왼쪽 아래 **Summary** 칸에 메모를 쓰고(예: `1~3번 풀이`) **Commit to main**을 누릅니다.
5. 위쪽 **Push origin**을 누릅니다.
6. **Repository → View on GitHub** → **Actions** 탭에서 결과를 봅니다.
   - ✅ 초록색 체크: 전부 통과
   - ❌ 빨간색 X: 틀린 문제가 있음 → 눌러서 **채점 실행** 단계를 열면 어떤 문제가 왜 틀렸는지 나와요.

> **Commit**은 "내 PC에 저장 기록 남기기", **Push**는 "그 기록을 GitHub로 보내기"예요.
> Commit만 하고 Push를 안 하면 GitHub에는 안 올라가요.

> 채점은 모든 세트를 한꺼번에 해요. 그래서 1세트를 다 맞혀도 2세트에 안 푼 문제가 있으면 전체 결과는 ❌로 떠요.
> 로그에서 `set01/...`은 모두 PASSED, `set02/...`는 일부 FAILED처럼 세트별로 확인하세요.

### 채점 결과 읽는 법
```
set01/test_set01.py::test_01_is_even[4-True] PASSED
set01/test_set01.py::test_03_sum_to_n[10-55] FAILED
```
`test_03_sum_to_n[10-55] FAILED`는 **3번 문제**에서 `sum_to_n(10)`의 답이 `55`여야 하는데 다른 값이 나왔다는 뜻이에요.
아래쪽에 `assert None == 55`처럼 나오면, 함수가 아무것도 돌려주지 않은 것(`return` 빠짐)입니다.

---

## (선택) 올리기 전에 내 PC에서 미리 채점하기
꼭 안 해도 되지만, 매번 올려 보기 번거로우면 써 보세요.

1. PyCharm에서 `test_set01.py`를 엽니다.
2. 위쪽에 **pytest 설치** 안내가 뜨면 누릅니다. (PyCharm이 알아서 설치해요)
3. 파일 이름에서 마우스 오른쪽 버튼 → **Run 'pytest in test_set01.py'**를 누르면 결과가 아래에 나와요.

## 자주 생기는 문제
- **Actions 탭에 아무것도 안 떠요** → GitHub 웹에서 `.github/workflows/python-test.yml` 파일이 올라가 있는지 확인하세요.
- **Push origin 버튼이 안 보여요** → 아직 Commit을 안 했거나, 이미 다 올라간 상태예요.
- **`test_set01.py`가 Changes에 떠요** → 실수로 채점 파일을 고친 거예요. 파일에서 마우스 오른쪽 버튼 → **Discard changes**로 되돌리세요.
- **`.idea` 폴더가 Changes에 떠요** → PyCharm 설정 파일이라 올려도 문제는 없어요. 안 올리고 싶으면 `.gitignore` 파일에 `.idea/` 한 줄을 추가하세요.

---

다 풀었으면 Claude에게 저장소 주소를 알려주고 **"다음 세트 만들어줘"** 또는 **"내 코드 리뷰해줘"** 라고 하면 됩니다.
