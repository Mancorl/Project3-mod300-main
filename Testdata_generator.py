import numpy as np
import Box_Class as boks

def rand_tall_med_r(amont, low=0.0, high=1.0,maks_r=100):
    """
    Generate two arrays of random points within a specified range.

    Parameters:
        amont (int): Number of random points to generate.
        low (float): Lower limit of the random range.
        high (float): Upper limit of the random range.

    Returns:
        tuple: 3 numpy arrays of shape (amont) and 1 numpy arrays of shape (100 times smaler then boxs).
    """

    x = np.round(np.random.uniform(low, high, size=amont)) # list for x aksen
    y = np.round(np.random.uniform(low, high, size=amont)) # list for y aksen
    z = np.round(np.random.uniform(low, high, size=amont)) # list for z aksen
    delta_r = high - low # delta
    r = np.round(np.random.uniform(0, delta_r/maks_r, size=amont))

    return np.array([r,x,y,z]).T




box = 10000
x = rand_tall_med_r(101, 0.0, box,100)
#print(x)
#print(x.T)

boks1 = boks.box()
boks1.add_points(x)
boks1.plot()