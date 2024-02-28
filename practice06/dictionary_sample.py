# 딕셔너리
# 순서X, 중복X, 수정O, 삭제O

# 선언
a = {}
b = {'key1': 'value1', 'key2': 'value2'}
print(a, b)

c = {'key1': [1, 2, 3, 4], 'key2': 'value2'}
print(c)

d = {
    'Name': 'Gil Dong',
    'Age': 33,
    'Gender': 'Male',
    'Activated': True
}
print(d)

e = dict([
    ('Name', 'Gil Dong'),
    ('Age', 33)
])
print(e)
