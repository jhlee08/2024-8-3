a = [100, 96, 87, 100, 123, 1231, 31231, 31231]

print(a[0])
print(a[1])

print(a)
print(a[0:5]) # a[N:M] a의 n번째 요소부터 n-1번째 요소까지
print(a[4:5])
print(a[3:])
print(a[:4])


b = [[100, 87, 98, 99, 95],[75, 68, 91, 83, 88], [90, 79, 75, 82, 85] ]


print(b[0][1])
print(b[1])
print(b[0][2:])
print(b[0][1:])

c = [[[100, 87, 98, 99, 95],75, 68, 91, 83, 88], [100, 87, 98, 99, 95],[75, 68, 91, 83, 88]]

print('================')
d = [13, 12, 51, 32, 44]
e = d

d[1] = 10

print(d)
print(e)

f = a + b
print(f)

g = a + b
print(g)

h = d * 3
print(h)

print(len(a))
print(len(b))
print(len(b[0]))


print("=================")

text = "commit failed with error"
print(text[5])
print(text[10:])

text = text.replace("m",  "s", 1)
print(text)
