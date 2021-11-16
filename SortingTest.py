from datetime import datetime
import numpy as np

########## Initialization ##########
size10 = np.random.randint(10, size=10)
size100 = np.random.randint(100, size=100)
size1000 = np.random.randint(1000, size=1000)
size10000 = np.random.randint(10000, size=10000)
size100000 = np.random.randint(100000, size=100000)

print(size10)

########## Exchange Sort ##########
def ExchangeSort(nums):
    print("Exchange Sort on: \n\t" + str(nums))
    for i in range(len(nums)):
        for j in range(len(nums)):
            if nums[i] < nums[j]:
                temp = nums[i]
                nums[i] = nums[j]
                nums[j] = temp
    print("     -> " + str(nums))
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
    print("     -> " + str(nums))
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

########## Quick Sort ##########

########## Quick Sort (using partition) ##########
def QuickSortPartition(low, high, nums):
    pivot = 0
    if high > low:
        partition(low, high, pivot, nums)
        QuickSortPartition(low, pivot - 1, nums)
        QuickSortPartition(pivot + 1, high, nums)

def partition(low, high, pivotpoint, nums):
    pivotitem = nums[low]
    j = low
    for i in range(low + 1, high):
        if nums[i] < pivotitem:
            j += 1
            temp = nums[i]
            nums[i] = nums[j]
            nums[j] = temp
    pivotpoint = j
    temp = nums[low]
    nums[low] = nums[pivotpoint]
    nums[pivotpoint] = temp
########## Heap Sort ##########

########## Radix Sort ##########

########## Execution ##########

#ExchangeSort(size10)
#InsertSort(size10)
#BinaryInsertSort(size10)
#SelectionSort(size10)

print(size10)
QuickSortPartition(0, len(size10) - 1, size10 )
print(size10)
