
"""
This module provides a function to rescale 3D points to a defined coordinate range.
"""

import numpy as np

def re_make_point(point, xyz_high, xyz_low, max_val=10000):
    """
    Remap a point or array of points to a new coordinate range.
    """
    xyz_low = np.array([-50, -20 , -10])
    xyz_high = np.array([-30, 5 , 10])
    
    # Vectorized mapping
    return xyz_low + (xyz_high - xyz_low) * (point / max_val)
