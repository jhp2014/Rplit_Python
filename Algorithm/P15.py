n, m = map(int, input().split())
rice_cakes = list(map(int, input().split()))

left, right = 0, max(rice_cakes)
mid = 0
result = 0
while left < right:
    total = 0
    mid = (left + right) // 2
    
    for rice_cake in rice_cakes:
        remain = rice_cake - mid 
        if remain > 0:
            total += remain

    if total >= m:
        result = mid
        left = mid + 1
    else:
        right = mid - 1

print(result)