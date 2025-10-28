import matplotlib.pyplot as plt
import numpy as np

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
        self.spheres = []
        self.points = []

    def add_spheres(self, matrix):
        self.spheres = matrix

    def add_points(self, point):
        self.points.append(point)



    def plot(self):
        #print(len(self.spheres))
        radius_array=[]
        x_array = []
        y_array = []
        z_array=[]
        x_points_array=[]
        y_points_array=[]
        z_points_array=[]
        #x_mod = [[]]
        #y_mod = [[]]
        #z_mod = [[]]
        sphere = [[]]
        for i in range(len(self.spheres)):
            radius_array.append(self.spheres[i][0])
            x_array.append(self.spheres[i][1])
            y_array.append(self.spheres[i][2])
            z_array.append(self.spheres[i][3])
        
        for i in range(len(self.points)):
            x_points_array.append(self.points[i][0])
            y_points_array.append(self.points[i][1])
            z_points_array.append(self.points[i][2])

        fig = plt.figure()
    
        ax = fig.add_subplot(projection="3d")
        ax.set_xlim(0,self.x)
        ax.set_ylim(0,self.y)
        ax.set_zlim(0,self.z)

        u = np.linspace(0, 2 * np.pi, 100)
        v = np.linspace(0, np.pi, 100)
        u,v = np.meshgrid(u,v)
        for i in range(len(self.spheres)):
            print(x_array)
            sphere[0].append(x_array[i] + radius_array[i] * np.cos(u)*np.sin(v))
            sphere[1].append(y_array[i] + radius_array[i] * np.sin(u) * np.sin(v))
            sphere[2].(z_array[i] + radius_array[i] * np.cos(v))
        ax.plot(sphere)
        ax.scatter(x_points_array,y_points_array,z_points_array)
        plt.show()
#test = box()
#test.add_points([[120,555,555,555],[145,666,777,888],[267,999,999,9910],[267,999,999,9910],[267,999,999,9910],[267,999,999,9910]])
#print(test.points[0],test.points[2],test.points[1])
#test.plot()


