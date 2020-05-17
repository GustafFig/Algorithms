def line_MRU( X_i, v, dt):
  if X_i  == None or v  == None or dt == None: return X_i
  return v * dt + X_i

def space_MRU(v, pos, dt):
  final_pos = []
  for i in range(len(pos)):
    final_pos.append(line_MRU(pos[i], v[i], dt))
  return final_pos

print(space_MRU((None, 2, 3), (0, 10, 6), 1))
