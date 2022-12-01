#부품 찾기

n = int(input())
part = list(map(int, input().split()))
m = int(input())
request = list(map(int, input().split()))

result = []
for i in request:
    if i in part:
        result.append("yes")
    else:
        result.append("no")

print(result)
