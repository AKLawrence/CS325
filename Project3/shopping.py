# Amanda Lawrence
# 10/13/2018
# CS 325 - Analysis of Algorithms
# HW3 - #2c - Shopping Spree

import math
import sys

def range_inclusive(start, stop):
	return range(start, stop+1)


# Read inputs from a file, shopping.txt
with open('shopping.txt', 'r') as f:
	lines = f.readlines()
	lines = [x.strip() for x in lines]
	data_temp = [x.split()[0:] for x in lines]
	data_sets = []
	for line in data_temp:
		data_sets.append([int(x) for x in line])


# This section takes the one, unruly list of numbers from our file shopping.txt, that is now in data_sets and reformats it.
# We set up each individual test_case with its own list object, this_test_case, and append that into list_of_test_cases.
test_cases = int(data_sets[0][0])
list_of_test_cases = []
current_index = 1   									# used to determine the first index of a new test case
for individual_case in range(1, test_cases+1):			# structure each test case in its own array
	this_test_case = [] 								# used to contain all the data for a single test case, including the price and weight of items, and family members
	items = int(data_sets[current_index][0])    		# number of items in a test case
	this_test_case.append(items)						# add the number of items to the test case array
	for each in range(1, items+1):	
		this_test_case.append(data_sets[current_index+each])	# adds the set of [price, weight] for each item, to this_test_case
	num_in_fam = int(data_sets[current_index+(items+1)][0])
	this_test_case.append(num_in_fam)
	for each in range(1, num_in_fam+1):
		this_test_case.append(int(data_sets[current_index+(items+1)+each][0]))		# append in the max weight (as an int) each family member can carry, to this_test_case array
	current_index += (items+1) + (num_in_fam+1)
	list_of_test_cases.append(this_test_case)



# Pseudocode adapted from week 3, Lecture 3: 0-1 Knapsack
def shopping(A, test_case_num):
	num_of_items = int(A[0])

	num_in_fam = int(A[(num_of_items+1)])
	max_possible_capacity = max(A[(num_of_items+2)], A[len(A)-1])			# takes the maximum weight that any family member can carry, in this test_case

	total_price = 0 			# the total price, tallies up the total, for the price each family member gets from their haul.
	temp_output = []			# used to store "Member Items" for each family member's list of items, will later be added to the test_case_output
	test_case_output = []		# Creates the output list for this testcase, which will be written to the output file


	# creating a table, and initializing the first row and column to have values of 0
	# The table is setup:  max_price_table[item][weight] = price of item.
	max_price_table = [[0 for x in range(max_possible_capacity+1)] for y in range(num_of_items+1)]		# creates a 2D table, with columns=num_of_items+1, and rows=max_possible_capacity+1. Values initialized as 0.
	items_used_lookup = [[" " for x in range(max_possible_capacity+1)] for y in range(num_of_items+1)]	# table used to store list of items (their individual prices) for its corresponding location in max_price_table

	item_list = A[1:A[0]+1]
	nweights = A[A[0]+1]
	first = A[0]+2
	weight_limits = A[first:first+nweights]

	max_possible_capacity = max(weight_limits)
	
	for i in range_inclusive(1, num_of_items):
		this_item = i-1
		iprice, iweight = item_list[this_item]
		for w in range_inclusive(1, (max_possible_capacity)):
			if iweight > w:   					# if this item's weight is lower than the max_possible_capacity...
				max_price_table[i][w] = max_price_table[i-1][w]
				items_used_lookup[i][w] = items_used_lookup[i-1][w]
			else:
				max_price_table[i][w] = max(max_price_table[i-1][w], max_price_table[i-1][w-iweight] + iprice)
				if max_price_table[i-1][w] > max_price_table[i-1][w-iweight] + iprice:
					items_used_lookup[i][w] = items_used_lookup[i-1][w]
				else:
					items_used_lookup[i][w] = str(items_used_lookup[i-1][w-iweight]) + str(" ") + str(i)

	test_case_output.extend(["Test Case ", test_case_num, "\n"]) 

	for each_member in range_inclusive(1, num_in_fam):
		temp_items, temp_value = calculate_member_items(max_price_table, items_used_lookup, int(A[((num_of_items+1)+each_member)]))
		temp_output.extend([each_member, ":   ", temp_items, "\n"])	
		total_price += temp_value

	test_case_output.extend(["Total Price:  ", total_price, "\n", "Member Items ", "\n"])
	test_case_output.extend(temp_output)

	return test_case_output




# looks up and returns each person's list of items they can carry, and the sum value of their items.
def calculate_member_items(price_table, items_table, personal_capacity):
	my_best_value = price_table[-1][personal_capacity]
	my_items = items_table[-1][personal_capacity]
	return my_items, my_best_value



# The output should be written to a file called shopping.out
x = 0
shopping_answers = []
test_case_number = 1
for tc in list_of_test_cases:
	shopping_answers.append(shopping(tc, test_case_number))
	test_case_number += 1

y = 0
with open('shopping.out', 'w') as f:
	for y in range(0, len(shopping_answers), 1):
		output_txt = ' '.join([str(x) for x in shopping_answers[y]])
		f.write(output_txt + '\n')