# Author => Shivansh Thapliyal
# Date	 => 1-Jan-2020

def partition(arr,low,high):
	p = arr[high] #pivot element
	i = (low-1)
		
	for j in range(low,high):

		# if the current element is smaller than the pivot element
		if(arr[j]<p):	
			i=i+1  # then increment the index position of the smaller element
			arr[i],arr[j] = arr[j],arr[i] 
			
		
	arr[i+1],arr[high] = arr[high],arr[i+1] 
		
	return (i+1)

# Function that implement quicksort
def quickSort(arr,low,high):
	if(low<high):
		pi = partition(arr,low,high)

		# sorting elements after and before partition
		quickSort(arr,low,pi-1)
		quickSort(arr,pi+1,high)

	return arr



arr =  [6, 4, 3, 1, 5, 2]

low=0
high=len(arr)-1

sortedarr = quickSort(arr,low,high)
		
		
# After Sorting 
print(sortedarr)