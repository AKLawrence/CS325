# Amanda Lawrence
# 9/29/2018
# CS 325 - Analysis of Algorithms
# HW1 #4 - Insertion Sort



# Open our data.txt file and save each line of data as a list, within a list. We leave off the first value of each line in data.txt.
with open('data.txt', 'r') as f:
	lines = f.readlines()
	lines = [x.strip() for x in lines]
	data_temp = [x.split()[1:] for x in lines]
	data_sets = []
	for line in data_temp:
		data_sets.append([int(x) for x in line])
	#print(data_sets)




# Insertion sort algorithm adapted from pseudocode in Intro. to Algorithms textbook by: Cormen, Leiserson, Rivest, Stein; page 26.
def insertsort(A):
	#print("Running InsertSort function")
	for j in range(1, len(A), 1): 
		key = A[j]
		#print("Key is ", key)
		#insert A[j] into the sorted sequence A[1.. j-1]
		i = j-1
		while i > -1 and A[i] > key:
			A[i+1] = A[i]
			i = i-1
		A[i+1] = key
	return A

# For each line of data, in our lines list, call and run insertsort() and append that sorted list to a new array called isort_answers
x = 0
isort_answers = []
for x in range(x, len(data_sets), 1):
	isort_answers.append(insertsort(data_sets[x]))

y = 0
with open('insert.out', 'w') as f:
	for y in range(0, len(isort_answers), 1):
		output_txt = ' '.join([str(x) for x in isort_answers[y]])
		#f.write('%s\n' % ' '.join(isort_answers[y]))
		f.write(output_txt + '\n')
	