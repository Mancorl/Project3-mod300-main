import Box_Class
import Testdata_generator
import Point_checker
import Point_maker
import numpy as np

boks = Box_Class.box()
boks.add_spheres(Testdata_generator.rand_tall_med_r_2(5,0,10000,100))
print(boks.spheres)
pointlist = Point_maker.make_points(1,0,100)

def Check_Points(box,numb,low,high,ratio):
    counter_success = 0
    Counter_total = 0
    #boks = Box_Class.box(100,100,100)
    #boks.add_spheres(Testdata_generator.rand_tall_med_r_2(1,0,100,1))
    #boks.add_spheres(np.array[np.array(100),np.array(100),np.array(100),np.array(100)])
    pointlist = Point_maker.make_points(numb,low,high)
    for i in pointlist:
        if Point_checker.in_circle(i, box.spheres[0]): 
            print(Point_checker.in_circle(i, box.spheres[0]))
            counter_success += 1
            #print(i)
        Counter_total+= 1

    if ratio:
        return (counter_success, Counter_total)
    box.plot()

print(Check_Points(boks, 300,0,10000,False))

