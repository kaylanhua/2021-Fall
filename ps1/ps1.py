#arr is array of (val, key) pairs
import math
import time
from random import randrange
import csv

def merge(arr1, arr2):
    sortedArr = []

    i = 0
    j = 0
    while i < len(arr1) or j < len(arr2):
        if i >= len(arr1):
            sortedArr.append(arr2[j])
            j += 1
        elif j >= len(arr2):
            sortedArr.append(arr1[i])
            i += 1
        elif arr1[i][0] <= arr2[j][0]:
            sortedArr.append(arr1[i])
            i += 1
        else:
            sortedArr.append(arr2[j])
            j += 1

    return sortedArr

def mergeSort(arr):
    if len(arr) < 2:
        return arr

    midpt = int(math.ceil(len(arr)/2))

    half1 = mergeSort(arr[0:midpt])
    half2 = mergeSort(arr[midpt:])

    return merge(half1, half2)

def countSort(arr, univsize):
    universe = []
    for i in range(univsize):
        universe.append([])

    for elt in arr:
        universe[elt[0]].append(elt)

    sortedArr = []
    for lst in universe:
        for elt in lst:
            sortedArr.append(elt)

    return sortedArr
 
def radixSort(arr, n, U, b):
    sortOn = [(elt[0] % b, elt[0], elt[1]) for elt in arr]
    sortOn = countSort(sortOn, b)
    for i in range(1, math.ceil(math.log(U, b))):
        temp = [((elt[1] // (pow(b, i))) % b, elt[1], elt[2]) for elt in sortOn]
        sortOn = countSort(temp, b)
    return [[elt[1], elt[2]] for elt in sortOn]

# TESTING
max = 21
iterations = 1

data = {
    'n': [],
    'U': [],
    'count': [],
    'radix': [],
    'merge': []
}

for j in range(1, max):
    twoPow = pow(2, j)
    for i in range(1, max):
        universe = pow(2, i)
        print("currently calculating: 2^" + str(j) + " with U = " + str(i))
        mergeSum, countSum, radixSum = 0, 0, 0
        data['n'].append(twoPow)
        data['U'].append(universe)

        for k in range(iterations):
            test = [[randrange(universe), 0] for m in range(twoPow)]

            start_time = time.time()
            mergeSort(test)
            mergeSum += time.time() - start_time

            start_time2 = time.time()
            countSort(test, universe)
            countSum += time.time() - start_time2

            start_time3 = time.time()
            radixSort(test, twoPow, universe, twoPow)
            radixSum += time.time() - start_time3

        data['count'].append(countSum / iterations)
        data['radix'].append(radixSum / iterations)
        data['merge'].append(mergeSum / iterations)

with open("./data.csv", "w") as outfile:
    writer = csv.writer(outfile)
    writer.writerow(data.keys())
    writer.writerows(zip(*data.values()))
