# Amanda Lawrence
# 9/29/2018
# CS 325 - Analysis of Algorithms
# HW1 #5 - Merge Sort Running Time Analysis, generating a random string of values to sort

import math
import sys
import random
import time


# Create the arrays of sizes: 5000, 10000, 15000, 20000, 30000, 40000, and 50000 and populate them using randomly generated values from 0 to 10000
A5000 = [random.randint(1,10000) for n in range(5000)]
A10000 = [random.randint(1,10000) for n in range(10000)]
A15000 = [random.randint(1,10000) for n in range(15000)]
A20000 = [random.randint(1,10000) for n in range(20000)]
A30000 = [random.randint(1,10000) for n in range(30000)]
A40000 = [random.randint(1,10000) for n in range(40000)]
A50000 = [random.randint(1,10000) for n in range(50000)]


# Merge function 
def merge(A, p, q, r):
	n1 = q - p + 1
	n2 = r - q
	L = list(range(n1+1))
	R = list(range(n2+1))
	for i in range(0, n1, 1):
		L[i] = A[p + i]
	for j in range(0, n2, 1):
		R[j] = A[q + j + 1]
	L[n1] = float('inf')
	R[n2] = float('inf')
	i = 0
	j = 0
	indexes = list(range(p, r+1, 1))
	for k in indexes:
		if L[i] <= R[j]:
			A[k] = L[i]
			i = i + 1
		else:
			A[k] = R[j]
			j = j + 1
	return A



# Merge sort algorithm adapted from pseudocode in Intro. to Algorithms textbook by: Cormen, Leiserson, Rivest, Stein; pages 34 and 31.
def mergesort(A, p, r):
	if p < r:
		q = int(math.floor((p + r)/2))
		mergesort(A, p, q)
		mergesort(A, q+1, r)
		merge(A, p, q, r)
	return A


def determineRunTime(A):
	x = 0
	tik = time.time()
	niters = 10
	for ii in range(niters):
		results = mergesort(A, 0, len(A)-1)
	tok = time.time()
	print("For an array of %d values, Merge Sort takes: " % (len(A)))
	print("Total of %15.8f seconds for %d attempts." % (tok-tik, niters))
	print("Average time taken: %15.8f seconds" % ((tok-tik)/float(niters)))


determineRunTime(A5000)
determineRunTime(A10000)
determineRunTime(A15000)
determineRunTime(A20000)
determineRunTime(A30000)
determineRunTime(A40000)
determineRunTime(A50000)


