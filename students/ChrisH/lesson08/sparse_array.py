#!/usr/bin/env python3
# -----------------------------------------------------------
# sparse_array.py
#  Class that represents a sparse array.
# -----------------------------------------------------------

class SparseArray(object):

    def __init__(self, sp_array):
        self._sparsearray = {}
        self._length = len(sp_array)
        for key, val in enumerate(sp_array):
            if val != 0:
                self._sparsearray[key] = val

    @property
    def sparsearray(self):
        return [ self._sparsearray.get(key, 0) for key in range(self._length) ]

    def __len__(self):
        return self._length




if __name__ == "__main__":

    sa = SparseArray([1,0,2,0,3,4,0,0,0,0,10])
    sa2 = SparseArray([1,0,2,0,3,4,0,0,0,0,10, 0, 0, 0, 0])

    print(sa.sparsearray)
    print(sa2.sparsearray)

    print("Length: ",len(sa))
    print("Length: ", len(sa2))