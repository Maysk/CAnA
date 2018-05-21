
from math import floor, ceil
import time

############################################
				#Questão 01#				
############################################
def question01_a(value):
	if(value >= 5):
		termo1 = question01_a(floor(value/2))
		termo2 = question01_a(floor(value/2) + 1)
		termo3 = question01_a(floor(value/2) + 2)

		return termo1 + termo2 + termo3 + value

	else:
		return 0


def question01_b(value):
	solutions_vector = 	[0 for i in range(value+1)]
	for i in range(5, value+1):
		solutions_vector[i] = 	( 
								solutions_vector[floor(i/2)]
								+ solutions_vector[floor(i/2) + 1]
								+ solutions_vector[floor(i/2) + 2]
								+ i
								)
	return solutions_vector[value]


def question01_c(value, solutions_vector):
	if (solutions_vector is None):
		solutions_vector = 	[0 for i in range(0, 5)] + [None for i in range(5, value+1)]
		result = question01_c(value, solutions_vector)
		return solutions_vector[value]
	else:
		if(value < 5 or solutions_vector[value] is not None):
			return solutions_vector[value]
		else:
			termo1 = question01_c(floor(value/2), solutions_vector)
			termo2 = question01_c(floor(value/2) + 1, solutions_vector)
			termo3 = question01_c(floor(value/2) + 2, solutions_vector)
			solutions_vector[value] = termo1 + termo2 + termo3 + value
			return solutions_vector[value]



############################################
				#Questão 02#				
############################################

def question02(sequence_s):
	size = len(sequence_s)
	solutions_vector = [0] * (size + 1)
	end_idx_max_sum = -1
	max_sum = 0
	for i in range(1, size+1):
		if(solutions_vector[i] < solutions_vector[i-1] + sequence_s[i-1]):
			solutions_vector[i] = solutions_vector[i-1] + sequence_s[i-1]
		
		if(solutions_vector[i] > max_sum):
			max_sum = solutions_vector[i]
			end_idx_max_sum = i

	if (i == -1) :
		print("Vazio")
	
	else:
		begin_idx_max_sum = end_idx_max_sum
		while (begin_idx_max_sum >=0 and solutions_vector[begin_idx_max_sum] > 0):
			begin_idx_max_sum -= 1

		print("Sequencia de soma maxima: ", sequence_s[begin_idx_max_sum:end_idx_max_sum])





############################################
				#Questão 03#				
############################################

def is_cubic_or_square(number):
	x = abs(number)
	v1 = x ** (1/3)
	v2 = x ** (1/2)
	return  v1 == ceil(v1) or v2 == ceil(v2) 

def question03(number):
	number_str = str(number)
	number_size = len(number_str)
	solutions_vector = [0] * number_size
	R_vector = [-1] * number_size
	
	i = 1
	j = 0
	
	while(i <= number_size):
		j = i 
		while(j>0):
			n = int(number_str[j-1:i])
			if(is_cubic_or_square(n) and solutions_vector[i-1] < solutions_vector[j-1] + 1):
				solutions_vector[i-1] = solutions_vector[j-1] + 1
				R_vector[i-1] = j-1
			j = j - 1
		i = i + 1 


	return [solutions_vector[-1] != 0, solutions_vector, R_vector]


def print_question03(number_str, R_vector, end_i):
	
	if(end_i>=0):
		print_question03(number_str, R_vector, R_vector[end_i]-1)
		print(number_str[R_vector[end_i]: end_i+1], end=" | ")



############################################
				#Questão 03#				
############################################


	




############################################
				#EditDistance#				
############################################
def new_matrix(number_of_lines, number_of_columns):
	return [[None]*number_of_columns for i in range(number_of_lines)]
def edit_distance(word_a,word_b, m, n):
	matrix_e = new_matrix(m+1, n+1)
	matrix_r = new_matrix(m+1, n+1)

	for column_idx in range(n+1):
		matrix_e[0][column_idx] = column_idx
		matrix_r[0][column_idx] = "left"
	for line_idx in range(m+1):
		matrix_e[line_idx][0] = line_idx
		matrix_r[line_idx][0] = "up"

	for line_idx in range(1, m+1):
		for column_idx in range(1, n+1):
			if(word_a[line_idx - 1] == word_b[column_idx -1]):
				matrix_e[line_idx][column_idx] = matrix_e[line_idx - 1][column_idx - 1]
				matrix_r[line_idx][column_idx] = "diagonal"

			elif( matrix_e[line_idx - 1][column_idx - 1] <= min(matrix_e[line_idx - 1 ][column_idx], matrix_e[line_idx][column_idx-1]) ): 
				matrix_e[line_idx][column_idx] = 1 + matrix_e[line_idx - 1][column_idx - 1]
				matrix_r[line_idx][column_idx] = "diagonal"

			elif(matrix_e[line_idx - 1][column_idx] <= matrix_e[line_idx][column_idx - 1]):
				matrix_e[line_idx][column_idx] = 1 + matrix_e[line_idx - 1][column_idx]
				matrix_r[line_idx][column_idx] = "up"
			else:
				matrix_e[line_idx][column_idx] = 1 + matrix_e[line_idx][column_idx - 1]
				matrix_r[line_idx][column_idx] = "left"

	return [matrix_e[m][n], matrix_r]

def track_edit_distance(word_a, word_b, i, j, matrix_r):
	if(i == 0 and j == 0):
		return

	if(matrix_r[i][j] == "diagonal"):
		track_edit_distance(word_a, word_b, i-1, j-1, matrix_r)
		print("Edit: ", word_a[i-1], word_b[j-1])
	elif(matrix_r[i][j] == "up"):
		track_edit_distance(word_a, word_b, i-1, j,matrix_r)
		print("Edit: ", word_a[i-1], "_")
	else:
		track_edit_distance(word_a, word_b, i, j-1, matrix_r)
		print("Edit: ", "_", word_b[j-1])


############################################
				#LCS#				
############################################
def lcs(word_a, word_b, m, n):
	matrix_e = new_matrix(m + 1, n + 1)
	matrix_r = new_matrix(m + 1, n + 1)

	for column_idx in range(n + 1):
		matrix_e[0][column_idx] = 0

	for line_idx in range(m + 1):
		matrix_e[line_idx][0] = 0
	
	for line_idx in range(1, m + 1):
		for column_idx in range(1, n + 1):
			if(word_a[line_idx - 1] == word_b[column_idx - 1 ]):
				matrix_e[line_idx][column_idx] = 1 + matrix_e[line_idx - 1][column_idx - 1]
				matrix_r[line_idx][column_idx] = "diagonal"
			elif(matrix_e[line_idx - 1][column_idx] >= matrix_e[line_idx][column_idx -1]):
				matrix_e[line_idx][column_idx] = matrix_e[line_idx - 1][column_idx]
				matrix_r[line_idx][column_idx] = "up"
			else:
				matrix_e[line_idx][column_idx] = matrix_e[line_idx][column_idx-1]
				matrix_r[line_idx][column_idx] = "left"
	return [matrix_e[m][n], matrix_r]

def track_lcs(word_a, i, j, matrix_r):
	if (i == 0 or j == 0):
		return
	if(matrix_r[i][j] == "diagonal"):
		track_lcs(word_a, i-1, j-1, matrix_r)
		print(word_a[i-1])
	elif(matrix_r[i][j] == "up"):
		track_lcs(word_a, i-1, j, matrix_r)
	else:
		track_lcs(word_a, i, j-1, matrix_r)

############################################
				#Knapsack#				
############################################
def new_vector(length):
	return [None] * length

def knapsack_with_repetition(item_weights, item_values, n, capacity):
	vector_v = new_vector(capacity + 1)
	vector_r = new_vector(capacity + 1)
	vector_v[0] = 0
	vector_r[0] = -1

	for i in range(1, capacity+1):
		vector_v[i] = 0
		vector_r[i] = -1
		for j in range(n):
			if(item_weights[j] <= i and vector_v[i] < item_values[j] + vector_v[i - item_weights[j]]):
				vector_v[i] = item_values[j] + vector_v[i - item_weights[j]]
				vector_r[i] = j

	return [vector_v[capacity], vector_r]

def track_knapsack_with_repetition(item_weights, item_values, capacity, vector_r):
	i = vector_r[capacity]
	if i >= 0:
		print("Item: ", i, "; Weight: ", item_weights[i], "; Value: ", item_values[i], "; Remaining Capacity: ", capacity - item_weights[i])
		track_knapsack_with_repetition(item_weights, item_values, capacity - item_weights[i], vector_r)


def knapsack_without_repetition(item_weights, item_values, n, capacity):
	matrix_e = new_matrix(capacity + 1 , n + 1)
	matrix_r = new_matrix(capacity + 1 , n + 1)

	for line_idx in range(capacity+1):
		matrix_e[line_idx][0] = 0

	for column_idx in range(n+1):
		matrix_e[0][column_idx] = 0

	for line_idx in range(1, capacity + 1):
		for column_idx in range(1, n + 1):
			matrix_e[line_idx][column_idx] = matrix_e[line_idx][column_idx-1]
			matrix_r[line_idx][column_idx] = 0

			if(item_weights[column_idx - 1] <= line_idx and matrix_e[line_idx][column_idx] < matrix_e[line_idx - item_weights[column_idx-1]][column_idx-1] + item_values[column_idx-1] ):
				matrix_e[line_idx][column_idx] = matrix_e[line_idx - item_weights[column_idx-1]][column_idx-1]  + item_values[column_idx-1]
				matrix_r[line_idx][column_idx] = 1
	return [matrix_e[capacity][n], matrix_r]

def track_knapsack_without_repetition(item_weights, item_values, capacity, n, matrix_r):
	if (capacity <= 0 or n <= 0):
		return
	if(matrix_r[capacity][n] == 0):
		track_knapsack_without_repetition(item_weights, item_values, capacity, n - 1, matrix_r)
	else:
		print("Item: ", n-1, "; Weight: ", item_weights[n-1], "; Value: ", item_values[n-1], "; Remaining Capacity: ", capacity - item_weights[n-1])
		track_knapsack_without_repetition(item_weights, item_values, capacity - item_weights[n-1], n - 1, matrix_r)


############################################
				#Testes#				
############################################




question_being_tested = 'knapsack_with_repetition'	

if(question_being_tested == '1'):
	##Teste Q1
	begin_t = 0
	end_t = 0
	elapsed_time = 0
	chosen_N = 10000000


	begin_t = time.perf_counter()
	result = question01_a(chosen_N)
	end_t = time.perf_counter()
	elapsed_time = end_t - begin_t

	print("Question01_a: " + str(elapsed_time))
	print("Question01_a: " + str(result))

	begin_t = time.perf_counter()
	result = question01_b(chosen_N)
	end_t = time.perf_counter()
	elapsed_time = end_t - begin_t

	print("Question01_b: " + str(elapsed_time))
	print("Question01_b: " + str(result))

	begin_t = time.perf_counter()
	result = question01_c(chosen_N, None)
	end_t = time.perf_counter()
	elapsed_time = end_t - begin_t

	print("Question01_c: " + str(elapsed_time))
	print("Question01_c: " + str(result))

elif(question_being_tested == '2'):
	sequence = [5, 15, -30, 10, -5, 40, 10]
	question02(sequence)

elif(question_being_tested == '3'):
	number_being_tested = 125271448164
	number_being_tested_str = str(number_being_tested)
	result = question03(number_being_tested)
	if (result[0]):
		print("It's possible to break as cubics or squares numbers:")
		print_question03(number_being_tested_str, result[2], len(number_being_tested_str)-1)
		print("\n\n")
	else:
		print("OH NOO! It's not possible to break as cubics or squares numbers.")

elif(question_being_tested == '4'):
	pass
elif(question_being_tested == '5'):	
	pass
elif(question_being_tested == '6'):
	pass
elif(question_being_tested == 'edit_distance'):
	word_1 = ''
	word_2 = 'bana'
	result = edit_distance(word_1, word_2, len(word_1), len(word_2))
	number_of_editions = result[0]
	print("Number of Editions: ", number_of_editions)
	track_edit_distance(word_1, word_2, len(word_1), len(word_2), result[1])
elif(question_being_tested == 'lcs'):
	word_1 = 'bonan'
	word_2 = 'bana'
	result = lcs(word_1, word_2, len(word_1), len(word_2))
	max_lcs = result[0]
	print("Max LCSs: ", max_lcs)
	track_lcs(word_1, len(word_1), len(word_2), result[1])


elif(question_being_tested == 'knapsack_with_repetition'):
	item_weights = [3,2,4,5]
	item_values = [40,10,50,70]
	number_of_items = 4
	capacity = 5
	result = knapsack_with_repetition(item_weights, item_values, number_of_items, capacity)
	print("Max Value: ", result[0])
	track_knapsack_with_repetition(item_weights, item_values, capacity, result[1])

elif(question_being_tested == 'knapsack_without_repetition'):
	item_weights = [3,2,4,5]
	item_values = [40,10,50,70]
	number_of_items = 4
	capacity = 20
	result = knapsack_without_repetition(item_weights, item_values, number_of_items, capacity)
	print("Max Value: ", result[0])
	track_knapsack_without_repetition(item_weights, item_values, capacity, number_of_items, result[1])