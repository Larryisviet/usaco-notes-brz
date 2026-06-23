# https://usaco.org/index.php?page=viewproblem2&cpid=856



fin = open("blist.in", "r")
n = int(fin.readline())
buckets = [0] * 1001
answ = 0
for i in range(n):
  line = fin.readline().split()
  si = int(line[0])
  ti = int(line[1])
  bi = int(line[2])
  for t in range(si, ti+1):
    buckets[t] += bi
for a in range(1000):
  answ = max(answ, buckets[a])
fout = open("blist.out", "w")
fout.write(str(answ) + "\n")
fout.close()
  
