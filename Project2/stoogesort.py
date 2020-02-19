# Amanda Lawrence
# 10/6/2018
# CS 325 - Analysis of Algorithms
# HW2 - #5a - Stooge Sort

import math
import sys


# Read inputs from a file, data.txt, where the first value of each line is the number of integers that need to be sorted, followed by the values to sort. 
with open('data.txt', 'r') as f:
	lines = f.readlines()
	lines = [x.strip() for x in lines]
	data_temp = [x.split()[1:] for x in lines]
	data_sets = []
	for line in data_temp:
		data_sets.append([int(x) for x in line])
	#print(data_sets)


# stoogesort written from pseudocode in HW2 #4 
def stoogesort(A, low, high):
	print("__________________________________________")
	if (high >= len(A)):
		#print("INSANE: index %d is beyond limit of A (%d elements)" % (high, len(A)))
		sys.exit(1)
	n = high - low + 1
	print("To start this round, A is:", A)
	print("n is ", n)
	if n==2 and A[low] > A[high]:
		print("Swapping the A[min] and A[max] values")
		print("A[low] is", A[low])
		print("A[high] is", A[high])
		temp = A[low]
		A[low] = A[high]
		A[high] = temp
	if n > 2:
		print("In the ELIF statement")
		m = int(math.ceil(((2.0*n)/3.0)))
		print("m is: ", m)
		print("starting a stoogesort on ", low)
		print("ending the stoogesort on ", m-1)
		stoogesort(A, low, low+(m-1))
		print("stoogesort number 2?")
		print("n-m is: ", n-m)
		stoogesort(A, low + (n-m), low + (n-1))
		print("stoogesort number 3?")
		stoogesort(A, low, low + (m-1))
	print(A)
	return A



# The sorted output should be written to a file called stooge.out
x = 0
ssort_answers = []
for ds in data_sets:
	ssort_answers.append(stoogesort(ds, 0, len(ds)-1))

y = 0
with open('stooge.out', 'w') as f:
	for y in range(0, len(ssort_answers), 1):
		output_txt = ' '.join([str(x) for x in ssort_answers[y]])
		f.write(output_txt + '\n')