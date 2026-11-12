#From the paper of GRAVITY collaboration
import math as m

G = 4*m.pi**2
theta = 0.125072 #mas -> degrees
d = 8179 #pc
a = theta * d
T = 16
M = (a**3)/(T**2)

print(M) #4181585.1337360134