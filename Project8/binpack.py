# Amanda Lawrence
# 11/24/2018
# CS 325 - Analysis of Algorithms
# HW 8: Problem 1


import math
import sys
import copy

def range_inclusive(start, stop):
	return range(start, stop+1)


# Read inputs from a file, bin.txt
with open('bin.txt', 'r') as f:
	lines = f.readlines()
	lines = [x.strip() for x in lines]
	data_temp = [x.split()[0:] for x in lines]
	data_set = []
	for line in data_temp:
		data_set.append([str(x) for x in line])

#print (data_set)


# This section takes the one, unruly list of numbers, that is now in data_set and reformats it.
# We assign values to num_of_test_cases, bin_capacity, num_of_items.
# We create a list for the values of weights for each item, called weights.
# all of these values will be contained in a list, list_of_test_cases
num_of_test_cases = int(data_set[0][0])							# the number of testcases in file
list_of_test_cases = []
current_index = 1
for individual_case in range(1, num_of_test_cases+1):			# structure each test case in its own list
	this_test_case = [] 								# used to contain all the data for a single test case
	bin_capacity = int(data_set[current_index][0])		# capacity for bins for this test case
	this_test_case.append(bin_capacity)					# add the bin_capacity to the test case list
	items = int(data_set[current_index+1][0])    		# number of items in a test case
	this_test_case.append(items)						# add the number of items to the test case list
	weights = []
	for each in range(1, 2):	
		for each_items in range(1, items+1):	
			weights.append(data_set[current_index+2][each_items-1])	# adds the set of weights for each item, to this_test_case
	this_test_case.append(weights)
	current_index += 3
	list_of_test_cases.append(this_test_case)


'''FIRST FIT PSEUDOCODE:
For all items, i, from 1 to total number of items:
	For all bins, b, from 1 to the total number of bins:
		If the current item fits in the current bin:
			Pack the item, i, into the bin, b.
			Break, and move onto the next item.
	If the item, i, did not fit in any available bin:
		Create a new bin and pack item i, into it. 
'''
def first_fit(test_case_list):
	bins = []
	for i in range(0, len(test_case_list[2])):
		for b in range_inclusive(1, len(bins)):
			if (len(bins) >= 0):
				if (int(test_case_list[2][i]) + int(bins[b-1]) <= int(test_case_list[0])):			# if the current item, i, plus the current bin is less than or equal to possible capacity...
					bins[b-1] = int(bins[b-1]) + int(test_case_list[2][i]) 						# pack the item, i, into the current bin
					break
			else:
				break
		else:												# if there are no bins in bins list, OR, item i did not find a bin yet....
			bins.append(int(0))
			bins[-1] = int(bins[-1]) + int(test_case_list[2][i])
	return len(bins)


'''FIRST FIT DECREASING PSEUDOCODE:
Sort items, so they are in decreasing order
For all items, i, from the largest to smallest item:
	For all bins, b, from 1 to the total number of bins:
		If the current item fits in the current bin:
			Pack the item, i, into the bin, b.
			Break, and move onto the next item.
	If the item, i, did not fit in any available bin:
		Create a new bin and pack item i, into it. 
'''
def first_fit_decreasing(test_case_list):
	sorted_list = copy.deepcopy(test_case_list[2])
	sorted_list.sort(key=int, reverse=True)
	bins = []
	for i in range(0, len(sorted_list)):
		for b in range_inclusive(1, len(bins)):
			if (len(bins) >= 0):
				if (int(sorted_list[i]) + int(bins[b-1]) <= int(test_case_list[0])):			# if the current item, i, plus the current bin is less than or equal to possible capacity...
					bins[b-1] = int(bins[b-1]) + int(sorted_list[i]) 						# pack the item, i, into the current bin
					break
			else:
				break
		else:												# if there are no bins in bins list, OR, item i did not find a bin yet....
			bins.append(int(0))
			bins[-1] = int(bins[-1]) + int(sorted_list[i])
	return len(bins)


''' BEST FIT PSEUDOCODE:
For all items, i, from 1 to the total number of items
	For all bins, b, from 1 to the total number of bins
		If an item, i, fits in bin, b
			Calculate the remaining capacity after the item has been added
	Pack the item, i, in bin, b, where b is the bin with the minimum remaining capacity after adding the item i.
	If no such bin exists, open/create a new bin and add the item.
'''
def best_fit(test_case_list):
	bins = []
	for i in range(0, len(test_case_list[2])):
		min_remaining_capacity = 100000
		chosen_bin = -100000
		for b in range_inclusive(1, len(bins)):
			if (len(bins) >= 0):
				if (int(test_case_list[2][i]) + int(bins[b-1]) <= int(test_case_list[0])) and (test_case_list[0] - (int(test_case_list[2][i]) + int(bins[b-1])) < min_remaining_capacity ):
					chosen_bin = b-1
		if chosen_bin >= 0:
			bins[int(chosen_bin)] = int(bins[int(chosen_bin)]) + int(test_case_list[2][i])
		if chosen_bin < 0:											# if there are no bins in bins list....
			bins.append(int(0))
			bins[-1] = int(bins[-1]) + int(test_case_list[2][i])
	return len(bins)





#OUTPUT
# The output is written to the terminal
x = 1
for a in list_of_test_cases:
	print 'Test Case ', x, ' First Fit:  ', first_fit(list_of_test_cases[x-1]), ', First Fit Decreasing:  ', first_fit_decreasing(list_of_test_cases[x-1]), ', Best Fit: ', best_fit(list_of_test_cases[x-1])
	x += 1
