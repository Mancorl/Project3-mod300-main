import numpy as np
xyz_low = np.array([-50, -20 , -10])
xyz_high = np.array([-30, 5 , 10])

def re_make_point(point, xyz_high, xyz_low, max_val=10000):
    # Vectorized mapping
    return xyz_low + (xyz_high - xyz_low) * (point / max_val)
