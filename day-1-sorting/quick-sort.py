# Author => Shivansh Thapliyal
# Date	 => 1-Jan-2020

def quickSort(arr,low,high):
	if(low<high):
		pi = partition(arr,low,high)
		quickSort(arr,low,pi-1)
		quickSort(arr,pi+1,high)

	return arr

	
def partition(arr,low,high):
	p = arr[high]
	i = (low-1)
		
	for j in range(low,high):
		if(arr[j]<=p):
			i=i+1
			temp = arr[i]
			arr[i] = arr[j]
			arr[j] = temp
			
		
		temp = arr[i+1]
		arr[i+1] = arr[high]
		arr[high] = temp
		
		return (i+1)
	

arr =  [6, 4, 3, 1, 5, 2]
a=0
low=0
high=len(arr)-1
sortedarr = quickSort(arr,low,high);
		
		
# After Sorting 
ii=0;
while(ii<len(arr)):
	print(sortedarr[ii], " ")
	ii==ii+1
