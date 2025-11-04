def pi_cal(sphere,points_in):
    size_of_box = 100
    pi = []
    for i in range(len(sphere)):
        pi.append((sphere[i,0]**(-3))*3*points_in/4*size_of_box**3)
    return pi