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



def combina_asc(l1, l2):
	resultado = []
	while (len(l1) > 0 or len(l2) > 0) :
		if(len(l1) == 0):
			resultado.append(l2.pop(0))
		elif(len(l2) == 0):
			resultado.append(l1.pop(0))
		elif(l1[0] < l2[0]):			
			resultado.append(l1.pop(0))
		else:
			resultado.append(l2.pop(0))
	return resultado

def merge_sort_asc(vetor, p, r):
	if(p == r):
		return [vetor[p]]
	else:
		q = floor((p + r)/2)
		l1 = merge_sort_asc(vetor, p, q)
		l2 = merge_sort_asc(vetor, q+1, r)
		return combina_asc(l1, l2)


def combina_desc(l1, l2):
	resultado = []
	while (len(l1) > 0 or len(l2) > 0) :
		if(len(l1) == 0):
			resultado.append(l2.pop(0))
		elif(len(l2) == 0):
			resultado.append(l1.pop(0))
		elif(l1[0] > l2[0]):			
			resultado.append(l1.pop(0))
		else:
			resultado.append(l2.pop(0))
	return resultado

def merge_sort_desc(vetor, p, r):
	if(p == r):
		return [vetor[p]]
	else:
		q = floor((p + r)/2)
		l1 = merge_sort_desc(vetor, p, q)
		l2 = merge_sort_desc(vetor, q+1, r)
		return combina_desc(l1, l2)


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
inicial_idx = 0
final_idx = 4

v_copy = v.copy()
insertion_sort_asc(v_copy, inicial_idx, final_idx)
print("Insertion Sort Asc:", v_copy)

v_copy = v.copy()
insertion_sort_desc(v_copy, inicial_idx, final_idx)
print("Insertion Sort Desc:", v_copy)

v_copy = v.copy()
v_copy[inicial_idx:final_idx+1] = merge_sort_asc(v_copy, inicial_idx, final_idx)
print("Merge Sort Asc:", v_copy)

v_copy = v.copy()
v_copy[inicial_idx:final_idx+1] = merge_sort_desc(v_copy, inicial_idx, final_idx)
print("Merge Sort Desc:", v_copy)

v_copy = v.copy()
heap_sort_asc(v_copy, inicial_idx, final_idx)
print("Heap Sort Asc:", v_copy)
