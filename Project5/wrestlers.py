# Amanda Lawrence
# 11/3/2018
# CS 325 - Analysis of Algorithms
# HW 5: Problem 4.c.


import math
import sys

def range_inclusive(start, stop):
	return range(start, stop+1)


# Read inputs from a file, based on input in command line argument
# Specified as sys.argv[1] in order to ignore the first argument, technically, which is the wrestlers.py file.
filename = sys.argv[1]				
with open(filename, 'r') as f:
	lines = f.readlines()
	lines = [x.strip() for x in lines]
	data_temp = [x.split()[0:] for x in lines]
	data_set = []
	for line in data_temp:
		data_set.append([str(x) for x in line])


# This section takes the one, unruly list of numbers and wrestler names and rivalries, that is now in data_set and reformats it.
# We set up the list of wrestlers, as its own dict, wrestler_dict. 
# We set up the rivalries as a list of lists, rivalry_lists.
num_of_wrestlers = int(data_set[0][0])							# the number of wrestlers in wrestler_dict
wrestler_dict = {}												# used to store a dict of wrestler names.
rivalry_lists = []
babyfaces = []
heels = []
current_index = 1   											# used to determine the first index of the first wrestler, and to step through each wrestler, and then rivarlies 
while current_index <= num_of_wrestlers:
	if current_index == 1:
			wrestler_dict.update({data_set[current_index][0]: current_index-1})
			babyfaces.append(list(wrestler_dict.keys())[0])
	else:
		wrestler_dict.update({data_set[current_index][0]: current_index-1})
	current_index += 1

for each_rivalry in range_inclusive(1, int(data_set[num_of_wrestlers+1][0])):			# structure each activity block (an activity ID number, start time, and finish time) in its own array
	rivalry_lists.append(data_set[current_index+each_rivalry])		# adds the set of [activity number, start time, end time] for each item, to this_activity



# Creating our adjacency list to represent a graph of the relationships/rivalries between wrestlers
adj = {}
left = 0
right = 1
for n in range(0, num_of_wrestlers):
	adj[n] = []
for r in range(0, len(rivalry_lists)):
	if rivalry_lists[r][left] in babyfaces:									# if left wrestler is found in babyfaces list...
		if rivalry_lists[r][right] in heels or rivalry_lists[r][right] not in babyfaces:			# if right wrestler is found in heels list, or he is not in babyfaces list... they are a heel
			if rivalry_lists[r][right] not in heels:						# if wrestler wasn't in heel list yet, add to heel list.
				heels.append(rivalry_lists[r][right])
			adj[wrestler_dict[rivalry_lists[r][left]]].append([wrestler_dict[rivalry_lists[r][right]], 1]) 		# add entry to adjacency list for the left wrestler's index number to create vertex, and edge = 1
	elif rivalry_lists[r][left] in heels:
		if rivalry_lists[r][right] in heels:																	# both left and right wrestlers are in heels, we will add these to adjacency list, with edge=2
			adj[wrestler_dict[rivalry_lists[r][left]]].append([wrestler_dict[rivalry_lists[r][right]], 2])
		elif rivalry_lists[r][right] in babyfaces:																# if left is a heel, and the right is already in babyfaces, just add this vertex and node to adjacency list
			adj[wrestler_dict[rivalry_lists[r][left]]].append([wrestler_dict[rivalry_lists[r][right]], 1])
		elif rivalry_lists[r][right] not in babyfaces:														# lastly, if left is in heels, here we will add the right wrestler into babyfaces
			babyfaces.append(rivalry_lists[r][right])
			adj[wrestler_dict[rivalry_lists[r][left]]].append([wrestler_dict[rivalry_lists[r][right]], 1])
	else:																	# else, if the left wrestler is not in babyfaces or heels... we check whether the right wrestler is in babyfaces or heels. if neither are in any lists yet, we'll set the left wrestler to babyfaces and the right wrestler to heels. this will probably start a new, disconnected graph. 
		if rivalry_lists[r][right] in babyfaces:
			heels.append(rivalry_lists[r][left])
			adj[wrestler_dict[rivalry_lists[r][left]]].append([wrestler_dict[rivalry_lists[r][right]], 1])
		elif rivalry_lists[r][right] in heels:
			babyfaces.append(rivalry_lists[r][left])
			adj[wrestler_dict[rivalry_lists[r][left]]].append([wrestler_dict[rivalry_lists[r][right]], 1])
		else:																# if neither of the left or right has a team, assign the left to the babyfaces, and right to heels
			babyfaces.append(rivalry_lists[r][left])
			heels.append(rivalry_lists[r][right])
			adj[wrestler_dict[rivalry_lists[r][left]]].append([wrestler_dict[rivalry_lists[r][right]], 1])


# check the adjacency list as a graph and to determine if it meets the requirements or not.
# Requirements: all rivalries must be between wrestlers of opposing teams, we can confirm this by checking the edge lengths and confirming that all equal 2. This fails if we find an edge of 2.
def results(adjacency_list, b, h):
	for each_vertex in range(0, len(adj)):
		for each_list in adj[each_vertex]:
			if each_list[1] == 2:				# if we find an edge=2, then we have a rivalry between two teammates and this fails
				print("No, this is impossible.")
				return
	print "Yes"
	print "Babyfaces: ", ' '.join(b)
	print "Heels:  ", ' '.join(h)



results(adj, babyfaces, heels)