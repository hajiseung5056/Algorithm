# 세 정수의 최댓값 구하기

def max3(a,b,c):
    maximum = a
    if b > maximum: maximum = b
    if c > maximum: maximum = c
    return maximum

print(f'max3(3,2,1) = {max(3,2,1)}')