def take_inputs():
  while True:
    a = float(input('a = '))
    if (a != 0):
      break

  b = float(input('b = '))
  c = float(input('c = '))
  return a, b, c

def quadratic(x):
  a, b, c = take_inputs()
  return a ** x + b * x + c

def quadratic_solver():
  a, b, c = take_inputs()

  delta = (b ** 2 - 4 * a * c)**(1/2)
  return ((-b + delta) / 2 * a, (-b - delta) /2 * a)


print(quadratic_solver())
print(quadratic(quadratic_solver()[1]))
