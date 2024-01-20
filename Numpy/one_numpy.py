import numpy as np

# arr=[1,2,4,5,6,7,5,8,9,5]
arr2 = (1, 2, 4, 5, 6, 7, 5, 8, 9, 5)
# print(type( arr))
# print(np.__version__)
# a = np.array(arr2)
# print(type(a))

d2_arr = np.array(
    [
        [1, 2, 3, 4],
        [1, 4, 5, 6],
    ]
)
""" 2 d array """
# print(type(d2_arr))
# for i in d2_arr:
#     for j in i:
#         print(j,end=' ')
#     print('\n')

""" 3d array """
arr = np.array(
    [
        [
            [1, 2, 3],
            [4, 5, 6],
        ],
        [
            [1, 2, 3],
            [4, 5, 6],
        ],
    ],
)

# for i in arr:
#     for j in i:
#         for z in j:
#             print(z)
#         print("\n")
#     print("\n")

# print(d2_arr.ndim)
# print(arr.ndim)

# arr = np.array([1, 2, 3, 4], ndmin=5)
# print(arr.ndim)

# arr =np.array([
#     [1, 2, 3, 4, 5],
#     [5, 4, 3, 2, 1],
# ])
# print(arr[1,1])

# arr = np.array(
#     [
#         [1, 2, 3, 4, 5],
#         [6, 7, 8, 9, 10],
#     ],
# )

# print("Last element from 2nd dim: ", arr[1, -1])


# arr = np.array([1, 2, 3, 4, 5, 6, 7])
# print(arr[4:])
# arr = np.array([1, 2, 3, 4, 5, 6, 7])
# print(arr[:4])
arr = np.array([1, 2, 3, 4, 5, 6, 7,'amad'])
# print(arr[-3:-1])
np.array()
print(arr.dtype)
