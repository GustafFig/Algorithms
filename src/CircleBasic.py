import numpy as np

def take_radio():
  r = float(input('radio = '))
  if r == 0:
    print('it\' is a dot')
  return r

def circunference(r):
  take_radio()
  return 2 * np.pi * r

def area(r):
  take_radio()
  return r ** 2 * np.pi
