from Size_of_atom import Get_dim_and_size_of_atom
import numpy as np

def Calculate_sphere():
    spheres = []
    H, C, N, O, P, dna_list = Get_dim_and_size_of_atom()
    for arr in (H, C, N, O, P):
        if arr is None or len(arr) == 0:
            continue
        for i in range(len(arr)):
            r = float(arr[i][0])
            x = float(arr[i][1])
            y = float(arr[i][2])
            z = float(arr[i][3])
            spheres.append([r, x, y, z])
        return np.array(spheres, dtype=float)