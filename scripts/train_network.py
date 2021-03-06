__author__ = 'ali'
import numpy as np
from scipy.optimize import minimize
import random

from forward_backward_prop import forward_backward_prop

N = 200
dimensions = [10, 5, 10]
data = np.random.randn(N, dimensions[0])  # each row will be a datum
labels = np.zeros((N, dimensions[2]))
for i in xrange(N):
    labels[i, random.randint(0, dimensions[2] - 1)] = 1

params = np.random.randn((dimensions[0] + 1) * dimensions[1] + (dimensions[1] + 1) * dimensions[2])

params_opt = minimize(lambda params: forward_backward_prop(data, labels, params),
                      params, jac=True, method="BFGS", options={'disp': True})