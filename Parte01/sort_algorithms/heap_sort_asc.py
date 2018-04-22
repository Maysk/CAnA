from math import floor
def parent(idx):
	return floor((idx-1)/2) 

def left(idx):
	return 2*idx + 1

def right(idx):
	return 2*idx + 2

def fix_below(vetor, idx, r):
	left_idx = left(idx) 
	right_idx = right(idx)

	if (left_idx <= r and vetor[left_idx] > vetor[idx]):
		bigger_idx = left_idx
	else:
		bigger_idx = idx

	if(right_idx <= r and vetor[right_idx] > vetor[bigger_idx]):
		bigger_idx = right_idx

	if(bigger_idx != idx):
		vetor[idx], vetor[bigger_idx] = vetor[bigger_idx], vetor[idx]
		fix_below(vetor, bigger_idx, r)


def build_max_heap(vetor, p, r):
	q = floor((p+r)/2)
	while(q >= 0):
		fix_below(vetor, q, r)
		q = q - 1;

def heap_sort_asc(vetor, p, r):
	build_max_heap(vetor, p, r)
	i = r
	while (i > p):
		vetor[p], vetor[i] = vetor[i], vetor[p]
		fix_below(vetor, p, i-1)
		i = i -1


