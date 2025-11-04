
"""
This file contains the function for plotting spheres
"""

import numpy as np

def plot_sphere(sphere):
    """
    Generate sphere

    Parameters:
        i = amont of sphere
        j = r,x,y,z

    Returns:
        :returns x y z point for all sphere
    """
    u = np.linspace(0, 2 * np.pi, 100)
    v = np.linspace(0, np.pi, 100)
    u, v = np.meshgrid(u, v)

    x_sphere,y_sphere,z_sphere = [],[],[]
    for i in range(len(sphere)):
        x= sphere[i,1] + sphere[i,0] * np.sin(v) * np.cos(u)
        y= sphere[i,2] + sphere[i,0] * np.sin(v) * np.sin(u)
        z= sphere[i,3] + sphere[i,0] * np.cos(v)  
        
        x_sphere.append(x.flatten())
        y_sphere.append(y.flatten())
        z_sphere.append(z.flatten())

        
    return np.concatenate(x_sphere), np.concatenate(y_sphere), np.concatenate(z_sphere)
