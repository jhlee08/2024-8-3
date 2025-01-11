#함수 사용 방법

"""
def calculate(x):
    return 3*x + 5

print( calculate(5))
print( calculate(3))
print( calculate(1))

# python generate_random_value() is_number()
# java generateRandomvalue() isNumber()

print("#################################")
"""
# 커피(음료)를 자동으로 만들어주는 기계를 만든다고 가정



def put_esspresso():
    print("espresso")


def warm_up():
    print("음료를 데웁니다.")


def add_ice():
    print("얼음을 넣습니다.")


def add_esspresso():
    print("espresso를 넣습니다.")


def add_water():
    print("물을 넣습니다.")


def add_milk():
    print("우유를 넣습니다.")


def add_cocoa():
    print("코코아를 넣습니다")


# 사용자에게 메뉴를 주문을 받습니다
# 이때,
# 에스프레소: 에스프레소를 넣고
# 아이스 아메리카노 : 얼음을 넣고 -> 물을 넣고 -> 에스프레소를 넣으면 완성
# 핫 모카라떼: 우유를 넣고 -> 데우고 -> 에스프레소 -> 코코아
# 아이스 라떼: 얼음을 넣고 -> 우유를 넣고 -> 에스프레소
# 아이스 코코아: 얼음을 넣고 -> 우유를 넣고 -> 코코아를 넣고


print("에스프레소, 아이스 아메리카노, 핫 아메리카노, 핫 모카라떼, 아이스 라떼, 아이스 코코아")
user_input = input("원하시는 메뉴를 입력해주세요 ::")
if user_input == "에스프레소":
    add_esspresso()
if user_input == "아이스 아메리카노":
    add_ice()
    add_water()
    add_esspresso()
if user_input == "핫 아메리카노":
    add_water()
    add_esspresso()
    warm_up()
if user_input == "핫 모카라떼":
    add_milk()
    warm_up()
    add_esspresso()
    add_cocoa()
if user_input == "아이스 라떼":
    add_ice()
    add_milk()
    add_esspresso()
if user_input == "핫 라떼":
    add_milk()
    add_esspresso()
    warm_up()
if user_input == "아이스 코코아":
    add_ice()
    add_milk()
    add_cocoa()