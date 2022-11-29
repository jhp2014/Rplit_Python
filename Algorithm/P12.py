#성적이 낮은 순서로 학생 출력

n = int(input())
lst = []

for _ in range(n):
  name, score = input().split()
  score = int(score)
  lst.append((name,score))


lst.sort(key = lambda x: x[1])

for name in lst:
  print(name[0], end=' ')