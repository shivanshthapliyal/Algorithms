# A divide and conquer sorting approach which has a time-complexity of O(n log(n)).
# A stable sort - if two values are equal, the relative order prior to sorting will be maintained
# Space complexity of merge sort is  O (n).
# Merge sort scales well with large amounts of data.


def merge(left_arr,right_arr):
	output=[]

	#adding to output till elements are found
	while left_arr and right_arr:
		left_arr_item = left_arr[0]
		right_arr_item = right_arr[0]

		if left_arr_item < right_arr_item:
			output.append(left_arr_item)
			left_arr.pop(0)
		else:
			output.append(right_arr_item)
			right_arr.pop(0)


	while left_arr:
		output.append(left_arr[0])
		left_arr.pop(0)

	while right_arr:
		output.append(right_arr[0])
		right_arr.pop(0)

	return output


def merge_sort(arr):
	arr_length = len(arr)

	#base case
	if arr_length<2:
		return arr

	left_arr = arr[:arr_length//2]
	right_arr = arr[arr_length//2:]
	# // forces division

	# we then sort the list recursively
	left_arr = merge_sort(left_arr)
	right_arr = merge_sort(right_arr)
	
	return merge(left_arr,right_arr)



array = [34,12,2,41,53,127]

sortedarray = merge_sort(array)

print(sortedarray)