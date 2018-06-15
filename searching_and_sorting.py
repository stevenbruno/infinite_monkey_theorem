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


if __name__ == '__main__':
	testlist = [0, 1, 2, 8, 14, 18, 36, 101]
	print(binarySearch(testlist, 12))
	print(recBinarySearch(testlist, 0, len(testlist)-1, 12))


# Short Bubble Sort (called short because potential to finish early)

def shortBubbleSort(alist):
	exchanges - True
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


