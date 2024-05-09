if __name__ == '__main__':
    import numpy as np
    import matplotlib.pyplot as plt

    arr = np.array(([1, 0, 3, 4, 5], [6, 7, 8, 9, 10], [1, 0, 0, 0, 0], [2, 0, 0, 0, 0]), dtype="i4")
    new_arr = arr.astype("bool")
    n_arr = arr.reshape(2, 5, -1)
    arr_one = np.ones((2, 5), dtype=int)
    print(arr)
    print(arr[2, 1:4])
    print(new_arr)
    print(n_arr)
    print(arr_one)
    print(arr.dtype)
    print(new_arr.dtype)
    print(arr.shape)
    print(arr.cumsum())
