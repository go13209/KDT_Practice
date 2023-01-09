# 실습 문제 1
# 문자열을 입력받고, e가 처음 나오는 위치(index)를 출력하세요. 만약, 문자열에서 e가 없으면 -1을 출력하세요.
# 단, index() / find() 메서드는 사용하지 마세요.
string = input()
dict = {}
cnt = 0
for char in string[0:]:
    if char not in dict:
        dict[char] = cnt
        cnt += 1
    else:
        cnt += 1

if 'e' in dict.keys():
    print(dict['e'])
else:
    print(-1)


# 실습 문제 2
# 문자열을 입력받고, 각 단어의 등장 횟수를 출력하세요.
# 단, count() 메서드는 사용하지 마세요.
words = input().split()
dict = {}

for word in words:
    if word not in dict:
        dict[word] = 1
    else:
        dict[word] += 1
    
for key, value in dict.items():
    print(key, value)


# 실습 문제 3
# 문자열을 입력받고, e를 제거한 결과를 출력하세요.
# 단, replace() 메서드는 사용하지 마세요.
string = input()
list = []

for char in string[0:]:
    if char != 'e':
        list.append(char)

for char in list:
    print(char, end='')


# 실습 문제 4
# 문자열과 알파벳을 공백으로 구분해서 입력받고, 문자열에서 입력한 알파벳의 개수를 출력하세요.
# 단, count() 메서드는 사용하지 마세요.
string = input().split()
cnt = 0
list = []
for char in string[0][0:]:
    list.append(char)

for i in list:
    if i == string[1]:
        cnt += 1
print(cnt)


# 실습 문제 5
# 양의 정수 3개를 입력받고, 3개의 양수를 -(hyphen)으로 연결해서 출력하세요.
# 단, join() 메서드는 사용하지 마세요.
number = input().split()
print(f'{number[0]}-{number[1]}-{number[2]}')


# 실습 문제 6
# 양의 정수를 입력받고, 자릿수의 합을 출력하세요. 만약, 입력받은 값이 0보다 작으면 -1을 출력하세요.
# 단, 양의 정수를 문자열로 변경하지 마세요. str() 함수를 사용하지 마세요.
number = input()
list = []
sum = 0
if int(number) < 0:
    print(-1)
else:
    for i in number[0:]:
        list.append(i)
    for i in list:
        sum = sum + int(i)
    print(sum)