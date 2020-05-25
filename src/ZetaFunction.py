import numpy as np

def element(n, exp): return 1 / n ** exp

def Z(s, until = 100):
  sum = 0
  for position in range(1, 100):
    sum += element(position, s)
  return sum

Z_of_two = Z(2)
base = np.pi ** 2 / 6

print('Z function: ', Z_of_two)
print('pi ** 2 / 6: ', base)
print('Z - Sum(1/n**s): ', base - Z_of_two)
print('Sum(1/n**s) is Bigger:', Z_of_two > base)
