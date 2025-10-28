import numpy as np
def rand_tall_med_r(amont, low=0.0, high=1.0, r_size = 100):
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
    r = np.round(np.random.uniform(0, delta_r / r_size, size=amont))

    x ,y, z = [],[],[]
    for i in r:
        x.append(np.round(np.random.uniform(low+i, high-i)))
        y.append(np.round(np.random.uniform(low+i, high-i)))
        z.append(np.round(np.random.uniform(low+i, high-i)))
    return np.array([r,x,y,z]).T

#point_test = rand_tall_med_r(2 , 0, 10)
#print(point_test)