# 기본 출력법
print('sample01')
print("sample02")
print()
print('''sample03''')
print("""sample04""")

print()

# separator
print('A', 'B', 'C', 'D', 'E')
print('A', 'B', 'C', 'D', 'E', sep=',')
print('A', 'B', 'C', 'D', 'E', sep='  ')
print('A', 'B', 'C', 'D', 'E', sep='')

print()

# end
print('Hello', end=' ')
print('World', end='')

print()

# format
# d: 정수
# s: 문자열
# f: 실수
print('%d %d' % (1, 2))
print('{} {}'.format ('Hello', 'World'))
print('{1} {0}'.format ('second', 'first'))
