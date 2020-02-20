# Amanda Lawrence
# 10/21/2018
# CS 325 - Analysis of Algorithms
# HW4 - #4 - Activity Selection Last-to-Start Implementation

import math
import sys

def range_inclusive(start, stop):
	return range(start, stop+1)


# Read inputs from a file, act.txt
with open('act.txt', 'r') as f:
	lines = f.readlines()
	lines = [x.strip() for x in lines]
	data_temp = [x.split()[0:] for x in lines]
	data_sets = []
	for line in data_temp:
		data_sets.append([int(x) for x in line])


# This section takes the one, unruly list of numbers from our file act.txt, that is now in data_sets and reformats it.
# We set up each problem set of activities, as its own list, this_problem_set. Each problem set is contained in list_of_activites.
activity_amount = int(data_sets[0][0])
list_of_activities = []											# used to store an array of arrays. Stores a single problem set, and its activities (along with their start times and finish times)
current_index = 1   											# used to determine the first index of the first activity, and to step through each activity 
while current_index < len(data_sets):
	activity_amount = int(data_sets[current_index-1][0])
	this_problem_set = []
	for individual_activity in range(0, activity_amount):			# structure each activity block (an activity ID number, start time, and finish time) in its own array
		this_problem_set.append(data_sets[current_index+individual_activity])		# adds the set of [activity number, start time, end time] for each item, to this_activity
	current_index += activity_amount+1
	list_of_activities.append(this_problem_set)


# For each problem set in our list_of_activities, we will:
# Break this problem set out into three lists, one of start times, one of finish times, and one for the activity IDs.
# Call our insertion sort functions an sort our activities by start time, from the last starting time to the earliest start time. 
# Then, we will call activity_selector(a, s, f), with the sorted lists of activity IDs, start times, and list of end times as arguments.
def split_and_sort(activity):
	a_id = []				# the ID of the activity
	s = []					# start times
	f = []					#finish times
	for task in range(0, len(activity)):
		a_id.append(activity[task][0])
		s.append(activity[task][1])
		f.append(activity[task][2])
	sorted_IDs = []
	sorted_s = []
	sorted_f = []
	sorted_IDs, sorted_s, sorted_f = insertsort(a_id, s, f)
	return activity_selector(sorted_IDs, sorted_s, sorted_f)


#Insertion sort written in HW1, and adapted to sort the list of starting times, and move the activity_if, and finish times to the index of their corresponding start time
# This function actually sorts our start times from lowest/earliest/smallest to largest/latest, but it returns a reversed list for all three lists. 
def insertsort(activity_id, start, finish):
	for j in range(1, len(start), 1): 
		key = start[j]
		key_f = finish[j]
		key_a = activity_id[j]
		i = j-1
		while i > -1 and start[i] > key:
			start[i+1] = start[i]
			finish[i+1] = finish[i]
			activity_id[i+1] = activity_id[i]
			i = i-1
		start[i+1] = key
		finish[i+1] = key_f
		activity_id[i+1] = key_a
	activity_id = activity_id[::-1]
	start = start[::-1]
	finish = finish[::-1]
	return activity_id, start, finish



# We've already sorted each problem set of activities, based on the start time of each activity, sorted from highest/last starting time to the earliest.
# The following code, which is based on the pseudocode in our Introduction to Algorithms by CLRS, for GREEDY-ACTIVITY-SELECTOR on p.421.
# The GREEDY-ACTIVITY-SELECTOR pseudocode is a iterative function, that creates and returns a list of activites that we can successfully schedule.
# The major change I make to the pseudocode from the book, is to instead, consider the activities in order of decreasing (from later to earlier) start times. 
def activity_selector(activity_id, start, finish):
	n = len(start)
	A = [activity_id[0]]
	k = 0
	for m in range(1, n):
		if finish[m] <= start[k]:
			A.append(activity_id[m])
			k = m
	return A[::-1]




# The output is written to the terminal
x = 1
for a in list_of_activities:
	activities_list = split_and_sort(a) 
	activities_selected_n = len(activities_list)
	print 'Set ', x
	print 'Number of Activities Selected:  ', activities_selected_n
	sarr = [str(n) for n in activities_list]
	print 'Activities :  ', ' '.join(sarr)
	print '\n'
	x += 1
