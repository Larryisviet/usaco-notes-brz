seg = input().split()
n = int(seg[0])
m = int(seg[1])
limit = []
for a in range(n):
    road = input().split()
    length = int(line[0])
    speed_limit = int(line[1])
    for b in range(length):
        limit.append(speed_limit)
speed = []
for c in range(m):
  road = input().split()
  length = int(line[0])
  s = int(line[1])
  for b in range(length):
        speed.append(s)
answer = 0
for i in range(100):
    answer = max(answer, speed[i] - limit[i])
return answer
