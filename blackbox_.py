import numpy as np

#global max (28, 392)
#local max (12, 360)
def f(x):
    if x>37:
        f = -15.4 * np.log(x-35) +163.15493533
    else:
        f =  -((0.25*x - 3)**2 * (0.25*x - 5.) * (0.25*x - 8.) - 360)
    return f