fin = open("speeding.in", "r")
seg = fin.readline().split()
n = int(seg[0])
m = int(seg[1])
limit = []
for a in range(n):
    road = fin.readline().split()
    length = int(road[0])
    speed_limit = int(road[1])
    for b in range(length):
        limit.append(speed_limit)
speed = []
for c in range(m):
    road = fin.readline().split()
    length = int(road[0])
    s = int(road[1])
    for b in range(length):
        speed.append(s)
answer = 0
for i in range(100):
    answer = max(answer, speed[i] - limit[i])

if answer < 0:
    answer = 0

fout = open("speeding.out", "w")
fout.write(str(answer) + "\n")
fout.close()
