from datetime import datetime
import numpy as np

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
  
def BinaryInsertSort(nums):
    for i in range(1, len(nums)):
        temp = nums[i]
        j = BinarySearch(nums, temp, 0, i-1)
        for k in range(i, j, -1):
            nums[k] = nums[k-1]
        nums[j] = temp
    return nums

def BinarySearch(nums, val, start, high):
    if high - start <= 1:
        if val < nums[start]:
            return start - 1
        else:
            return start
    mid = (start + high)//2
    if nums[mid] <  val:
        return BinarySearch(nums, val, mid, high)
    elif nums[mid] > val:
        return BinarySearch(nums, val, start, mid)
    else:
        return mid

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
# def MergeSort2(nums):
#     low, mid = 0, 0
#     high = len(nums)
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
#https://github.com/alicepham/python-singly-linked-list-sorting-algos/blob/master/A4_Q2_V9.py
class Node:
        def __init__(self, data, next=None):
            self.data = data
            self.next = next
        def set_data(self, data):
            self.data = data
        def get_data(self):
            return self.data
        def set_next(self, next):
            self.next = next
        def get_next(self):
            return self.next
        def __str__(self):
            return "chair: " + self.data.name + " || " + str(self.data.personality)

class LinkedList:
        def __init__(self):
            self.head = None
            self.last = None
            self.length = 0

        def insert(self, num):
            '''inserts a person to the head of the classroom'''
            temp = num
            if self.head == None:
                '''case 2: classroom is empty'''
                self.head = temp
                self.last = temp
                self.length = 1
            else:
                temp.set_next(self.head)
                self.head = temp
                self.length += 1
        
        def print_list(self):
            '''prints the list'''
            a = []
            current = self.head
            while current != None:
                a.append(current.get_data().name + " : " + str(current.get_data().personality))
                current = current.get_next()
            print(a)
            
        def radix_sort(self):
            '''radix sort the classroom'''
            if self.head == None:
                print("The Classroom is empty!")
            elif self.head == self.last:
                print("There is only one person in the classroom")
            else:
                len_list = self.get_length()
                modulus = 10
                div = 1
                while True:
                    new_list = [[],[],[],[],[],[],[],[],[],[]]
                    current = self.head
                    while current != None:
                        current_value = current.get_data().personality
                        least_digit = current_value % modulus
                        least_digit /= div
                        least_digit = int(least_digit)
                        new_list[least_digit].append(current)
                        current = current.get_next()
                        #self.print_list()
                    modulus = modulus * 10
                    div = div * 10

                    if len(new_list[0]) == len_list:
                        print("done")
                        break
                    self.head = None
                    self.last = None #clears the classroom
                    A = [str(a) for i in new_list for a in i]
                    print(A)
                    print(" ")
                    for x in reversed(new_list):
                        for y in reversed(x):
                            self.insert(y.get_data())
        
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
#         link p to the high of the list[j]
#         p = p -> link

# def coalesce(masterList):
#     masterList = None
#     for j in range(9):
#         link the nodes in list[j] to the high of the masterList


########## Helper Functions ##########

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
    sizes = [100, 1000, 10000, 100000]
    #sizes = [5, 10, 25, 50]
    #sizes = [1]
    print("Average run times for " + algorithm + " on arrays of size:")
    for size in sizes:
        print(" " + str(size) + " -> " + getAvg(function, size, numOfTests) + " seconds")
    print("___________________________________________\n")

########## Execution ##########

# runtests(Name of Algorithm, Amount of times to be tested)

# runTests(ExchangeSort, 50)
# runTests(InsertSort, 50)

# Not sorting properly 
# runTests(BinaryInsertSort, 50)

# runTests(SelectionSort, 50)
# runTests(MergeSort, 50)

# RecursionError: maximum recursion depth exceeded in comparison
# runTests(QuickSort, 50)

# runTests(QuickSort2, 50)

linked = LinkedList()
linked.insert(7)
linked.insert(6)
linked.insert(1)
linked.insert(2)
linked.insert(5)
linked.insert(4)
linked.insert(3)

linked.print_list()