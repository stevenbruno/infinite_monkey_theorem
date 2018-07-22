""" 
Various searching and sorting algorithms implemented in Python.
From Miller & Ranum Problem Solving with Algorithms and Data Structures
Author: Steven Bruno
June 7, 2018
"""

# Binary Search

def binarySearch(alist, item):
	first = 0
	last = len(alist)-1
	found = False

	while first<=last and not found:
		midpoint = (first + last)//2
		if alist[midpoint] == item:
			found = True
		else:
			if item < alist[midpoint]:
				last = midpoint - 1
			else:
				first = midpoint + 1

	return found


# Recursive Binary Search

def recBinarySearch(alist, first, last, item):
	midpoint = (first + last)//2

	if midpoint == first and midpoint == last:
		if alist[midpoint] == item:
			return True
		else:
			return False

	else: 
		if alist[midpoint] == item:
			return True
		else:
			if item < alist[midpoint]:
				last = midpoint - 1
				return recBinarySearch(alist, first, last, item)
			else:
				first = midpoint + 1
				return recBinarySearch(alist, first, last, item)


# Short Bubble Sort (called short because potential to finish early)

def shortBubbleSort(alist):
	exchanges = True
	passnum = len(alist)-1
	while passnum > 0 and exchanges:
		exchanges = False
		for i in range(passnum):
			if alist[i]>alist[i+1]:
				exchanges = True
				temp = alist[i]
				alist[i] = alist[i+1]
				alist[i+1] = temp
			passnum = passnum-1


# Selection Sort

def selectionSort(alist):
	for fillslot in range(len(alist)-1, 0, -1):
		positionOfMax = 0
		for location in range(1, fillslot+1):
			if alist[location] > alist[positionOfMax]:
				positionOfMax = location

		temp = alist[fillslot]
		alist[fillslot] = alist[positionOfMax]
		alist[positionOfMax] = temp


# Insertion Sort

def insertionSort(alist):
	for index in range(1, len(alist)):

		current_value = alist[index]
		position = index

	while position > 0 and alist[position - 1] > alist[position]:
		alist[position] = alist[position-1]
		position -= 1

	alist[position] = current_value


# Shell Sort (somewhere between O(n) and O(n2), depends on increment)

def shellSort(alist): 
	sublistcount = len(alist)//2
	while sublistcount > 0:
		for startposition in range(sublistcount):
			gapInsertionSort(alist, startposition, sublistcount)

		print("After increments of size", sublistcount, ", the list is ", alist)

		sublistcount = sublistcount // 2

def gapInsertionSort(alist, start, gap):
	for i in range(start+gap, len(alist), gap):
		currentvalue = alist[i]
		position = i

		while position >= gap and alist[position-gap] > currentvalue:
			alist[position]=alist[position-gap]
			position = position-gap


		alist[position] = currentvalue


# Merge Sort O(nlogn) (except the slice makes this an underestimate)

def mergeSort(alist):
    print("Splitting ",alist)
    if len(alist)>1:
        mid = len(alist)//2
        lefthalf = alist[:mid] #slicing is O(k), can potentially be removed to optimize the sort
        righthalf = alist[mid:]

        mergeSort(lefthalf)
        mergeSort(righthalf)

        i=0
        j=0
        k=0
        while i < len(lefthalf) and j < len(righthalf):
            if lefthalf[i] < righthalf[j]:
                alist[k]=lefthalf[i]
                i=i+1
            else:
                alist[k]=righthalf[j]
                j=j+1
            k=k+1

        while i < len(lefthalf):
            alist[k]=lefthalf[i]
            i=i+1
            k=k+1

        while j < len(righthalf):
            alist[k]=righthalf[j]
            j=j+1
            k=k+1
    print("Merging ",alist)


# Quick Sort: best case O(nlogn), worst close to O(n2), sorts in place, can be improved with median of three 
def quickSort(alist):
   quickSortHelper(alist,0,len(alist)-1)

def quickSortHelper(alist,first,last):
   if first<last:

       splitpoint = partition(alist,first,last)

       quickSortHelper(alist,first,splitpoint-1)
       quickSortHelper(alist,splitpoint+1,last)

def partition(alist,first,last):
   pivotvalue = alist[first]

   leftmark = first+1
   rightmark = last

   done = False
   while not done:

       while leftmark <= rightmark and alist[leftmark] <= pivotvalue:
           leftmark = leftmark + 1

       while alist[rightmark] >= pivotvalue and rightmark >= leftmark:
           rightmark = rightmark -1

       if rightmark < leftmark:
           done = True
       else:
           temp = alist[leftmark]
           alist[leftmark] = alist[rightmark]
           alist[rightmark] = temp

   temp = alist[first]
   alist[first] = alist[rightmark]
   alist[rightmark] = temp


   return rightmark

if __name__ == '__main__':
	alist = [54,26,93,17,77,31,44,55,20]
	quickSort(alist)
	print(alist)