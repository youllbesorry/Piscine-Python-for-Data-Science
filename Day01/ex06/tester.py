from ft_filter import ft_filter

ages = [5, 58, 12, 17, 18, 24, 32]

def ageCheck(x):
  if x < 18:
    return False
  else:
    return True

adults = ft_filter(ageCheck, ages)

for x in adults:
  print(x) 