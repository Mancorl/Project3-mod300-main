
"""
Finds points inside any of spheres
"""
import numpy as np
import Circletest

def point_in_spheres(spheres,points):
    """
    Finds points inside any of spheres.

    Parameters:
        spheres : Each row [r, x, y, z].
        points : Each row [x, y, z].

    Returns:
        x_point, y_point, z_point (list): Coordinates of inside points.
        point_in (int): Number of points inside spheres.
    """
    x_point,y_point,z_point = [],[],[]
    point_in = 0
    for i in range(len(spheres)):
        for j in range(len(points)):
            if Circletest.in_circle(points[j,:], spheres[i,:]):
                point_in += 1
                x_point.append(points[j,0])
                y_point.append(points[j,1])
                z_point.append(points[j,2])
                points[j,:] = [0,0,0]

    return x_point,y_point,z_point,point_in




