
import numpy as np

x = np.array([[1,2],[3,4]])
y = np.array([[4,3],[2,1]])

z1 = x+y
print(f"Add {z1}")

z2 = x*2
print(f"scale: {z2}")

z3 = y-x
print(f"Subtract: {z3}")

z4 = x*y
print(f"Multiply: {z4}")

z5 = np.dot(x,y)
print(z5)