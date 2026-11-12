#From the paper of GRAVITY collaboration
import math as m

GM = 4*m.pi**2
x, y = 1.0, 0.0
vx, vy = 0, 6.28
dt = 0.001
steps = 10000

for i in range(steps):
    r = m.sqrt(x**2 + y**2)
    ax = -(GM*x)/(r**3)
    ay = -(GM*y)/(r**3)
    vx = vx + ax*dt
    vy = vy + ay*dt
    x = x + vx*dt
    y = y + vy*dt
    

print(x, y) #0.9999265199771726 0.009361057497866894 i.e came back
print(m.sqrt(x**2 + y**2)) #0.99997033693562 so the distance is 1AU 