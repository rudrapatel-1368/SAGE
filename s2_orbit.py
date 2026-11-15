#From the paper of The GRAVITY Collaboration
import math as m
import matplotlib.pyplot as plt 

M = 4.154e6
a_arcsecs = 0.125072
d_pc = 8179 
ecc = 0.884282            

GM = 4*(m.pi**2)*M
a = a_arcsecs * d_pc

r_close = a * (1 - ecc)
r_far = a * (1 + ecc)

print("a =", a)
print("closest =", r_close)
print("farthest =", r_far)

v_far = m.sqrt(GM / a * (1 - ecc) / (1 + ecc))

x, y = r_far, 0.0          
vx, vy = 0.0, v_far        
dt = 0.0001
steps = int(16.0518 / dt)  # one full orbit

r_min = r_far
xs = []
ys = []
for i in range(steps):
    r = m.sqrt(x**2 + y**2)
    ax = -(GM *x/r**3)
    ay = -(GM*y/r**3)
    vx = vx + ax*dt
    vy = vy + ay*dt 
    x = x + vx*dt 
    y = y + vy*dt
    xs.append(x)
    ys.append(y)
    if r < r_min:
        r_min = r

print("v_far =", v_far)
print("end:", x, y)
print("closest:", r_min)

plt.plot(xs, ys)
plt.plot(0, 0, "ko")
plt.gca().set_aspect("equal")
plt.title("S2 orbit around Sgr A*")
plt.xlabel("x (AU)")
plt.ylabel("y (AU)")
plt.savefig("s2_orbit.png", dpi=200)
plt.show()