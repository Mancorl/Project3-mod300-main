import numpy as np
def volum_cal(sphere):
    volum = []
    for i in range(len(sphere)):
        volum.append((sphere[i,0]**3)*4*np.pi/3)
    return volum