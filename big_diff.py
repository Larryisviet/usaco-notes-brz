def big_diff(nums):
  mx = nums[0]
  mn = nums[0]
  for i in range(len(nums)-1):
    mx = max(mx,nums[i+1])
  for i in range(len(nums)-1):
    mn = min(mn,nums[i+1])
  return mx-mn
