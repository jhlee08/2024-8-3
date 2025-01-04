for i in range(10):
    print(i+1)

print("################")

for i in range(1,11):
    print(i)

print("################")
print(list(range(1,11)))

## 여기서 부터는 조건을 같이 넣는다
# 3,6,9게임
# 1, 2, 짝(3)
# 1~100
# 33 -> 짝짝
for i in range(1,101):
    if i//10 == 3 or i//10 == 6 or i/10 == 9:
        if i % 10 == 3 or i % 10 == 6 or i % 10 == 9:
            print("짝짝")
        else:
            print("짝")
    else:
        if i%10 == 3 or i%10 == 6 or i%10 == 9:
            print("짝")
        else:
            print(i)

# 사용자한테 숫자 하나를 입력 받아
# 해당 숫자의 구구단을 출력
# 2를 입력받으면
# 2*1=2 - 2*9+18

