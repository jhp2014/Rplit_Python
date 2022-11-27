n, m = map(int, input().split())
x, y, dir = map(int, input().split())
arr = []

for _ in range(n):
  arr.append(list(map(int, input().split())))

cnt = 1
turn = 0
#현재 방향에서 왼쪽 방향
dx = [0, -1, 0, 1]
dy = [-1, 0, 1, 0]

#예외 처리
if arr[x][y] == 1:
  print(0)
  

while True:
  arr[x][y] = 2  #방문처리
  print(arr)
  nx = x + dx[dir]
  ny = y + dy[dir]
  print("nx , ny = " + str(nx) + "," + str(ny) + ": " + str(x) +","+ str(y))
  if arr[nx][ny] == 0:
    print("arr[nx][ny] = " + str(arr[nx][ny]))
    x = nx
    y = ny
    cnt += 1
    dir = (dir + 3) % 4  #방향 전환
    turn = 0

  elif arr[nx][ny] != 0 and turn != 4:
    turn += 1
    dir = (dir + 3) % 4

  elif arr[nx][ny] != 0 and turn == 4:
    #뒤로가기
    turn = 0
    nx = x + dx[(dir + 3) % 4]
    ny = y + dy[(dir + 3) % 4]
    
    if arr[nx][ny] == 1:
      break
    else:
      x = nx
      y = ny

print(cnt)