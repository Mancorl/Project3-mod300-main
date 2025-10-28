import Check_points
import Box_Class
import Testdata_generator
boks = Box_Class.box()
boks.add_spheres(Testdata_generator.rand_tall_med_r_2(1,0,100,1))
(in_sphere,total_points) = Check_points.Check_Points(boks,300,0,100,True)

print(f"Total fraction of points inside the circle is: {in_sphere/total_points}")


