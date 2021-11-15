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
    for i in range(2, len(nums)):
        temp = nums[i]
        j = i - 1
        while j > 0 and nums[j] > temp:
            nums[j + 1] = nums[j]
            j -= 1
        nums[j+1] = temp
    print("     -> " + str(nums))
    return nums


########## Binary Insert Sort ##########

########## Selection Sort ##########

########## Merge Sort ##########

########## Merge Sort 2 ##########

########## Merge Sort 4 (Linked List) ##########

########## Quick Sort ##########

########## Quick Sort (using partition) ##########

########## Heap Sort ##########

########## Radix Sort ##########

########## Execution ##########

#ExchangeSort(size10)
InsertSort(size10)