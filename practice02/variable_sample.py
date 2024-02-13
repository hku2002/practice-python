# 파이썬 변수

# 기본 선언
n = 700
print(n)
print(type(n))

# 동시 선언
x = y = z = 700
print(x, y, z)
print()

# 선언 및 재선언
var = 75
var = 'str'
print(var)  # str
print(type(var))  # class 'str'
print()

# Object References
# 변수 할당 상태
# 1. 타입에 맞는 오브젝트 생성
# 2. 값 생성
# 3. print

# 예)
print(300)
print(int(300))
print()

# id 확인
m = 800
n = 655

print(id(m))
print(id(n))
print(id(m) == id(n))
print()

a = 800
b = 800
print(id(a))
print(id(b))
print(id(a) == id(b))
