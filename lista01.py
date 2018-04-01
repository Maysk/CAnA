from math import floor
from sort_algorithms import insertion_sort_asc, heap_sort_asc


#Questão 5

def conta(vetor, p, r, elem):
	i = p
	contador = 0
	while (i<=r):
		if(vetor[i] == elem):
			contador = contador + 1
		i = i +1
	return contador

def questao05(vetor, p, r):
	if(p==r):
		return vetor[r]
	else:
		q = floor((p+r)/2)
		m1 = questao05(vetor, p, q)
		m2 = questao05(vetor, q+1, r)

		c_m1 = 0
		c_m2 = 0

		if(m1 != None):
			c_m1 = conta(vetor, p, r, m1)
		if(m2 != None):
			c_m2 = conta(vetor, p, r, m2)

		if(c_m1 > (r - p + 1)/2):
			return m1

		if(c_m2 > (r - p + 1)/2):
			return m2

		return None


def questao06(vetor1, vetor2, p1, r1, p2, r2):
	if ( r1-p1 <= 1 and r2-p2 <= 1 ):
		n = r1 - p1 +1 + r2 - p2 + 1
		aux = vetor1[p1:r1+1] + vetor2[p2:r2+1]
		insertion_sort_asc(aux, 0, n-1)
		return aux[floor(n/2)]

	else:
		q1 = floor((p1+r1)/2)
		q2 = floor((p2+r2)/2)

		med1 = vetor1[q1]
		med2 = vetor2[q2]
		print(p1, q1, r1, p2, q2, r2)
		print(med1, med2)
		if(med1 == med2):
			return med1
		elif(med1 < med2):
			return questao06(vetor1, vetor2, q1, r1, p2, q2)
		else:
			return questao06(vetor1, vetor2, p1, q1, q2, r2)



def busca_binaria(vetor, value, p, r):
	q = floor((p+r)/2)
	if(p>r):
		return None
	if(vetor[q] == value):
		return q	
	elif(vetor[q] < value):
		return busca_binaria(vetor, value, q+1, r)
	else:
		return busca_binaria(vetor, value, p, q-1)

def questao07(vetor, p, r, x):
	heap_sort_asc(vetor, p, r)
	i = p
	j = None
	while(i <= r and j == None):
		j = busca_binaria(vetor, x - vetor[i], p, r)
		if(j == i):
			j = None
		
		if(j == None):
			i = i + 1
	if(j != None):
		print("Indices", i, j, vetor[i], vetor[j])
	else:
		print("Não tem")




v = [1,1,1,2,2]
z = questao05(v, 2, 4)
print("Majoriatario: ", z)

v1 = [1, 2, 3, 3]
v2 = [4, 5, 6]
med = questao06(v1, v2, 0, len(v1)-1, 0, len(v2)-1)
print("Mediana: ", med)

v3 = [4, 3, 5, 6, 1, 7, 2, 3]
questao07(v3, 0, len(v3) - 1, 6)