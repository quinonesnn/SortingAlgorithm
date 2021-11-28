from datetime import datetime
import numpy as np
import random
import heapq

########## Initialization ##########
array = np.random.randint(10, size=10)
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
    for i in range(1, len(nums)):
        key = nums[i]
        j = i-1
        while j >=0 and key < nums[j] :
                nums[j+1] = nums[j]
                j -= 1
        nums[j+1] = key
    return nums


########## Binary Insert Sort ##########
  
def BinaryInsertSort(array):
    for i in range(1, len(array)):
        temp = array[i]
        pos = BinarySearch(array, temp, 0, i) + 1
 
        for k in range(i, pos, -1):
            array[k] = array[k - 1]
 
        array[pos] = temp
    return array

def BinarySearch(array, key, strt, end):
    if end - strt <= 1:
        if key < array[strt]:
            return strt - 1
        else:
            return strt
 
    middle = (strt + end)//2
    if array[middle] < key:
        return BinarySearch(array, key, middle, end)
    elif array[middle] > key:
        return BinarySearch(array, key, strt, middle)
    else:
        return middle

########## Selection Sort ##########
def SelectionSort(nums):
    size =  len(nums)
    for step in range(size):
        min_idx = step
        for i in range(step + 1, size):
            if nums[i] < nums[min_idx]:
                min_idx = i
        nums[step], nums[min_idx] = nums[min_idx], nums[step]
    return nums

########## Merge Sort ##########
def MergeSort(nums):
    if len(nums) == 1:
        return nums
    mid = len(nums) // 2
    left = MergeSort(nums[:mid])
    right = MergeSort(nums[mid:])
    return Merge(left, right)

def Merge(left, right):
    output = []
    i = j = 0
    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            output.append(left[i])
            i += 1
        else:
            output.append(right[j])
            j += 1
    output.extend(left[i:])
    output.extend(right[j:])
    return output

########## Merge Sort 2 ##########

















########## Merge Sort 4 (Linked List) ##########
class Node:
    def __init__(self,data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    def append(self, new_value):
        new_node = Node(new_value)     
        if self.head is None:
            self.head = new_node
            return
        curr_node = self.head
        while curr_node.next is not None:
            curr_node = curr_node.next
        curr_node.next = new_node

    def sortedMerge(self, a, b):
        result = None
        if a == None:
            return b
        if b == None:
            return a
        if a.data <= b.data:
            result = a
            result.next = self.sortedMerge(a.next, b)
        else:
            result = b
            result.next = self.sortedMerge(a, b.next)
        return result
     
    def mergeSort(self, h):
        if h == None or h.next == None:
            return h
        middle = self.getMiddle(h)
        nexttomiddle = middle.next

        middle.next = None

        left = self.mergeSort(h)
         
        right = self.mergeSort(nexttomiddle)
 
        sortedlist = self.sortedMerge(left, right)
        return sortedlist
     
    def getMiddle(self, head):
        if (head == None):
            return head
 
        slow = head
        fast = head
 
        while (fast.next != None and
               fast.next.next != None):
            slow = slow.next
            fast = fast.next.next
             
        return slow
         
def printList(head):
    if head is None:
        print(' ')
        return
    curr_node = head
    while curr_node:
        print(curr_node.data, end = " ")
        curr_node = curr_node.next
    print(' ')

########## Quick Sort ##########
# Made this function only take the array to make it cleaner with the helper functions
def QuickSort(nums):
    low = 0
    high = len(nums) - 1
    # Recursive step
    def recQuickSort(nums, low, high):
        if low >= high:
            return
        pivot = partition(nums, low, high)
        recQuickSort(nums, low, pivot-1)
        recQuickSort(nums, pivot+1, high)
    recQuickSort(nums, low, high)
    return nums
        
def partition(nums, low, high):
    pivot = low
    for i in range(low+1, high+1):
        if nums[i] <= nums[low]:
            pivot += 1
            nums[i], nums[pivot] = nums[pivot], nums[i]
    nums[pivot], nums[low] = nums[low], nums[pivot]
    return pivot

########## Quick Sort (using partition) ##########
# def QuickSort2(nums):
#     low = 0
#     high = len(nums) - 1
#     # Recursive step
#     def recQuickSort2(nums, low, high):
#         if low >= high:
#             return
#         pivot = partition2(nums, low, high)
#         recQuickSort2(nums, low, pivot-1)
#         recQuickSort2(nums, pivot+1, high)
#     recQuickSort2(nums, low, high)
#     return nums

# def partition2(nums, low, high):
#     pivot = nums[low]
#     i = low
#     j = high + 1
#     while True:
#         i += 1
#         if i < high and nums[i] <= pivot:
#             break
#     while True:
#         j -= 1
#         if nums[j] > pivot:
#             break
#     while i < j:
#         nums[i], nums[j] = nums[j], nums[i]
#         while True:
#             i += 1
#             if nums[i] <= pivot:
#                 break
#         while True:
#             j -= 1
#             if nums[j] > pivot:
#                 break
#     pivot = j
#     nums[low], nums[pivot] = nums[pivot] , nums[low]
#     return pivot
# either on page 467 or 413


########## Heap Sort ##########
def HeapSort(arr):
    n = len(arr)
    for i in range(n//2 - 1, -1, -1):
        heapify(arr, n, i)
    for i in range(n-1, 0, -1):
        arr[i], arr[0] = arr[0], arr[i]  # swap
        heapify(arr, i, 0)
    return arr

def heapify(arr, n, i):
    largest = i  
    l = 2 * i + 1
    r = 2 * i + 2
    if l < n and arr[largest] < arr[l]:
        largest = l
    if r < n and arr[largest] < arr[r]:
        largest = r
    if largest != i:
        arr[i], arr[largest] = arr[largest], arr[i]  # swap
        heapify(arr, n, largest)
 
########## Radix Sort ##########
# class Node:
#         def __init__(self, data, next=None):
#             self.data = data
#             self.next = next
#         def set_data(self, data):
#             self.data = data
#         def get_data(self):
#             return self.data
#         def set_next(self, next):
#             self.next = next
#         def get_next(self):
#             return self.next

# class LinkedList:
#         def __init__(self):
#             self.head = None
#             self.last = None
#             self.length = 0

#         def insert(self, num):
#             temp = Node(num)
#             if self.head == None:
#                 self.head = temp
#                 self.last = temp
#                 self.length = 1
#             else:
#                 temp.set_next(self.head)
#                 self.head = temp
#                 self.length += 1

#         def get_length(self):
#             return self.length
        
#         def print_list(self):
#             output = []
#             current = self.head
#             while current != None:
#                 output.append(current.get_data())
#                 current = current.get_next()
#             print(output)
            
#         def radix_sort(self):
#             output = []
#             if self.head == None:
#                 return output
#             elif self.head == self.last:
#                 return output
#             else:
#                 len_list = self.get_length()
#                 modulus = 10
#                 div = 1
#                 while True:
#                     new_list = [[],[],[],[],[],[],[],[],[],[]]
#                     current = self.head
#                     while current != None:
#                         current_value = current.get_data()
#                         least_digit = current_value % modulus
#                         least_digit /= div
#                         least_digit = int(least_digit)
#                         new_list[least_digit].append(current)
#                         current = current.get_next()
#                     modulus = modulus * 10
#                     div = div * 10

#                     if len(new_list[0]) == len_list:
#                         break
#                     self.head = None
#                     self.last = None
#                     for x in reversed(new_list):
#                         for y in reversed(x):
#                             self.insert(y.get_data())
#                     output = [str(a) for i in new_list for a in i]
#                     return output




########## Array Helper Functions ##########

# Logs time in miliseconds before and after the algorithm runs
def getTime(function, arr):
    start = datetime.now()
    function(arr)
    high = datetime.now()
    return str(high - start)[5:]

def getAvg(function, arrSize, numOfTests):
    times = []
    testArray = np.random.randint(arrSize, size=arrSize)
    for i in range(numOfTests):
        times.append(float(getTime(function, testArray)))
    return '{:f}'.format(np.mean(times))

def runTests(function, numOfTests):
    print("\n___________________________________________")
    algorithm = str(function).split()[1]
    # test on random array of size 10 and printing the results
    size10 = np.random.randint(10, size=10)
    print(algorithm + " on array of size 10: \n\t" + str(size10))
    results = function(size10)
    print("     -> " + str(results))
    #sizes = [100, 1000, 10000, 100000]
    sizes = [5, 10, 25, 50]
    #sizes = [1]
    print("Average run times for " + algorithm + " on arrays of size:")
    for size in sizes:
        print(" " + str(size) + " -> " + getAvg(function, size, numOfTests) + " seconds")
    print("___________________________________________\n")


########## Linked List Helper Functions ##########
def randomLinked(size):
    linked = LinkedList()
    for i in range(size):
        linked.append(random.randint(0,size))
    return linked

def getLinkedAvg(numOfTests, arrSize):
    times = []
    linked = randomLinked(arrSize)
    for i in range(numOfTests):
        start = datetime.now()
        linked.mergeSort(linked.head)
        high = datetime.now()
        time = str(high - start)[5:]
        times.append(float(time))
    return '{:f}'.format(np.mean(times))

def runLinkedTests(numOfTests):
    print("\n___________________________________________")
    size10 = randomLinked(10)
    print("MergeSort4 on linked list of size 10: \n\t")
    printList(size10.head)
    size10.head = size10.mergeSort(size10.head)
    printList(size10.head)

    print("Average run times for mergesort on linked list of size:")
    sizes = [5, 10, 25, 50]
    for size in sizes:
        print(" " + str(size) + " -> " + getLinkedAvg(numOfTests, size) + " seconds")
    print("\n___________________________________________")
    
########## Execution ##########

# runtests(Name of Algorithm, Amount of times to be tested)

# runTests(ExchangeSort, 50)
# runTests(InsertSort, 50)
# runTests(BinaryInsertSort, 50)
# runTests(SelectionSort, 50)
# runTests(MergeSort, 50)

# runTests(MergeSort2, 50)

# runLinkedTests(50)
# runTests(QuickSort, 50)

# runTests(QuickSort2, 50)

# runTests(HeapSort, 50)


# linked.print_list()
# linked.radix_sort()
# print("_--------------------------")
# linked.print_list()