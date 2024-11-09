# 수학 성적이 비정상적인 입력인 경우 다시 입력을 받는다.

"""num = -1


while num > 100 or num < 0:
    num = int(input("수학 성적을 입력해주세요. ::"))

if num > 80:
    print("A반입니다.")
elif num > 60:
    print("B반입니다.")
else:
    print("C반입니다.")
"""
"""
import random

answer = random.randrange(1,100)
nu = int(input("예상 숫자를 입력해주세요"))
print(answer)
while answer != nu:
    answer = int(random.randrange(1, 100))
    nu = int(input("예상 숫자를 입력해주세요"))
    print(answer)
if answer == nu:
    print("correct")
"""

# up/down
# value = 10
# answer = 50
# down
# answer = 5
# up

# 100 미만의 피보나치 수열 출력하기
"""
Fibonacci = 1
n = 0
m = 0

while Fibonacci < 100:
    print(Fibonacci)
    m = n
    n = Fibonacci
    Fibonacci = m + n
"""
"""
fibonacci_list = [1,1]
n = 1

while fibonacci_list[n-1]+fibonacci_list[n] < 100:
    fibonacci_list.append(fibonacci_list[n-1]+fibonacci_list[n])
    n = n + 1
    print(fibonacci_list)

# 사용자에게 숫자 하나를 입력받아서
# 해당 숫자만큼 * 출력하기
"""
"""
count = int(input("숫자 하나를 입력하세요>>"))
i = 0

while i < count:
    print("*")
    i = i + 1
"""

# (0,0) 시작
# 사용자가 UP 입력하면 위로, DOWN 입력하면 아래로, LEFT 입력하면 왼쪽으로, RIGHT 입력하면 오른쪽으로
# MAP의 범위는 (0,0)~(100,100)
# (0,0) 가장 왼쪽으로 아래, (100,100) 가장 오른쪽의 위
# 1. 잘못일력하면 처리x
# 2. 맵 밖에 못나가게 처리 (0,0) 에서 아래 누르면 잘못된 방향이라고 알려주고 (0,0) 유지
# EXIT 입력하면 종료
"""
X = 0
Y = 0
print((X,Y))
ans = ""
ans = str(input("어디쪽으로 이동할지 입력해주세요"))
while 0 < X < 100 and  0 < Y < 100:
    if ans == "up":
        Y = Y + 1
        print((X, Y))
    if ans == "down":
        Y = Y - 1
        print((X,Y))
    if ans == "left":
        X = X - 1
        print((X, Y))
    if ans == "right":
        X = X + 1
        print((X, Y))
"""


