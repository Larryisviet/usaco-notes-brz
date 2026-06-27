#Farmer John has $N$ cows ($1 \leq N \leq 10^5$), each of which has a unique ID number between $1$ and $10^9$, inclusive.

# Every morning, the cows are supposed to line up from left to right in the order of their ID numbers, from smallest to largest, so that Farmer John can take attendance. 
# However, this morning, the cows are feeling mischievous, and so they might not have lined up in the correct order.

# You are given the ID numbers $A_1, \dots, A_N$ of this morning's line of cows, from left to right. 
# Determine the total number of cows that are not in their correct positions.

ans = 0
n = int(input())
nums = [int(x) for x in input().split()]
y = [int(y) for y in sorted(nums)]
for i in range(n):
  if nums[i] != y[i]:
    ans += 1

print(ans)
