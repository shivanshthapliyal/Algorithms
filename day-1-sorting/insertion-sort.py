def insertion_sort(arr):
	arr_length = len(arr)
	for i in range(1,arr_length):

		curr_val = arr[i]

		j = i-1

		while j>=0 and arr[j]>curr_val:
			arr[j+1] = arr[j]
			j -= 1

		arr[j+1] = curr_val

		print(arr,"\t Step ",i)

	return arr

array = [134,12,2,41,53,127]
print(array)
print()
sortedarray = insertion_sort(array)
print()
print(sortedarray)  