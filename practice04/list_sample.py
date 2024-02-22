# 리스트
# 순서 존재, 중복 가능, 수정 가능, 삭제 가능

# 선언
a = []
b = list()
c = [0, 1, 2, 3]
d = [1000, 2000, 'sample1', 'sample2', True, False]
e = [1, 2, [1000, 2000], ['sample1', 'sample2'], [True, False]]
print(c)
print(len(c))
print(d)
print(e)

# 인덱싱
print('========indexing=======')
print('d[0]: ', d[0])
print('e[0] + e[2][1]: ', e[0] + e[2][1])

# 슬라이싱
print('========slicing=======')
print('d[0:3]: ', d[0:3])
print('d[0:3]: ', d[2:])
print('e[-1][0:2]: ', e[-1][0:2])

# 값 비교
print(c == c[:3] + c[3:])
print('c: ', c)
print('c[:3] + c[3:]: ', c[:3] + c[3:])
