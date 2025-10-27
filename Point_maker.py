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
test = make_points(10,1,100)