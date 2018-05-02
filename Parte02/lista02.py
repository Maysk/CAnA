
from math import floor
import time
#The complexity is O(3 ^ log n)
def question01_a(value):
	if(value >= 5):
		termo1 = question01_a(floor(value/2))
		termo2 = question01_a(floor(value/2) + 1)
		termo3 = question01_a(floor(value/2) + 2)

		return termo1 + termo2 + termo3 + value**2

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
								+ i**2
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
			solutions_vector[value] = termo1 + termo2 + termo3 + value**2
			return solutions_vector[value]


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