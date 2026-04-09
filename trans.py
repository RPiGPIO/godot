#2d transformations
import math
# Original point
x = 5
y = 3
# Translation
tx, ty = 2, 4
x_t = x + tx
y_t = y + ty
print("Translated:", x_t, y_t)
# Scaling
sx, sy = 2, 2
x_s = x * sx
y_s = y * sy
print("Scaled:", x_s, y_s)
# Rotation (45 degrees)
theta = math.radians(45)
x_r = x*math.cos(theta) - y*math.sin(theta)
y_r = x*math.sin(theta) + y*math.cos(theta)
print("Rotated:", round(x_r, 2), round(y_r, 2))



#3d transformations
import math
# Original point
x = int(input("Enter x = "))
y = int(input("Enter y = "))
z = int(input("Enter z = "))
# Translation
tx, ty, tz = 5, 2, 1
x_t, y_t, z_t = x+tx, y+ty, z+tz
print("Translated:", x_t, y_t, z_t)
# Scaling
sx, sy, sz = 2, 2, 3
x_s, y_s, z_s = x*sx, y*sy, z*sz
print("Scaled:", x_s, y_s, z_s)
# Rotation about Z-axis (45°)
theta = math.radians(45)
x_r = x*math.cos(theta) - y*math.sin(theta)
y_r = x*math.sin(theta) + y*math.cos(theta)
z_r = z
print("Rotated (Z-axis):", round(x_r,2), round(y_r,2), z_r)
