def Box_Maker(x=10000,y=10000,z=10000):
    '''
    Initialization function of the box class, called automatically upon instansiation of a new box

    Parameters
    self 
    '''
    ax.set_xlim(0,x)
    ax.set_ylim(0,y)
    ax.set_zlim(0,z)
    return (x,y,z)