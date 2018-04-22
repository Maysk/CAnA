from math import floor
def insertion_sort_asc(vetor, p, r):
	j = p + 1 
	while (j <= r):
		carta = vetor[j]
		i = j - 1
		while (i >= p and vetor[i] > carta):
			vetor[i+1] = vetor[i]
			i = i -1
		vetor[i + 1] = carta
		j = j + 1

def insertion_sort_desc(vetor, p, r):
	j = p + 1 
	while (j <= r):
		carta = vetor[j]
		i = j - 1
		while (i >= p and vetor[i] < carta):
			vetor[i+1] = vetor[i]
			i = i -1
		vetor[i + 1] = carta
		j = j + 1