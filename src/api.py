def someNone(arr):
  for elem in arr:
    if elem == None: return True
  return False

def analyze(callback, values, objective = None):
  result = callback(values)
  print('function: ', result)

  if objective:
    print('objective: ', objective)
    print('result - objective: ', result - objective)
    print('result is Bigger: ', result > objective)

def fac(k):
  prod = 1
  if (k == 0 or k == 1):
    return prod
  for factor in range(1, k + 1):
    prod *= factor
  return prod
