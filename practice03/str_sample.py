# 문자형

str1 = "Hello World!"
str2 = 'Hello World!'
str3 = """Hello World!"""
str4 = '''Hello World!'''

print(type(str1), type(str2), type(str3), type(str4))
print(len(str1))
print()

str_empty1 = ''
str_empty2 = str()

print(type(str_empty1), len(str_empty1))
print(type(str_empty2), len(str_empty2))
print()

print("I'm sample!")
print('I\'m sample!')
print('Hello \t World')

# 멀티라인 입력
multi_str1 = """
문자열
멀티
입니다.
"""
multi_str2 = \
    """
    문자열
    멀티
    입니다.
    """
print(multi_str1)
print(multi_str2)
