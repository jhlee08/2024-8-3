X = 0
Y = 0
print((X,Y))
ans = ""
ans = str(input("어디쪽으로 이동할지 입력해주세요"))
while ans != "up":
    ans = str(input("어디쪽으로 이동할지 입력해주세요"))
    if ans == "up":
        Y = Y+1


