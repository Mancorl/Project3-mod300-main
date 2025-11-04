
"""
The random walker! a file that makes how many random walkers walk in a random 3D space. RANDOMLY!
"""

import matplotlib.pyplot as plt
import numpy as np
from Point_Maker import make_points
import numpy as np
from remake_points import re_make_point

def random_walker(N):
    """
    Simulates a 3D random walk within a defined box.

    Parameters:
        N (int): Number of steps in the random walk.

    Returns:
        nparray: Array of shape (N, 3) with [x, y, z] positions for each step.
    """
    xyz_low = np.array([-50, -20 , -10])
    xyz_high = np.array([-30, 5 , 10])

    distribute = re_make_point(make_points(1,1,10000),xyz_high,xyz_low)
        
    x=distribute[0][0]
    y=distribute[0][1]
    z=distribute[0][2]

    for step in range(N):
        x=np.append(x,np.random.randint(-1,2))
        y=np.append(y,np.random.randint(-1,2))
        z=np.append(z,np.random.randint(-1,2))

        
        if sum(x) > xyz_high[0] or sum(y) > xyz_high[1] or sum(z) > xyz_high[2]:

            x = x[:-1]
            y = y[:-1]
            z = z[:-1]

            continue

        if sum(x) < xyz_low[0] or sum(y) < xyz_low[1] or sum(z) < xyz_low[2]:

            x = x[:-1]
            y = y[:-1]
            z = z[:-1]

            continue
    
    return np.array([np.cumsum(x), np.cumsum(y), np.cumsum(z)]).T
        



def main():
    """
    A default plot for the random walker
    """
    ax=plt.figure().add_subplot(projection="3d") 
    walks=20
    steps=100
    for walk_index in range(walks):
        print_walk=random_walker(steps)
        ax.plot(*print_walk.T)
        plt.pause(0.05)

    ax.set_xlim([-50, -30])
    ax.set_ylim([-20, 5]) 
    ax.set_zlim([-10, 10])
    ax.set_title("3D Random Walk Simulation")
    ax.set_xlabel("X-axis")
    ax.set_ylabel("Y-axis")
    ax.set_zlabel("Z-axis")
    plt.show()

if __name__ == "__main__":
    main()
