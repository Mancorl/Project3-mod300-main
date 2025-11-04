
"""
This file contains the function that calculates the volume of each sphere.
"""
import numpy as np

def volum_cal(sphere):
    """
    Calculates the volume of each sphere.

    Parameters:
        sphere : Each row [r, x, y, z].

    Returns:
        list: Volumes of all spheres.
    """
    volum = []
    for i in range(len(sphere)):
        volum.append((sphere[i,0]**3)*4*np.pi/3)
    return volum
