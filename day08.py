import numpy as np


with open("data/day08.txt") as f:
    inputs = f.read().strip()

# inputs = "0222112222120000"


arr = np.array([int(pixel) for pixel in inputs])
arr = arr.reshape(-1, 6, 25)
# arr = arr.reshape(-1, 2, 2)
layer = np.argmin((arr == 0).sum(axis=(1, 2)))
result_a = (arr[layer, :, :] == 1).sum() * (arr[layer, :, :] == 2).sum()
print(result_a)

amax = np.argmax(arr!=2, axis=0)
code = np.empty((arr.shape[1], arr.shape[2]))
for i in range(arr.shape[1]):
    for j in range(arr.shape[2]):
        code[i, j] = arr[amax[i, j], i, j]
print(code)

for i in range(code.shape[0]):
    for j in range(code.shape[1]):
        symbol = "." if code[i,j] else " "
        print(symbol, end="")
    print()
