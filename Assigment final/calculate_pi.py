
"""
This file provides a function to estimate pi
"""

def calculate_pi(sphere,points_in):
    """
    Estimates pi based on points inside spheres.

    Parameters:
        sphere: Each row [r, x, y, z].
        points_in (int): Number of points inside spheres.

    Returns:
        list: Estimated π values for each sphere.
    """
    size_of_box= 100
    pi = []
    for i in range(len(sphere)):
        pi.append((sphere[i,0]**(-3))*3*points_in/4*size_of_box**3)
    return pi
