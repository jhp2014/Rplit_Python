n, m, k = map(int, input().split())

data = list(map(int, input().split()))

data.sort(reverse=True)

first = data[0]
second = data[1]

result = 0

for i in range(m):
  if i != 0 and i % k == 0:
    result += second
  else:
    result += first

print(result)