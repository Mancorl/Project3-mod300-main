
"""
This file is testing if a point is in the sphere
"""

def in_circle(point, sphere):
    """
      testing if a point is in the sphere

      Parameters:
          point (int): list[x,y,z] cordenets
          sphere (int): list of sphere [r,x,y,z]

      Returns:
          true if in the sphere
      """

    return ((sphere[1]-point[0]) ** 2) + ((sphere[2]-point[1]) ** 2) + ((sphere[3]-point[2]) ** 2) < sphere[0]**2
