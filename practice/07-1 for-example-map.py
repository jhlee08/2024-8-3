# 벽은 #, 캐릭터 @, 빈공간 *
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
        if tmpX > 10 or tmpX < 0:
            print("map의 범위를 벗어날 수 없습니다.")
        else:
            X = tmpX

        tmpY = Y+dy[index]
        if tmpY > 10 or tmpY < 0:
            print("map의 범위를 벗어날 수 없습니다.")
        else:
            Y = tmpY

    print("현재 위치 : (",X,",",Y,")" )

print("프로그램을 종료합니다.")
"""

map = [[1,1,1,1,1,1,1,1,1,1,],
       [1,1,1,1,1,1,1,1,1,1,],
       [1,1,1,1,1,1,1,1,1,1,],
       [1,1,1,1,1,1,1,1,1,1,],
       [1,1,1,1,1,1,1,1,1,1,],
       [1,1,1,1,1,1,1,1,1,1,],
       [1,1,1,1,1,1,1,1,1,1,],
       [1,1,1,1,1,1,1,1,1,1,],
       [1,1,1,1,1,1,1,1,1,1,],
       [1,1,1,1,1,1,1,1,1,1,]]
X = 0
Y = 0

'''
X가 2고, Y가 0일때 예상 출력 결과:
############
#**********#
#**********#
#**********#
#**********#
#**********#
#**********#
#**********#
#**********#
#**********#
#**@*******#
############
'''
def print_map():
    for i in range(1,10):
        print("")


user_input = ""

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
        if tmpX > 10 or tmpX < 0:
            print("map의 범위를 벗어날 수 없습니다.")
        else:
            X = tmpX

        tmpY = Y+dy[index]
        if tmpY > 10 or tmpY < 0:
            print("map의 범위를 벗어날 수 없습니다.")
        else:
            Y = tmpY

    print_map()

print("프로그램을 종료합니다.")

