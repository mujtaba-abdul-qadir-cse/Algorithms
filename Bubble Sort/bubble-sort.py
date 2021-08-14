lst = [16, 3, 7, 25, 92, 8, 6, 127, 44]

print("Unsorted list:\n")
print(lst)

for i in range(0, len(lst)):
	for j in range(i+1, len(lst)):
		if lst[j] < lst[i]:
			temp = lst[j]
			lst[j] = lst[i]
			lst[i] = temp

print("\nSorted list:\n")
print(lst)
