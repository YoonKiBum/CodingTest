n = int(input())
data = []
for _ in range(n):
  name, kor, eng, math = input().split()
  data.append((name, int(kor), int(eng), int(math)))

data.sort(key = lambda x: (-x[1], x[2], -x[3], x[0]))

for i in range(n):
  a, b, c, d = data[i]
  print(a)
