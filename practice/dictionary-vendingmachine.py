"""
d = {"key": "value", 2.3: "value", 5: 1, 5: "111"}
print(d)

print(d.keys())
print(d.values())


# 자판기 프로그램을 할 것
# 사용자모드 / 관리자모드
# 사용자모드 - 물건 구매
# 관리자모드 - 물건 추가, 물건 가격 변동
# 음료수 종류: 콜라 사이다 미린다 밀키스 레몬워터 
1. 사용자모드 - 남아있는 음료가 없으면 재고가 없다고 말한다
            - 해당하는 음료가 없으면 다시 입력 받는다
            - 카드 or 페이 == 잔액 있을 때: 결제완료 표시후 물건 제공 
                            잔액 없을 때: 다른 결제 수단을 사용해달라고 말하기
            - 랜덤 물건 뽑기 기능 
2. 관리자모드 - 유통기한이 지난 음료가 있다면 버리기


"""
inventory = {'coke':10, 'cider':10, 'mirinda':5, 'milkis':0, 'lemonwater':3}
price = {'coke':1000, 'cider':900, 'mirinda':700, 'milkis':800, 'lemonwater':600}


def print_menu():
    print("menu를 출력합니다.")
    for i in inventory.keys():
        print(i, "가격:", price[i], " 잔여수량:", inventory[i])

def buy_drink():
    print("음료를 선택하고, 구매합니다.")

def switch_mode():
    print("모드를 전환합니다.")

def manager_login():
    print("관리자 모드에 진입합니다.")

def print_function():
    print("관리자가 사용가능한 기능을 출력합니다.")
    print("1. 음료를 등록하기")
    print("2. 음료를 추가하기")
    print("3. 사용자 모드로 전환")

def change_price():
    print("음료의 가격을 변경합니다.")

def add_drink():
    print("음료를 추가합니다.")

def register_drink():
    print("음료를 등록합니다.")

def delete_drink():
    print("음료를 삭제합니다.")

def extract_drink():
    print("음료를 뺍니다.")
"""
user_input = input("모드를 입력해주세요")
if user_input == "manager":
    switch_mode()
    manager_login()
    an = input("유통기한이 지난 음료가 있는지 확인할까요?")
    if an == "YES":
        
    elif an == "No":
        nu = input("관리자모드를 종료후 사용자 모드로 전환하겠습니까?")
"""



