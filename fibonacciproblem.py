# Farmer John learned about the Fibonacci sequence when he was reading about some broccoli and pineapples that he plans to grow. 
# The Fibonacci sequence F0,F1,F2,… has F0=0 and F1=1, and then for i>1, Fi=Fi−2+Fi−1. 
# That is, each subsequent term is defined to be the sum of the two terms preceding it: F2=0+1=1,F3=1+1=2,F4=1+2=3,F5=2+3=5,F6=3+5=8,F7=5+8=13….  
#Farmer John wants to experiment with the first two terms of the sequence, so he has invented his own "Fibjohnacci sequence" {J0,J1,J2,…}. 
# It is defined exactly like the Fibonacci sequence, except that Farmer John has picked his own two starting terms J0 and J1 (1≤J0≤9,1≤J1≤9).  
	   
#Farmer John wants to find term JN (2≤N≤1018) of the Fibjohnacci sequence. 
# Like the Fibonacci sequence, the Fibjohnacci sequence can grow very rapidly, so this term might be enormous. 
# Therefore Farmer John only wants to know the last digit of JN.

jo = int(input())
ji = int(input())
n = int(input())
def solve(jo, ji, n):
    seen = set()
    e = 0
    starto = jo
    starti = ji
    while (jo,ji) not in seen:
        seen.add((jo, ji))  
        jo, ji = ji%10, (jo + ji) % 10
        e += 1
    jo = starto 
    ji = starti
    n = n % e
    if n == 0:
        n=e
    for i in range(0,n-1):    
        jo, ji = ji%10, (jo + ji) % 10
    return (ji%10)
print(solve(jo,ji,n))
