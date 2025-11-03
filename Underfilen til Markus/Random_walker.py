import random
import matplotlib.pyplot as plt
import numpy as np
from Point_Maker import make_points
import numpy as np





def re_make_point(point, xyz_high, xyz_low, max_val=10000):
    # Vectorized mapping
    return xyz_low + (xyz_high - xyz_low) * (point / max_val)



def random_walker(N):
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
            # if __name__ == "__main__":
            #     print("---------------------")
            #     print("Dette er high lim hit")
            #     print(sum(x) > xyz_high[0],sum(x),'x >',xyz_high[0])
            #     print(sum(y) > xyz_high[1],sum(y),'y >',xyz_high[1])
            #     print(sum(z) > xyz_high[2],sum(z),'z >',xyz_high[2])
            #     print("---------------------")
            

            x = x[:-1]
            y = y[:-1]
            z = z[:-1]
            continue

        if sum(x) < xyz_low[0] or sum(y) < xyz_low[1] or sum(z) < xyz_low[2]:
            # if __name__ == "__main__":
            #     # print("---------------------")
            #     # print("low lim hit")
            #     # print(sum(x) < xyz_low[0],sum(x),'x <',xyz_low[0])
            #     # print(sum(y) < xyz_low[1],sum(y),'y <',xyz_low[1])
            #     # print(sum(z) < xyz_low[2],sum(z),'z <',xyz_low[2])
            #     # print("---------------------")
            
            x = x[:-1]
            y = y[:-1]
            z = z[:-1]
            continue
    
    return np.array([np.cumsum(x), np.cumsum(y), np.cumsum(z)]).T
        



def main():
    
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
    plt.show()

if __name__ == "__main__":
    main()
