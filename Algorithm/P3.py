n, m = map(int, input().split())
array = []

for _ in range(n):
  array.append(sorted(list(map(int, input().split())))[0])

print(max(array))


