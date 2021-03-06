__author__ = 'ali'
import numpy as np
def softmax(x):
    """ Softmax function """
    ###################################################################
    # Compute the softmax function for the input here.                #
    # It is crucial that this function is optimized for speed because #
    # it will be used frequently in later code.                       #
    # You might find numpy functions np.exp, np.sum, np.reshape,      #
    # np.max, and numpy broadcasting useful for this task. (numpy     #
    # broadcasting documentation:                                     #
    # http://docs.scipy.org/doc/numpy/user/basics.broadcasting.html)  #
    # You should also make sure that your code works for one          #
    # dimensional inputs (treat the vector as a row), you might find  #
    # it helpful for your later problems.                             #
    ###################################################################

    ### YOUR CODE HERE
    # subtracting max of each row from its elements
    x = np.matrix(x)
    nax = len(np.shape(x)) - 1
    row_max = np.matrix(x.max(axis=nax))
    x = x - row_max

    x = np.exp(x)
    row_sum = x.sum(axis=nax)
    x = x / row_sum

    ### END YOUR CODE

    return np.array(x)