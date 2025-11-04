
"""
This File makes a list of all atoms (as spheres) with their radius and position.
"""

import numpy as np
from Size_of_atom import Get_dim_and_size_of_atom

def calculate_sphere():
    """
    Makes a list of all atoms (as spheres) with their radius and position.
    Each atom is saved as [radius, x, y, z].
    """
    h, c, n, o, p, _ = Get_dim_and_size_of_atom()

    spheres = []

    for atom_list in [h, c, n, o, p]:
        for atom in atom_list:
            r, x, y, z = atom
            spheres.append([float(r), float(x), float(y), float(z)])
    return np.array(spheres, dtype=float)

if __name__ == "__main__":
    print(calculate_sphere())
