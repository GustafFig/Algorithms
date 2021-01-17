import numpy as np

def fac(k):
  prod = 1
  if (k == 0 or k == 1):
    return prod
  for factor in range(1, k + 1):
    prod *= factor
  return prod

def element(n, exp): return 1 / n ** exp

def Z(s, until = 100):
  sum = 0
  for position in range(1, until):
    sum += element(position, s)
  return sum

def prime_element(n, exp): return 1 / (1 - 1 / n ** exp)

def Z_prime(s, until = 100):
  product = 1
  for position in range(1, until):
    product *= prime_element(position, s)
  return product

def signal(exp):
  if (exp % 2 == 0):
    return 1
  else:
    return -1

def Sum_inner(s, n):
  sum_i = 0
  for k in range(n + 1):
    sum_i += signal(k) * (fac(n) / (fac(k) * fac(n - k))) * ((k + 1) ** -s)
  return sum_i

def Zeta(s, until = 100):
  sum = 0
  for n_outer in range(until):
    sum += (1 / 2 ** (n_outer + 1)) * Sum_inner(s, n_outer)
  return (1 / (1 - 2 ** (1 - s))) * sum
