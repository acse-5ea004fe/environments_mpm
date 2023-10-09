import numpy as np
from scipy.ndimage import gaussian_filter
from scipy import misc
import pandas as pd

__all__ = ['rand_array', 'smooth_image', 'my_mat_solve','join_in_table']


def rand_array(shape):
    return np.random.rand(*shape)

def smooth_image(a, sigma=1):
    return gaussian_filter(a, sigma=sigma)

def my_mat_solve(A, b):
    return A.inv()*b

def join_in_table(np_array1):
    ts1 = pd.DataFrame(np_array1, index=pd.date_range("1/1/2000", periods=1000))
    return ts1