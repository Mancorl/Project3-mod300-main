import numpy as np
import matplotlib.pyplot as plt
from Size_of_atom import Get_dim_and_size_of_atom


H,C,N,O,P,dna_list=Get_dim_and_size_of_atom()

u = np.linspace(0, 2 * np.pi, 100)   
v = np.linspace(0, np.pi, 100)       
u, v = np.meshgrid(u, v)
for i in range(len(H)):
    r=x=H[i][0]
    x=H[i][1]
    y=H[i][2]
    z=H[i][3]
    x_s = x + r * np.sin(v) * np.cos(u)
    y_s = y + r * np.sin(v) * np.sin(u)
    z_s = z + r * np.cos(v)

fig = plt.figure()
ax = fig.add_subplot(projection='3d')
ax.plot_surface(x_s, y_s, z_s, color='b', alpha=0.4)

ax.set_xlabel('X (nm)')
ax.set_ylabel('Y (nm)')
ax.set_zlabel('Z (nm)')
plt.show()


