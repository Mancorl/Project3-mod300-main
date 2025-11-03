import numpy as np
def plot_sphere(sphere):
    """
    Generate two arrays of random points within a specified range.

    Parameters:
        tuple: i x j marix
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
        x_sphere.append(sphere[i,1] + sphere[i,0] * np.sin(v) * np.cos(u))
        y_sphere.append(sphere[i,2] + sphere[i,0] * np.sin(v) * np.sin(u))
        z_sphere.append(sphere[i,3] + sphere[i,0] * np.cos(v))
    return x_sphere,y_sphere,z_sphere