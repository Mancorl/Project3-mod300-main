
"""
This file Plots a 3D visualization of DNA atom positions using spheres 
for hydrogen, oxygen, phosphorus, carbon, and nitrogen atoms.
"""
import matplotlib.pyplot as plt
import Plot_Sphere
import Size_of_atom


def Plot_dna(H,O,P,C,N):
    """
    Plots a 3D visualization of DNA atom positions using spheres 
    for hydrogen, oxygen, phosphorus, carbon, and nitrogen atoms.

    Each element is drawn in a different color to represent its type.
    """
    x_h, y_h ,z_h = Plot_Sphere.plot_sphere(H)

    x_o, y_o ,z_o = Plot_Sphere.plot_sphere(O)

    x_p, y_p ,z_p = Plot_Sphere.plot_sphere(P)

    x_c, y_c ,z_c = Plot_Sphere.plot_sphere(C)

    x_n, y_n ,z_n = Plot_Sphere.plot_sphere(N)

    fig = plt.figure()

    ax = fig.add_subplot(projection="3d")

    ax.plot(x_h, y_h, z_h, '.', color="#93B3C8")  # Hydrogen - light blue
    ax.plot(x_o, y_o, z_o, '.', color='#FF0D0D')  # Oxygen - red
    ax.plot(x_p, y_p, z_p, '.', color='#FFA500')  # Phosphorus - orange
    ax.plot(x_c, y_c, z_c, '.', color="#6C5800")  # Carbon - brown
    ax.plot(x_n, y_n, z_n, '.', color='#3050F8')  # Nitrogen - blue

    ax.set_xlabel("X (Å)")
    ax.set_ylabel("Y (Å)")
    ax.set_zlabel("Z (Å)")
    ax.set_title("3D Visualization of DNA")

    plt.show() 

if __name__ == "__main__":
    H,O,P,C,N,_ = Size_of_atom.Get_dim_and_size_of_atom()
    Plot_dna(H,O,P,C,N)
