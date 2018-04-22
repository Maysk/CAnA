#Merge Sort
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