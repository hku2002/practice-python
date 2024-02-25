# 튜플
# 순서O, 중복O, 수정X, 삭제X (불변)

a = ()
b = (1)
c = (1,)

print(type(a))
print(type(b))
print(type(c))

d = (1, 2, ('a', 'b', c))
e = (1, 2, 3)

print(d)
print(e[2])
print(e[0] + e[1])
print(e[:2])

print(type(list(e)))

print(e.index(2))
print(e.count(2))
