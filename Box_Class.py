import matplotlib.pyplot as plt
import numpy as np

def plot_sphere(sphere):
    """
    Generate two arrays of random points within a specified range.

    Parameters:
        tuple: i x j marix
        i = amont of sphere
        j = r,x,y,z

    Returns:
        :returns x y z point for all sphere
    """
    u = np.linspace(0, 2 * np.pi, 100)
    v = np.linspace(0, np.pi, 100)
    u, v = np.meshgrid(u, v)

    x_sphere,y_sphere,z_sphere = [],[],[]
    for i in range(len(sphere)):
        x_sphere.append(sphere[i,1] + sphere[i,0] * np.sin(v) * np.cos(u))
        y_sphere.append(sphere[i,2] + sphere[i,0] * np.sin(v) * np.sin(u))
        z_sphere.append(sphere[i,3] + sphere[i,0] * np.cos(v))
    return x_sphere,y_sphere,z_sphere







class box:
    def __init__(self, x=10000,y=10000,z=10000):
        '''
        Initialization function of the box class, called automatically upon instansiation of a new box

        Parameters
        self 
        '''
        self.x = x
        self.y = y
        self.z = z
        self.points = []

    def add_spheres(self, sphere):
        self.sphere = sphere

    def add_points(self, point):
        self.points.append(point)

    

    def plot(self):
        fig = plt.figure()
        x_sphere, y_sphere, z_sphere = plot_sphere(self.sphere)
        ax = fig.add_subplot(projection="3d")
        ax.set_xlim(0,self.x)
        ax.set_ylim(0,self.y)
        ax.set_zlim(0,self.z)

        
        ax.plot(x_sphere,y_sphere,z_sphere,'.r')
        #ax.scatter(x_points_array,y_points_array,z_points_array)
        plt.show()
#test = box()
#test.add_points([[120,555,555,555],[145,666,777,888],[267,999,999,9910],[267,999,999,9910],[267,999,999,9910],[267,999,999,9910]])
#print(test.points[0],test.points[2],test.points[1])
#test.plot()


