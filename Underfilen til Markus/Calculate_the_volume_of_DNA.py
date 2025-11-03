import numpy as np
from Size_of_atom import Get_dim_and_size_of_atom
import matplotlib.pyplot as plt
from Calculate_sphere import Calculate_sphere
from Random_walker import random_walker
import Point_In_Spheres
import math
from Task_9 import task_9

def Calculate_the_volume_of_DNA(walks,steps):
    """
    Estimates the DNA volume using the Monte Carlo method.

    Random points are generated inside a 3D box, and the fraction that land
    inside the DNA (modeled as spheres) is used to estimate its volume.
    Also plots the 3D result and gives a 95% confidence interval.

    Parameters:
        walks (int): Number of random walks.
        steps (int): Steps per walk.
    """
    ax = plt.figure().add_subplot(projection="3d")
    spheres = Calculate_sphere()
    points = []

    for walk_index in range(walks):
        print_walk = random_walker(steps)
        ax.plot(*print_walk.T,color='#3050F8')
        plt.pause(0.05)

        for i in range(len(print_walk)):
            points.append(print_walk[i])

    points = np.array(points, dtype=float)


    x, y, z, point_in = Point_In_Spheres.Point_In_Spheres(spheres, points)

    total_points = len(points)
    inside_points = int(point_in)
    inside_fraction = inside_points / total_points
    Volume_of_box=20*25*20
    Volume_of_DnA = inside_fraction * Volume_of_box

    print("Number of points inside DNA:", inside_points)
    print("Total points tested:", total_points)

    print(f"Bounding box volume: {Volume_of_box}")
    print(f"Inside fraction:     {inside_fraction:.6f}")
    print(f"DNA volume ≈ {Volume_of_DnA}")

    
    ax.set_xlim([-50, -30])
    ax.set_ylim([-20, 5])
    ax.set_zlim([-10, 10])

    ax.set_xlabel("X (nm)")
    ax.set_ylabel("Y (nm)")
    ax.set_zlabel("Z (nm)")
    
    ax.scatter(x, y, z,".",s=1,color="#F83030")
    plt.show()
    


def main():
    walks = 200
    steps = 1000
    Calculate_the_volume_of_DNA(walks,steps)


if __name__ == "__main__":
    main()
