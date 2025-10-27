import matplotlib.pyplot as plt

class box:
    def __init__(self, x=10000,y=10000,z=10000):
        self.x = x
        self.y = y
        self.z = z
        self.points = [[]]

    def add_points(self, matrix):
        if matrix == [] or matrix == [[]]:
            return
        
        for i in range(len(matrix)):
            self.points.append(matrix[i])


        if self.points[0] == []:
            del self.points[0]

    
    def plot(self):
        print(len(self.points))
        radius_array=[]
        x_array = []
        y_array = []
        z_array=[]
        for i in range(len(self.points)):
            radius_array.append(self.points[i][0])
            x_array.append(self.points[i][1])
            y_array.append(self.points[i][2])
            z_array.append(self.points[i][3])

        fig = plt.figure()
        ax = fig.add_subplot(projection="3d")
        ax.scatter(x_array,y_array,z_array)
        plt.show()
test = box()
test.add_points([[120,555,555,555],[145,666,777,888],[267,999,999,9910],[267,999,999,9910],[267,999,999,9910],[267,999,999,9910]])
print(test.points[0],test.points[2],test.points[1])
test.plot()


