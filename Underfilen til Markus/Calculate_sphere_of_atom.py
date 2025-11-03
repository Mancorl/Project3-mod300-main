import numpy as np
import matplotlib.pyplot as plt
from Size_of_atom import Get_dim_and_size_of_atom
from Random_walker import random_walker
import Point_In_Spheres
import math

H, C, N, O, P, dna_list = Get_dim_and_size_of_atom()


spheres = []
for arr in (H, C, N, O, P):
    if arr is None or len(arr) == 0:
        continue
    for i in range(len(arr)):
        r = float(arr[i][0])
        x = float(arr[i][1])
        y = float(arr[i][2])
        z = float(arr[i][3])
        spheres.append([r, x, y, z])

spheres = np.array(spheres, dtype=float)

def main():
    ax = plt.figure().add_subplot(projection="3d")
    walks = 200
    steps = 100
    points = []

    for walk_index in range(walks):
        print_walk = random_walker(steps)
        ax.plot(*print_walk.T,color='#3050F8')
        plt.pause(0.05)

        for i in range(len(print_walk)):
            points.append(print_walk[i])

    points = np.array(points, dtype=float)


    x, y, z, point_in = Point_In_Spheres.Point_In_Spheres(spheres, points)

    total_points = len(points)
    inside_points = int(point_in)
    inside_fraction = inside_points / total_points
    Volume_of_box=20*25*20
    Volume_of_DnA = inside_fraction * Volume_of_box

    print("Number of points inside DNA:", inside_points)
    print("Total points tested:", total_points)

    print(f"Bounding box volume: {Volume_of_box}")
    print(f"Inside fraction:     {inside_fraction:.6f}")
    print(f"DNA volume ≈ {Volume_of_DnA}")

    
    ax.set_xlim([-50, -30])
    ax.set_ylim([-20, 5])
    ax.set_zlim([-10, 10])

    ax.set_xlabel("X (nm)")
    ax.set_ylabel("Y (nm)")
    ax.set_zlabel("Z (nm)")
    
    ax.plot(x, y, z,color="#F83030")
    plt.show()
    
    ######TODO MAKE 95 KONFIDENS INTERVAL#########
    p = inside_fraction
    n = total_points
    z = 1.96  # 95% z-score

    # standard error for a binomial proportion
    se = math.sqrt(max(p * (1 - p), 1e-16) / max(n, 1))

    # CI for proportion (clamped to [0,1])
    p_low = max(0.0, p - z * se)
    p_high = min(1.0, p + z * se)

    # CI for volume
    V_low = p_low * Volume_of_box
    V_high = p_high * Volume_of_box

    print(f"Inside fraction 95% CI: [{p_low:.6f}, {p_high:.6f}]")
    print(f"DNA volume 95% CI: [{V_low:.3f}, {V_high:.3f}] nm^3")

    # optional: other units
    V_nm3 = Volume_of_DnA
    V_um3 = V_nm3 / 1e9
    V_low_um3 = V_low / 1e9
    V_high_um3 = V_high / 1e9
    print(f"DNA volume ≈ {V_nm3:.3f} nm^3 ({V_um3:.3e} µm^3)")
    print(f"95% CI in µm^3: [{V_low_um3:.3e}, {V_high_um3:.3e}]")

if __name__ == "__main__":
    main()
