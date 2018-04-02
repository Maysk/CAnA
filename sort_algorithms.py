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



def combina_asc(vetor, p, q, r):
	l1 = vetor[p:q+1]
	l2 = vetor[q+1:r+1]
	i = 0
	j = 0
	k = p
	while (k<=r) :
		if(p + i > q):
			vetor[k] = l2[j]
			j = j + 1
		elif(q + 1 + j > r):
			vetor[k] = l1[i]
			i = i + 1
		elif(l1[i] < l2[j]):			
			vetor[k] = l1[i]
			i = i + 1
		else:
			vetor[k] = l2[j]
			j = j + 1

		k = k + 1

def merge_sort_asc(vetor, p, r):
	if(p == r):
		return [vetor[p]]
	else:
		q = floor((p + r)/2)
		merge_sort_asc(vetor, p, q)
		merge_sort_asc(vetor, q+1, r)
		combina_asc(vetor, p, q, r)


def combina_desc(vetor, p, q, r):
	l1 = vetor[p:q+1]
	l2 = vetor[q+1:r+1]
	i = 0
	j = 0
	k = p
	while (k<=r) :
		if(p + i > q):
			vetor[k] = l2[j]
			j = j + 1
		elif(q + 1 + j > r):
			vetor[k] = l1[i]
			i = i + 1
		elif(l1[i] > l2[j]):			
			vetor[k] = l1[i]
			i = i + 1
		else:
			vetor[k] = l2[j]
			j = j + 1

		k = k + 1


def merge_sort_desc(vetor, p, r):
	if(p == r):
		return [vetor[p]]
	else:
		q = floor((p + r)/2)
		merge_sort_desc(vetor, p, q)
		merge_sort_desc(vetor, q+1, r)
		combina_desc(vetor, p, q, r)


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



#TESTE

v = [5, 3, 4, 2, 1]
print("Inicial:", v)
inicial_idx = 1
final_idx = 3

v_copy = v.copy()
insertion_sort_asc(v_copy, inicial_idx, final_idx)
print("Insertion Sort Asc:", v_copy)

v_copy = v.copy()
insertion_sort_desc(v_copy, inicial_idx, final_idx)
print("Insertion Sort Desc:", v_copy)

v_copy = v.copy()
merge_sort_asc(v_copy, inicial_idx, final_idx)
print("Merge Sort Asc:", v_copy)

v_copy = v.copy()
merge_sort_desc(v_copy, inicial_idx, final_idx)
print("Merge Sort Desc:", v_copy)

v_copy = v.copy()
heap_sort_asc(v_copy, inicial_idx, final_idx)
print("Heap Sort Asc:", v_copy)
