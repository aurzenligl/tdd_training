# example based on code from numpy library:
# https://github.com/numpy/numpy/blob/master/numpy/matlib.py
# https://github.com/numpy/numpy/blob/master/numpy/fft/fftpack.c

'How should these functions be documented?'

def ones(shape, dtype=None, order='C'):
    # ...

static void radb3(int ido, int l1, const Treal cc[], Treal ch[],
const Treal wa1[], const Treal wa2[])
{
    // ...
}



































'''
Crucial difference is that first is public, second is private.

Public API is for people who may not know how to use library,
or are new to numerics. The function has specific purpose,
return value and argument types, following certain convention.
This can and should be explained shortly.
Then an illustrative example can be given.

Private implementation details of fft are addressed to a handful
of developers - experts who can do it accurately and in a performant manner.
These details can change any time without users noticing.
In order to explain the second one, part of numeric algorithms textbook
would need to be put into the source code. But it wouldn't serve any purpose:
people working with such problems can associate name "radb3" with
mixed-radix FFT of factor 3 and find relevant explanation in more suitable
place than source code.
'''

def ones(shape, dtype=None, order='C'):
    """
    Matrix of ones.
    Return a matrix of given shape and type, filled with ones.
    Parameters
    ----------
    shape : {sequence of ints, int}
        Shape of the matrix
    dtype : data-type, optional
        The desired data-type for the matrix, default is np.float64.
    order : {'C', 'F'}, optional
        Whether to store matrix in C- or Fortran-contiguous order,
        default is 'C'.
    Returns
    -------
    out : matrix
        Matrix of ones of given shape, dtype, and order.
    See Also
    --------
    ones : Array of ones.
    matlib.zeros : Zero matrix.
    Notes
    -----
    If `shape` has length one i.e. ``(N,)``, or is a scalar ``N``,
    `out` becomes a single row matrix of shape ``(1,N)``.
    Examples
    --------
    >>> np.matlib.ones((2,3))
    matrix([[ 1.,  1.,  1.],
            [ 1.,  1.,  1.]])
    >>> np.matlib.ones(2)
    matrix([[ 1.,  1.]])
    """
    # ...

// no documentation at all!
static void radb3(int ido, int l1, const Treal cc[], Treal ch[],
const Treal wa1[], const Treal wa2[])
{
    // ...
}
