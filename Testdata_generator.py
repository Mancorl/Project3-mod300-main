import numpy as np
import Box_Class as boks

def rand_tall_med_r_2(amont, low=0.0, high=1.0,maks_r=100):
    """
    Generate two arrays of random points within a specified range.

    Parameters:
        amont (int): Number of random points to generate.
        low (float): Lower limit of the random range.
        high (float): Upper limit of the random range.

    Returns:
        tuple: 3 numpy arrays of shape (amont) and 1 numpy arrays of shape (100 times smaler then boxs).
    """
    delta_r = high - low  # delta for radius
    r = np.round(np.random.uniform(0, delta_r / maks_r, size=amont))
    x ,y, z = [],[],[]
    for i in r:
        x.append(np.round(np.random.uniform(low+i, high-i)))
        y.append(np.round(np.random.uniform(low+i, high-i)))
        z.append(np.round(np.random.uniform(low+i, high-i)))
    return np.array([r,x,y,z]).T




#box = 10000
#x = rand_tall_med_r(1, 0, box, 1)
#print(x)
#print(x.T)

#boks1 = boks.box()
#boks1.add_spheres(x)
#boks1.plot()
