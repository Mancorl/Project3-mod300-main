
"""
This file estimates the DNA volume using the Monte Carlo method.
"""
import numpy as np
import matplotlib.pyplot as plt
from Calculate_sphere import calculate_sphere
from Random_walker import random_walker
import point_in_spheres

def Calculate_the_volume_of_DNA(walks,steps):
    """
    Estimates the DNA volume using the Monte Carlo method.

    Random walks are generated inside a 3D box, and the fraction that land
    inside the DNA (modeled as spheres) is used to estimate its volume.
    Also plots the 3D result.
    Parameters:
        walks (int): Number of random walks.
        steps (int): Steps per walk.
    """
    ax = plt.figure().add_subplot(projection="3d")
    spheres = calculate_sphere()
    points = []

    for walk_index in range(walks):
        print_walk = random_walker(steps)
        ax.plot(*print_walk.T,color='#3050F8')

        for i in range(len(print_walk)):
            points.append(print_walk[i])

    points = np.array(points, dtype=float)


    x, y, z, point_in = point_in_spheres.point_in_spheres(spheres, points)

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

    
    Volume_theoretical = np.sum((4/3) * np.pi * spheres[:, 0]**3)

    print(f"Theoretical DNA volume: {Volume_theoretical:.2f}")
    Ratio = Volume_of_DnA/ Volume_theoretical
    print(f"Ratio of theoretical volume vs Monte Carlo volume: {Ratio:.2f}")
    
    
    ax.set_xlim([-50, -30])
    ax.set_ylim([-20, 5])
    ax.set_zlim([-10, 10])

    ax.set_xlabel("X Å")
    ax.set_ylabel("Y Å")
    ax.set_zlabel("Z Å")
    ax.set_title("3D Random Walk + DNA volume")

    ax.scatter(x, y, z,".",s=1,color="#F83030")

    plt.show()
    
def main():
    """
    initiates the function with chosen walks and steps.
    """
    walks = 200
    steps = 100
    Calculate_the_volume_of_DNA(walks,steps)

if __name__ == "__main__":
    main()
