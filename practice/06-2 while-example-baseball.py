#야구게임
#
# 3자리의 랜덤숫자가 정답이고, 그 3개의 숫자는 겹치지 않음
#
# ---------- 기본 틀 -------------------
#
# 1. 정답을 랜덤으로 생성
# -> 각 자리수의 숫자가 겹치면 안됨.
# -> 겹쳤을때 어떻게 할것인가 or 안겹치게 어떻게 생성을 할것인가
#
# 2. 사용자의 입력을 받아야함.
# -> 숫자가 있는지 -> 그 숫자가 그 자리인지
# -> 결과에 따른 출력
#
# 3. 사용자가 종료 입력을 하면 종료
# -> 사용자가 정답을 맞춘 이후에 다음문제 출제
#
# ---------- 응용 -------------------
# 4. turn 수 제한
# -> 10번으로 제한, 10번안에 못맞추면 fail

"""
import random
a = random.randrange(1,9)
b = random.randrange(1,9)
c = random.randrange(1,9)
while print(a != b != c):
    if a == b or b == c or c == a
"""
"""
result = 0
import random

# result % 10 일의 자리
##  (result // 10) % 10 십의 자리
###  result // 100 백의 자리

while result // 100 == (result // 10) % 10 or result // 100 == result % 10 or (result // 10) % 10 == result % 10:
    result = random.randrange(1,1000)
    print(result)

user_input = input("값을 맞춰보세요 ::")

S = 0
B = 0
"""

import random

result = [0,0,0]
while result[0] == result[1] or result[1] == result[2] or result[2] == result[0]:
    result[0] = random.randrange(1,10)
    result[1] = random.randrange(1,10)
    result[2] = random.randrange(1,10)

S = 0

while S !=3:
    user_input2 = int(input("정답을 맞춰보세요"))
    user_input = [user_input2 // 100, (user_input2 // 10) % 10, user_input2 % 10]
    print(user_input)

    S = 0
    B = 0

    if result[0] == user_input[0]:
        S = S + 1
    elif result[0] == user_input[1] or result[0] == user_input[2]:
        B = B + 1

    if result[1] == user_input[1]:
        S = S + 1
    elif result[1] == user_input[0] or result[1] == user_input[2]:
        B = B + 1

    if result[2] == user_input[2]:
        S = S + 1
    elif result[2] == user_input[0] or result[2] == user_input[1]:
        B = B + 1

    if S == 3:
        print("정답입니다!")
    else:
        print("S ",S, " B",B)
