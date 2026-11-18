# 파이썬 연습 (자동 채점)

PyCharm으로 문제를 풀고 GitHub 웹사이트에 올리면, **GitHub가 자동으로 채점**해 줍니다.
채점은 GitHub 서버에서 하기 때문에 **내 PC에 따로 설치할 것은 없어요.**

```
set01/
  problems.md     ← 문제 설명
  solution01.py   ← 여기에 코드를 작성
  test_set01.py   ← 채점 파일 (고치지 마세요)
.github/workflows/python-test.yml  ← 자동 채점 설정
```

---

## 처음 한 번만: 준비하기

### 1) PyCharm에서 이 폴더 열기
1. PyCharm → **File → Open** → 이 폴더를 선택합니다.
2. 오른쪽 아래에 인터프리터(Python)를 고르라는 안내가 뜨면, 갖고 계신 PyPy를 고릅니다.
   (`C:\codiiiing\pypy3.7-v7.3.4-win64\pypy3.exe`)

### 2) GitHub 계정과 저장소 만들기
1. https://github.com 에서 회원가입합니다.
2. 오른쪽 위 **+** → **New repository**를 누릅니다.
3. Repository name에 `python-practice`처럼 이름을 적습니다.
4. **Public**을 선택합니다. (공개 저장소는 자동 채점이 무료예요)
5. **Create repository**를 누릅니다.

### 3) 파일 처음 올리기
1. 방금 만든 저장소 페이지에서 **uploading an existing file** 링크(또는 **Add file → Upload files**)를 누릅니다.
2. 탐색기에서 이 폴더 안의 **`set01` 폴더와 `README.md`**를 브라우저 창에 끌어다 놓습니다.
3. 아래 **Commit changes**를 누릅니다.

### 4) 채점 설정 파일 만들기 ⚠️ 중요
`.github` 폴더는 이름이 점(.)으로 시작해서 끌어다 놓기로는 잘 안 올라가요. 그래서 이 파일은 웹에서 직접 만듭니다.

1. 저장소 페이지에서 **Add file → Create new file**을 누릅니다.
2. 파일 이름 칸에 정확히 이렇게 입력합니다: `.github/workflows/python-test.yml`
   (`/`를 입력하면 자동으로 폴더가 만들어져요)
3. 내용 칸에 이 폴더의 `.github/workflows/python-test.yml` 파일 내용을 그대로 복사해 붙여넣습니다.
   (PyCharm 왼쪽 파일 목록에서 열 수 있어요)
4. **Commit changes**를 누릅니다.

이제 위쪽 **Actions** 탭에 채점이 돌아가는 게 보여요.
> 아직 문제를 안 풀었으니 ❌가 나오는 게 정상이에요.

---

## 매번: 문제 풀고 채점받기

1. PyCharm에서 `set01/solution01.py`를 열고, 함수 안의 `pass`를 지우고 코드를 작성합니다.
2. (선택) 파일 맨 아래 `if __name__ == "__main__":` 부분에 `print(...)`를 써 두고, 초록색 ▶ 버튼으로 실행해서 결과를 확인해 봅니다.
3. GitHub 저장소 페이지에서 `set01` 폴더 → **Add file → Upload files** → 고친 `solution01.py`를 끌어다 놓고 **Commit changes**를 누릅니다.
   (같은 이름의 파일은 자동으로 새 파일로 바뀌어요)
4. **Actions** 탭에서 결과를 봅니다.
   - ✅ 초록색 체크: 전부 통과
   - ❌ 빨간색 X: 틀린 문제가 있음 → 눌러서 **채점 실행** 단계를 열면 어떤 문제가 왜 틀렸는지 나옵니다.

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
3. 파일 이름에서 마우스 오른쪽 버튼 → **Run 'pytest in test_set01.py'**를 누르면 결과가 아래에 나옵니다.

## (나중에) Git으로 올리기
익숙해지면 웹 업로드 대신 PyCharm의 **Git** 기능으로 한 번에 올릴 수 있어요. 필요하면 그때 Claude에게 "PyCharm으로 GitHub에 올리는 법 알려줘"라고 하세요.

---

다 풀었으면 Claude에게 저장소 주소를 알려주고 **"다음 세트 만들어줘"** 또는 **"내 코드 리뷰해줘"** 라고 하면 됩니다.
