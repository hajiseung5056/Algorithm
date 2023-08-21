#세 정수를 입력받아 중앙값 구하기1

def med3(a,b,c):
    if a>=b:
        if b >= c:
            return b
        elif a <= c:
            return a
        else:
            return c

    elif a > c:
        return a
    elif b > c:
        return b
    else:
        return b