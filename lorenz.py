import numpy as np
from scipy.integrate import solve_ivp
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

def lorenz(t, xyz, sigma=10, beta=8/3, rho=28):
    x,y,z = xyz
    dx_dt = sigma*(x - y)
    xy_dt = x*(rho - z) - y
    dz_dt = x * y - beta * z
    return dx_dt, xy_dt, dz_dt

t_span = [0, 100]
xyz0 = [1, 1, 1]
print('STEP 1')
sol = solve_ivp(lorenz, t_span, xyz0, t_eval=np.linspace(0, 100, 10000))
print('step2')
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')
ax.plot(sol.y[0], sol.y[1], sol.y[2])
ax.set_xlabel("X")
ax.set_ylabel('Y')
ax.set_zlabel('Z')
plt.show()
print('End')