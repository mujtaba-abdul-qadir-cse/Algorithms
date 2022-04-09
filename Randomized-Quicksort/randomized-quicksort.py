from random import randint
def randomizedpartition(A, p, r):
	import random
	i = randint(p, r)
	temp = A[r]
	A[r] = A[i]
	A[i] = temp
	return partition(A, p, r)

def partition(A, p, r):
	x = A[r]
	i = p-1
	for j in range(p, r):
		if A[j] <=  x:
			i = i + 1
			temp = A[i]
			A[i] = A[j]
			A[j] = temp
			
	temp = A[i+1]
	A[i+1] = A[r]
	A[r] = temp
	
	return i+1
	
def randomizedquicksort(A, p, r):
	if p < r:
		q=randomizedpartition(A, p, r)
		randomizedquicksort(A, p, q-1)
		randomizedquicksort(A, q+1, r)
		
		
A = [3, 1, 4, 2, 8, 5, 7]
n = len(A)

randomizedquicksort(A, 0, n-1)

for i in A:
	print(i)
