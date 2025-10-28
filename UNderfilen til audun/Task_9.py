import matplotlib.pyplot as plt
import Plot_Sphere
import Size_of_atom


def task_9(H,O,P,C,N):
    x_h, y_h ,z_h = Plot_Sphere.plot_sphere(H)

    x_o, y_o ,z_o = Plot_Sphere.plot_sphere(O)

    x_p, y_p ,z_p = Plot_Sphere.plot_sphere(P)

    x_c, y_c ,z_c = Plot_Sphere.plot_sphere(C)

    x_n, y_n ,z_n = Plot_Sphere.plot_sphere(N)

    H,O,P,C,N
    fig = plt.figure()

    ax = fig.add_subplot(projection="3d")
#ax.set_xlim(-30,-50)
#ax.set_ylim(-10,2)
#ax.set_zlim(10,10)

    ax.plot(x_h, y_h, z_h, '.', color='#FFFFFF')  # Hydrogen - white
    ax.plot(x_o, y_o, z_o, '.', color='#FF0D0D')  # Oxygen - red
    ax.plot(x_p, y_p, z_p, '.', color='#FFA500')  # Phosphorus - orange
    ax.plot(x_c, y_c, z_c, '.', color='#404040')  # Carbon - dark gray
    ax.plot(x_n, y_n, z_n, '.', color='#3050F8')  # Nitrogen - blue

    plt.show() 

H,O,P,C,N,_ = Size_of_atom.Get_dim_and_size_of_atom()
task_9(H,O,P,C,N)