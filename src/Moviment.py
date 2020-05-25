import numpy as np
import matplotlib.pyplot as plt

def someNone(arr):
  for elem in arr:
    if elem == None: return True
  return False

def line_MRU( X_i, v, dt):
  if X_i  == None or v  == None or dt == None: return X_i
  return v * dt + X_i

def space_MRU(pos, v, dt):
  final_pos = []
  for i in range(len(pos)):
    final_pos.append(line_MRU(pos[i], v[i], dt))
  return final_pos

def line_MRUV(X_i, V_i, a, dt):
  if someNone([X_i, V_i, dt]): return X_i
  if a == None: return space_MRU(X_i, V_i, dt)
  return X_i + V_i * dt + a * (dt ** 2) / 2

def space_MRUV(pos, vel, acc, dt):
  arr = []
  for i in range(len(pos)):
    arr.append(line_MRUV(pos[i], vel[i], acc[i], dt))
  return arr

def metodo_de_Euler(xi, vi, f_a, int):
  x, v, a = [xi], [vi], [f_a(int[0])]
  t = np.linspace(int[0], int[1], 100)
  dt = t[1] - t[0]
  for i in range(len(t)):
    x.append(x[-1] + v[-1] * dt + a[-1] * (dt ** 2) / 2)
    v.append(v[-1] + a[-1] * dt)
    a.append(f_a(t[i]))
  return (x, v, a, dt, t)

def a(t):
  return 10 * t

total = metodo_de_Euler(0, 0, a, (0,1))
t, s = total[0], total[4]

plt.plot(t, s, 'ro')
plt.show()
