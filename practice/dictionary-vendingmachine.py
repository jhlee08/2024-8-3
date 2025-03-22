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

def user_login():
    print("사용자 모드에 진입합니다.")
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
        print("유통기한이 지난 음료가 없습니다")
    elif an == "NO":
        nu = input("관리자모드를 종료후 사용자 모드로 전환하겠습니까?")
        if an == "YES":
            switch_mode()
            user_login()
else:
    user_input == "user"
    print("음료의 종류는 콜라 사이다 미린다 밀키스 레몬워터입니다")
    if user_input == input("음료를 선택해주세요"):
        if user_input == "콜라":
            print("가격은 2000원입니다")
            nu_drink = int(input("몇개를 구매하실건가요?"))
"""
"""
class VendingMachine:
    def __init__(self):
        self.items = {
            "커피": {"가격": 500, "재고": 10},
            "탄산음료": {"가격": 700, "재고": 8},
            "생수": {"가격": 1000, "재고": 5},
            "주스": {"가격": 1200, "재고": 7}
        }
        self.balance = 0

    def display_items(self):
        print("\n=== 자판기 메뉴 ===")
        for item, info in self.items.items():
            print(f"{item}: {info['가격']}원 (재고: {info['재고']}개)")
        print("===================")

    def insert_money(self, amount):
        if amount <= 0:
            print("올바른 금액을 넣어주세요.")
            return
        self.balance += amount
        print(f"현재 투입된 금액: {self.balance}원")

    def purchase(self, item):
        if item not in self.items:
            print("해당 음료는 없습니다.")
            return

        price = self.items[item]["가격"]
        stock = self.items[item]["재고"]

        if stock <= 0:
            print(f"{item}의 재고가 부족합니다.")
            return

        if self.balance < price:
            print(f"잔액이 부족합니다. {price - self.balance}원 더 필요합니다.")
            return

        self.balance -= price
        self.items[item]["재고"] -= 1
        print(f"{item}을(를) 구매했습니다. 남은 잔액: {self.balance}원")

    def refund(self):
        if self.balance > 0:
            print(f"잔돈 {self.balance}원을 반환합니다.")
            self.balance = 0
        else:
            print("반환할 금액이 없습니다.")

    def check_balance(self):
        print(f"현재 잔액: {self.balance}원")

    def restock(self, item, amount):
        if item in self.items:
            self.items[item]["재고"] += amount
            print(f"{item}의 재고가 {amount}개 추가되었습니다. 현재 재고: {self.items[item]['재고']}개")
        else:
            print("해당 음료는 자판기에 없습니다.")


# 자판기 실행
def run_vending_machine():
    vm = VendingMachine()
    vm.display_items()

    while True:
        action = input("동작을 선택하세요 (돈넣기/구매/잔액확인/재고추가/반환/종료): ").strip()
        if action == "돈넣기":
            amount = int(input("투입할 금액을 입력하세요: "))
            vm.insert_money(amount)
        elif action == "구매":
            item = input("구매할 음료 이름을 입력하세요: ").strip()
            vm.purchase(item)
        elif action == "잔액확인":
            vm.check_balance()
        elif action == "재고추가":
            item = input("재고를 추가할 음료 이름을 입력하세요: ").strip()
            amount = int(input("추가할 개수를 입력하세요: "))
            vm.restock(item, amount)
        elif action == "반환":
            vm.refund()
        elif action == "종료":
            vm.refund()
            print("자판기 이용을 종료합니다.")
            break
        else:
            print("잘못된 입력입니다. 다시 시도하세요.")


# 자판기 프로그램 실행
if __name__ == "__main__":
    run_vending_machine()
"""




user_input = input("모드를 입력해주세요")
if user_input == "manager":
    switch_mode()
    manager_login()
    an = input("유통기한이 지난 음료가 있는지 확인할까요?")
    if an == "YES":
        print("유통기한이 지난 음료가 없습니다")
    elif an == "NO":
        nu = input("관리자모드를 종료후 사용자 모드로 전환하겠습니까?")
        if an == "YES":
            switch_mode()
            user_login()
def buy_drink(drink_key: int):
    coin = 0
    while price[drink_key] > coin:
        print("금액을 입력하세요")
        coin = coin + int(input(">>"))

    print(coin - price[drink_key], "원을 반환합니다")
def select_drink():
    global inventory

    drink = int(input("메뉴를 선택하세요"))

    if drink == 1:
        drink_key = 'coke'
       # inventory.update({'coke': inventory['coke'] + 1})
    elif drink == 2:
        inventory['chill sung'] = inventory['chill sung'] + 1
    elif drink == 3:
        inventory['chocolate milk'] = inventory['chocolate milk'] + 1
    elif drink == 4:
        inventory['strewberry milk'] = inventory['strewberry milk'] + 1
    elif drink == 5:
        inventory['banana milk'] = inventory['banana milk'] + 1


    if inventory[drink_key] == 0:
        print("선택한 음료의 수량이 부족합니다.")
        return -1
    else:
        inventory[drink_key] =inventory[drink_key] -1
        return drink_key

def buy_drink(drink_key: int):
    coin = 0
    while price[drink_key] > coin:
        print("금액을 입력하세요")
        coin = coin + int(input(">>"))

    print(coin - price[drink_key], "원을 반환합니다")



