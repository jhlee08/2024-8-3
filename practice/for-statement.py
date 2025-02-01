# 선생님 너네들 태도 점수를 점수에 넣겠다. (수행평가)
# 1학기에 점수 배점이 중간 30 / 기말 30 / 배드민턴 30 / 태도점수 10
# 어느 날 체육선생님이 아주 기분이 안좋은 날에
# 그 전시간 수학선생님이 설명을 너무 열심히 하는 바람에
# 단체로 체육시간에 늦음.
# 체육선생님의 일괄적으로 1점씩 깎겠다.
"""
attitudes = [9,9,9,8,9,9,8,9,9,9]

for attitude in attitudes:
    print(attitude)
    attitude = attitude + 1

print("attitude에 값을 더한 것 - attribute: call by value")
print(attitudes)

for i in range(len(attitudes)):
    attitudes[i] = attitudes[i] + 1

print("attitudes에 더한 값을 넣어준 것 - attribute[i]: call by reference")
print(attitudes)
"""


d = {"key":"value", 2.3: "value", 5:1, 5:"111"}
print(d)

print(d.keys())
print(d.values())

"""
# 자판기 프로그램을 할 것
# 사용자모드 / 관리자모드
# 사용자모드 - 물건 구매
# 관리자모드 - 물건 추가, 물건 가격 변동

1. 사용자모드 - 남아있는 음료가 없으면 재고가 없다고 말한다
            - 해당하는 음료가 없으면 다시 입력 받는다
            - 카드 or 페이 or 현금 결제인지 선택
2. 관리자모드 - 유통기한이 지난 음료가 있다면 버리기
            - 랜덤 물건 뽑기 기능 추가 
            
"""
inventory= {}



