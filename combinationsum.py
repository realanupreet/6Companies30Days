
res = []

#target is what more of the
def backtrack(num, combination, target):
  if len(combination) == k:
    if target == 0:
      res.append(combination)
    return
  for i in range(num + 1, 10):
    if i <= target:
      backtrack(i, combination + [i], target - i)
    else:
      return

backtrack(0, [], n)
return res
