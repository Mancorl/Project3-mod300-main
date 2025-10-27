import Box_Class
import Testdata_generator
import Point_checker
import Point_maker
import numpy as np

boks = Box_Class.box()
boks.add_spheres(Testdata_generator.rand_tall_med_r_2(1,0,10000,1))
#boks.add_spheres(np.array[np.array(100),np.array(100),np.array(100),np.array(100)])
pointlist = Point_maker.make_points(10,0,10000)
#pointlist = np.array([50,50,50])
#point= [5000,5000,5000]
#print(boks.spheres)
for i in pointlist:
    if Point_checker.in_circle(i, boks.spheres[0]): 
        print(Point_checker.in_circle(i, boks.spheres[0]))
        print(i)
        boks.add_points(i)
boks.plot()



