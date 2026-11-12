#From the paper of The GRAVITY Collaboration
import math as m

M = 4.154e6               # black hole mass, solar masses
a_deg = 0.12507
d_pc = 8179               # distance to Galactic Centre, parsecs
ecc = 0.884282            # eccentricity (called ecc, not e, to avoid confusion)

GM = 4*(m.pi**2)*M
a = a_deg * d_pc

r_close = a * (1 - ecc)
r_far = a * (1 + ecc)

print("a =", a)
print("closest =", r_close)
print("farthest =", r_far)