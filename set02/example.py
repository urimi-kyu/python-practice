def transpose(matrix):
    """20. 행과 열 바꾸기"""
    
    a = []
    if not matrix:
        return a
    else:
        i = len(matrix)
        j = len(matrix[0])

        for n in range(j):
            b = []
            for m in range(i):
                b.append(matrix[m][n])
            a.append(b)
        return a

# 직접 실행해 보고 싶으면 아래에 print를 써서 확인해 보세요.
if __name__ == "__main__":
    print(transpose([[1, 2, 3],
           [4, 5, 6]]))
