# [Day - 1](day-1-sorting/)
## Sorting Techniques
### [Merge Sort](day-1-sorting/merge-sort.py) 
- A divide and conquer sorting approach which has a time-complexity of O(n log(n)).
- A stable sort - if two values are equal, the relative order prior to sorting will be maintained.
- Worst case time complexity of merge sort is  O (n log(n)).
- Space complexity of merge sort is  O (n).
- Merge sort scales well with large amounts of data.
---
#### [Quick Sort](day-1-sorting/quick-sort.py) 
- A divide and conquer sorting approach which has a time-complexity of O(n log(n)).
- It is also called partition-exchange sort.
- Unlike merge sort where the main work happens while merging the subarrays, here in quick sort most of the work happens during the splitting process.
- Worst case time complexity of quick sort is  O (n^2).
- Average time complexity(Big-theta) of quick sort is O(n log n)
- Space complexity of quick sort is  O (n log n).
- Quick sort is an in-place sorting algorithm.
- The default implementation of quick sort is not stable. However any sorting algorithm can be made stable by considering indexes as comparison parameter. 
---
#### [Insertion Sort](day-1-sorting/insertion-sort.py) 
- Insertion sort is a simple sorting algorithm that works the way we sort playing cards in our hands.
- Incremental approach.
- Insertion sort takes maximum time to sort if elements are sorted in reverse order. And it takes minimum time (Order of n) when elements are already sorted.
- Worst case time complexity of insertion sort is  O (n^2).
- Space complexity of insertion sort is  O (1).
- Insertion sort is an in-place sorting algorithm.
- The default implementation of insertion sort is stable.
- Insertion sort is used when number of elements is small. It can also be useful when input array is almost sorted, only few elements are misplaced in complete big array.
---