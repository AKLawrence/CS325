# Amanda Lawrence
# 9/29/2018
# CS 325 - Analysis of Algorithms
# HW1 #4 - Merge Sort

import math
import sys


# Open our data.txt file and save each line of data as a list, within a list. We leave off the first value of each line in data.txt.
with open('data.txt', 'r') as f:
	lines = f.readlines()
	lines = [x.strip() for x in lines]
	data_temp = [x.split()[1:] for x in lines]
	data_sets = []
	for line in data_temp:
		data_sets.append([int(x) for x in line])
	print(data_sets)

# Merge function 
def merge(A, p, q, r):
	#print("-------------------------------------------------")
	#print("Running merge with (%d, %d, %d) ..." % (p, q, r))
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
	#print("L = %s" % str(L))
	#print("R = %s" % str(R))
	i = 0
	j = 0
	indexes = list(range(p, r+1, 1))
	#print("Will loop over k's: %s" % str(indexes))
	for k in indexes:
		#print("k = %d" % k)
		if L[i] <= R[j]:
			A[k] = L[i]
			i = i + 1
		else:
			A[k] = R[j]
			j = j + 1
	return A



# Merge sort algorithm adapted from pseudocode in Intro. to Algorithms textbook by: Cormen, Leiserson, Rivest, Stein; pages 34 and 31.
def mergesort(A, p, r):
	#print("Running MergeSort function")
	if p < r:
		q = int(math.floor((p + r)/2))
		#print("Got q = %d" % q)
		#print("len(A) = %d" % len(A))
		#print("Dividing A into (%d, %d) and (%d, %d) ... " % (p, q, q+1, r))
		#asdf = input()
		#print("Calling mergesort(A, %d, %d) ... " % (p,q))
		mergesort(A, p, q)
		#print("Calling mergesort(A, %d, %d) ... " % (q+1,r))
		mergesort(A, q+1, r)
		#print("Before merge, have " + str(A))
		merge(A, p, q, r)
		#print("After merge, have " + str(A))
	return A

# For each line of data, in our lines list, call and run mergesort() and append that sorted list to a new array called msort_answers
x = 0
msort_answers = []
for x in range(x, len(data_sets), 1):
	msort_answers.append(mergesort(data_sets[x], 0, len(data_sets[x])-1))
	#sys.exit(0)

y = 0
with open('merge.out', 'w') as f:
	for y in range(0, len(msort_answers), 1):
		output_txt = ' '.join([str(x) for x in msort_answers[y]])
		f.write(output_txt + '\n')
	