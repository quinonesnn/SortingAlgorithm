from datetime import datetime
import numpy as np
from numpy.core.fromnumeric import _mean_dispatcher
from numpy.lib.function_base import average

########## Initialization ##########
size100 = np.random.randint(100, size=100)
size1000 = np.random.randint(1000, size=1000)
size10000 = np.random.randint(10000, size=10000)
size100000 = np.random.randint(100000, size=100000)

########## Exchange Sort ##########
def ExchangeSort(nums):
    for i in range(len(nums)):
        for j in range(len(nums)):
            if nums[i] < nums[j]:
                temp = nums[i]
                nums[i] = nums[j]
                nums[j] = temp
    return nums


########## Insert Sort ##########
def InsertSort(nums):
    print("Insert Sort on: \n\t" + str(nums))
    for i in range(1, len(nums)):
        key = nums[i]
        j = i-1
        while j >=0 and key < nums[j] :
                nums[j+1] = nums[j]
                j -= 1
        nums[j+1] = key
    return nums


########## Binary Insert Sort ##########
def BinarySearch(nums, val, start, end):
    if start == end:
        if nums[start] > val:
            return start
        else:
            return start+1

    if start > end:
        return start
  
    mid = (start+end)/2
    if nums[mid] < val:
        return BinarySearch(nums, val, mid+1, end)
    elif nums[mid] > val:
        return BinarySearch(nums, val, start, mid-1)
    else:
        return mid
  
def BinaryInsertSort(nums):
    print("Binary Insert Sort on: \n\t" + str(nums))
    for i in range(1, len(nums)):
        val = nums[i]
        j = BinarySearch(nums, val, 0, i-1)
        nums = nums[:j] + [val] + nums[j:i] + nums[i+1:]
    print("     -> " + str(nums))
    return nums


########## Selection Sort ##########
def SelectionSort(nums):
    print("Selection Sort on: \n\t" + str(nums))
    for i in range(len(nums)):
        idx = i
        for j in range(i + 1, len(nums)):
            if nums[idx] > nums[j]:
                idx = j
        nums[i], nums[idx] = nums[idx], nums[i]
    print("     -> " + str(nums))
    return nums


########## Merge Sort ##########
# def MergeSort(n, nums):
#     if n > 1:
#         h = (n/2)
#         m = n - h


########## Merge Sort 2 ##########
# def MergeSort2(low, high):
#     mid = 0
#     if low < high:
#         mid = (low + high) / 2
#         MergeSort2(low, mid)
#         MergeSort2(mid + 1, high)
#         Merge2(low, mid, high)

# def Merge2(low, mid, high):
#     i, j, k = low, mid + 1, low
#     while i < mid and j < high:
#         if num


########## Merge Sort 4 (Linked List) ##########
# def MergeSort4(low, high, mergedlist):
#     list1, list2, mid = 0,0,0
#     if low == high:
#         mergedlist = low
#         nums[mergedlist].link = 0
#     else:
#         mid = (low + high) / 2
#         MergeSort4(low, mid, list1)
#         MergeSort4(mid + 1, high, list2)
#         Merge4(list1, list2, mergedlist)

# def Merge4(list1, list2, mergedlist):
#     lastsorted = 0
#     if nums[list1].key < nums[list2].key:
#         mergedlist = list1
#         list1 = nums[list1].link
#     else:
#         mergedlist = list2
#         list2 = nums[list2].link
#     lastsorted = mergedlist
#     while list1 != 0 and list2 != 0:
#         if nums[list1].key < nums[list2].key:
#             nums[lastsorted].link = list1
#             lastsorted = list1
#             list1 = nums[list1].link
#         else:
#             nums[lastsorted].link = list2
#             lastsorted = list2
#             list2 = nums[list2].link
#     if list1 == 0:
#         nums[lastsorted].link = list2
#     else:
#         nums[lastsorted].link = list1


########## Quick Sort ##########
# def QuickSort(low, high, nums):
#     pivot = 0
#     if high > low:
#         partition(low, high, pivot, nums)
#         QuickSort(low, pivot - 1, nums)
#         QuickSort(pivot + 1, high, nums)

# def partition(low, high, pivotpoint, nums):
#     pivotitem = nums[low]
#     j = low
#     for i in range(low + 1, high):
#         if nums[i] < pivotitem:
#             j += 1
#             temp = nums[i]
#             nums[i] = nums[j]
#             nums[j] = temp
#     pivotpoint = j
#     temp = nums[low]
#     nums[low] = nums[pivotpoint]
#     nums[pivotpoint] = temp


########## Quick Sort (using partition) ##########
# def QuickSortPartition()
# either on page 467 or 413


########## Heap Sort ##########
# class heap:
#     arr = []
#     heapsize = int

# def siftdown(heap, idx):
#     largerchild = 0
#     siftkey = heap.arr[idx]
#     parent = idx
#     spotfound = False
#     while 2 * parent <= heap.heapsize and not spotfound:
#         if 2 * parent < heap.heapsize and heap.arr[2 * parent] < heap.arr[2 * parent + 1]:
#             largerchild = 2 * parent + 1
#         else:
#             largerchild = 2 * parent
#         if siftkey < heap.arr[largerchild]:
#             heap.arr[parent] = heap.arr[largerchild]
#             parent = largerchild
#         else:
#             spotfound = True
#     heap.arr[parent] = siftkey

# def root(heap):
#     keyout = heap.arr[1]
#     heap.arr[1] = heap.arr[heap.heapsize]
#     heap.heapsize -= 1
#     siftdown(heap, 1)
#     return keyout

# def removekeys(n, heap, arr):
#     for i in range(n, 0, -1):
#         arr[i] = root(heap)

# def makeheap(n, heap):
#     heap.heapsize = n
#     for i in range(0, n/2, -1):
#         siftdown(heap, i)

# def HeapSort(n, heap):
#     makeheap(n, heap)
#     removekeys(n, heap, heap.arr)


########## Radix Sort ##########
# class nodetype:
#     keytype key
#     nodetype* link

# typedef nodetype* nodepointer

# def RadixSort(masterList, numdigits):
#     for i in range(numdigits):
#         distribute(masterList, i)
#         coalesce(masterList)

# def distribute(masterList, idx):
#     for j in range(9):
#         list[j] = None
#     p  = masterList
#     while p != None:
#         j = value of the ith digit (from the right) in p -> key
#         link p to the end of the list[j]
#         p = p -> link

# def coalesce(masterList):
#     masterList = None
#     for j in range(9):
#         link the nodes in list[j] to the end of the masterList


########## Helper Functions ##########

# Logs time in miliseconds before and after the algorithm runs
def getTime(function, arr):
    start = datetime.now()
    function(arr)
    end = datetime.now()
    return str(end - start)[5:]

def getAvg(function, arrSize, numOfTests):
    times = []
    testArray = np.random.randint(arrSize, size=arrSize)
    for i in range(numOfTests):
        times.append(float(getTime(function, testArray)))
    return '{:f}'.format(np.mean(times))

def runTests(function, numOfTests):
    print("___________________________________________")
    algorithm = str(function).split()[1]
    # test on random array of size 10 and printing the results
    size10 = np.random.randint(10, size=10)
    print(algorithm + " on array of size 10: \n\t" + str(size10))
    results = function(size10)
    print("     -> " + str(results))
    #sizes = [100, 1000, 10000, 100000]
    sizes = [5, 10, 25, 50]
    print("Average run times for " + algorithm + " on arrays of size:")
    for size in sizes:
        print(" " + str(size) + " -> " + getAvg(function, size, numOfTests) + " seconds")
    print("___________________________________________")

########## Execution ##########

runTests(ExchangeSort, 50)
