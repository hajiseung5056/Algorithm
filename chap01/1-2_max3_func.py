# 세 정수의 최댓값 구하기

def max3(a,b,c):
        """a,b,c의 최댓값을 구하여 반환"""
        maximum = a
        if b > maximum: maximum = b
        if c > maximum: maximum = c
        return maximum # 최댓값 반환

print(f'max3(3,2,1) = {max(3,2,1)}')
print(f'max3(3,2x) = {max(3,2,2)}')
print(f'max3(3,1,2) = {max(3,1,2)}')
print(f'max3(3,2,3) = {max(3,2,3)}')
print(f'max3(2,1,3) = {max(2,1,3)}')
print(f'max3(3,3,2) = {max(3,3,2)}')
print(f'max3(3,3,3) = {max(3,3,3)}')
print(f'max3(2,2,3) = {max(2,2,3)}')
print(f'max3(2,3,1) = {max(2,3,1)}')
print(f'max3(2,3,2) = {max(2,3,2)}')
print(f'max3(1,3,2) = {max(1,3,2)}')
print(f'max3(2,3,3) = {max(2,3,3)}')
print(f'max3(1,2,3) = {max(1,2,3)}')