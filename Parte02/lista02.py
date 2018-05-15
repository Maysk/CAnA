
from math import floor, ceil
import time

############################################
				#Questão 01#				
############################################
#The complexity is O(3 ^ log n)
def question01_a(value):
	if(value >= 5):
		termo1 = question01_a(floor(value/2))
		termo2 = question01_a(floor(value/2) + 1)
		termo3 = question01_a(floor(value/2) + 2)

		return termo1 + termo2 + termo3 + value

	else:
		return 0


#The Complexity is 
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
str(
)
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


question_being_tested = '3'	

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