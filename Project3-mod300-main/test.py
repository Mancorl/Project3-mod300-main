import random
import matplotlib.pyplot as plt
import numpy as np
import Circletest
import Point_In_Spheres
from Plot_Sphere import plot_sphere
import numpy as np
from Size_of_atom import Get_dim_and_size_of_atom
from Random_walker import random_walker




def main():
    _,_,_,_,_,dna_list=Get_dim_and_size_of_atom()
    atoms=len(dna_list)

    xyz_low  = np.array([-50, -20, -10], dtype=int)
    xyz_high = np.array([-30,   5,  10], dtype=int)
    
    

    ax=plt.figure().add_subplot(projection="3d") 
    walks=10
    steps=100
    for walk_index in range(walks):
        print_walk=random_walker(steps)
        print(*print_walk.T)
        # ax.plot(*print_walk.T)
        # plt.pause(0.05)

    # ax.set_xlim([-50, -30])
    # ax.set_ylim([-20, 5]) 
    # ax.set_zlim([-10, 10])
    # plt.show()

if __name__ == "__main__":
    main()

    

# DnA_Volume=box_volume * fraction


