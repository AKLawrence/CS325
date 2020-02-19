# Amanda Lawrence
# 9/29/2018
# CS 325 - Analysis of Algorithms
# HW1 #5 - Insertion Sort Running Time Analysis, generating random of values to sort. Output the array size, n, and time to the terminal

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


# Insertion sort algorithm adapted from pseudocode in Intro. to Algorithms textbook by: Cormen, Leiserson, Rivest, Stein; page 26.
# Insertion sort will take in the file, data.txt
# The first integer on each line of the file will be n, the number of values to be sorted, followed by the values to be sorted (on the same line)

def insertsort(A):
	for j in range(1, len(A), 1): 
		key = A[j]
		#insert A[j] into the sorted sequence A[1.. j-1]
		i = j-1
		while i > -1 and A[i] > key:
			A[i+1] = A[i]
			i = i-1
		A[i+1] = key
	return A

# For each line of data, in each array, call and run insertsort(A), calculate, and append the time it takes to run this algorithm, on average, 10 times.
def determineRunTime(A):
	x = 0
	tik = time.time()
	niters = 10
	for ii in range(niters):
		results = insertsort(A)
	tok = time.time()
	print("For an array of %d values, Insertion Sort takes: " % (len(A)))
	print("Total of %15.8f seconds for %d attempts." % (tok-tik, niters))
	print("Average time taken: %15.8f seconds" % ((tok-tik)/float(niters)))


determineRunTime(A5000)
determineRunTime(A10000)
determineRunTime(A15000)
determineRunTime(A20000)
determineRunTime(A30000)
determineRunTime(A40000)
determineRunTime(A50000)

