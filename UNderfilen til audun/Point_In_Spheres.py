import numpy as np
import Circletest

def Point_In_Spheres(spheres,points):
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

    return np.array(x_point,y_point,z_point),point_in



