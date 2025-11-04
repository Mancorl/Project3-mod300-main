import random
import matplotlib.pyplot as plt
import numpy as np

import numpy as np
def make_points(numb_1, low=0.0, high=1.0):
    """
    Generate two arrays of random points within a specified range.

    Parameters:
        numb_1 (int): Number of random points to generate.
        low (float): Lower limit of the random range.
        high (float): Upper limit of the random range.

    Returns:
        tuple: 3 numpy arrays of shape (numb_1)
    """
    x = np.random.uniform(low, high, numb_1)
    y = np.random.uniform(low, high, numb_1)
    z = np.random.uniform(low, high, numb_1)

    return np.round(np.array([x,y,z]).T)

xyz_low = np.array([-50, -20 , -10])
xyz_high = np.array([-30, 5 , 10])

def re_make_point(point, xyz_high, xyz_low, max_val=10000):
    # Vectorized mapping
    return xyz_low + (xyz_high - xyz_low) * (point / max_val)

ax=plt.figure().add_subplot(projection="3d")


def plotting_3d(n,N):
    amount=0
    for walk in range(n):
        distribute = re_make_point(make_points(1,1,10000),xyz_high,xyz_low)
        print_plot_list.append([])
        
        x=distribute[0][0]
        y=distribute[0][1]
        z=distribute[0][2]

        for step in range(N):
            x=np.append(x,np.random.randint(-1,2))
            y=np.append(y,np.random.randint(-1,2))
            z=np.append(z,np.random.randint(-1,2))

            if sum(x) > xyz_high[0] or sum(y) > xyz_high[1] or sum(z) > xyz_high[2]:
                print("---------------------")
                print("Dette er high lim hit")
                print(sum(x) > xyz_high[0],sum(x),'x >',xyz_high[0])
                print(sum(y) > xyz_high[1],sum(y),'y >',xyz_high[1])
                print(sum(z) > xyz_high[2],sum(z),'z >',xyz_high[2])
                print("---------------------")
                amount+=1

                break

            if sum(x) < xyz_low[0] or sum(y) < xyz_low[1] or sum(z) < xyz_low[2]:
                print("---------------------")
                print("low lim hit")
                print(sum(x) < xyz_low[0],sum(x),'x <',xyz_low[0])
                print(sum(y) < xyz_low[1],sum(y),'y <',xyz_low[1])
                print(sum(z) < xyz_low[2],sum(z),'z <',xyz_low[2])
                print("---------------------")
                amount+=1
                
                break
            
        all_plot_list.append(np.cumsum(x))
        all_plot_list.append(np.cumsum(y))
        all_plot_list.append(np.cumsum(z))

        print_plot_list[walk].append(np.cumsum(x))
        print_plot_list[walk].append(np.cumsum(y))
        print_plot_list[walk].append(np.cumsum(z))



        
        

    print("Det var",amount,"av",n,"så traff limiten")

        
ax.set_xlim([-50, -30])
ax.set_ylim([-20, 5]) 
ax.set_zlim([-10, 10])


all_plot_list=[]
print_plot_list=[]



user_input_1="start"
user_input_2="start"
def main(user_input_1,user_input_2):

    plotting_3d(user_input_1,user_input_2)
    for i in range(user_input_1):
        ax.plot(*print_plot_list[i])
        plt.pause(0.05)

#main(30,30)