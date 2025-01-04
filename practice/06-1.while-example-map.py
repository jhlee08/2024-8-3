"""
X = 0
Y = 0
print((X,Y))
ans = ""
ans = str(input("어디쪽으로 이동할지 입력해주세요"))
while ans != "up" and "down" and "left" and "right":
    ans = str(input("어디쪽으로 이동할지 입력해주세요"))
    if ans == "up":
        Y = Y+1
        print((X,Y))
"""
"""
user_input = ""
X = 0
Y = 0

while user_input != "EXIT":
    while user_input != "EXIT" and user_input != "UP" and user_input != "DOWN" and user_input != "LEFT" and user_input != "RIGHT":
        user_input = input("움직일 방향을 입력하세요 (종료는 EXIT) :: ")
    print(user_input)

    if user_input == "UP":
        if Y < 100:
            Y = Y + 1
        else:
            print("범위를 벗어날 수 없습니다.")
    elif user_input == "DOWN":
        if Y > 0:
            Y = Y - 1
        else:
            print("범위를 벗어날 수 없습니다.")
    elif user_input == "LEFT":
        if X > 0:
            X = X - 1
        else:
            print("범위를 벗어날 수 없습니다.")
    elif user_input == "RIGHT":
        if X < 100:
            X = X + 1
        else:
            print("범위를 벗어날 수 없습니다.")
    user_input = ""
print("프로그램을 종료합니다.")
"""


"""
user_input = ""
X = 0
Y = 0

valid_inputs = ["EXIT", "UP", "DOWN", "LEFT","RIGHT"]

while user_input != "EXIT":
    user_input = ""  # user_input 초기화
    while user_input not in valid_inputs:
        user_input = input("움직일 방향을 입력하세요 (종료는 EXIT) :: ")

    if user_input == "UP":
        if Y < 100:
            Y = Y+1
        else:
            print("map의 범위를 벗어날 수 없습니다.")
    elif user_input == "DOWN":
        if Y > 0:
            Y = Y-1
        else:
            print("map의 범위를 벗어날 수 없습니다.")
    elif user_input =="LEFT":
        if X>0:
            X = X-1
        else:
            print("map의 범위를 벗어날 수 없습니다.")
    elif user_input == "RIGHT":
        if X < 100:
            X = X+1
        else:
            print("map의 범위를 벗어날 수 없습니다.")
    print("현재 위치 : (",X,",",Y,")" )
print("프로그램을 종료합니다.")
"""

"""
user_input = ""
X = 0
Y = 0

directions = ["UP", "DOWN", "LEFT","RIGHT"]
dx = [0,0,-1,1]
dy = [1, -1, 0,0]
valid_inputs = ["EXIT"]+directions

while user_input != "EXIT":
    user_input = ""  # user_input 초기화
    while user_input not in valid_inputs:
        user_input = input("움직일 방향을 입력하세요 (종료는 EXIT) :: ")

    if user_input in directions:
        index = directions.index(user_input)

        tmpX = X+dx[index]
        if tmpX > 100 or tmpX < 0:
            print("map의 범위를 벗어날 수 없습니다.")
        else:
            X = tmpX

        tmpY = Y+dy[index]
        if tmpY > 100 or tmpY < 0:
            print("map의 범위를 벗어날 수 없습니다.")
        else:
            Y = tmpY

    print("현재 위치 : (",X,",",Y,")" )

print("프로그램을 종료합니다.")
"""
