from envtest import rand_array
from envtest import join_in_table
import numpy as np

points=1000

array1=np.random.rand(points)
print(join_in_table(array1))