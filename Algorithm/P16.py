n = int(input())
dp = [float('inf')] * (n + 1)

for num in range(2, n+1):
    if num % 5 == 0:
        temp = num // 5
        if temp == 1:
            dp[num] = 1
            continue
        else:
            dp[num] = min(dp[num], dp[temp] + 1)
    
    if num % 3 == 0:
        temp = num // 3
        if temp == 1:
            dp[num] = 1
            continue
        else:
            dp[num] = min(dp[num], dp[temp] + 1)
        
    if num % 2 == 0:
        temp = num // 2
        if temp == 1:
            dp[num] = 1
            continue
        else:
            dp[num] = min(dp[num], dp[temp] + 1)

    temp = num - 1
    if temp == 1:
        dp[num] = 1
    else:
        dp[num] = min(dp[num], dp[temp] + 1)

print(dp[n])
    