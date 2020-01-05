# 21-days-of-algorithms
I set the challenge for myself to implement as many algorithms as I can in 21 days.

## [Day - 1](day-1-sorting/)
### Sorting Techniques
#### [Merge Sort](day-1-sorting/merge-sort.py) 
- A divide and conquer sorting approach which has a time-complexity of O(n log(n)).
- A stable sort - if two values are equal, the relative order prior to sorting will be maintained.
- Worst case time complexity of merge sort is  O (n log(n)).
- Space complexity of merge sort is  O (n).
- Merge sort scales well with large amounts of data.

#### [Quick Sort](day-1-sorting/quick-sort.py) 
- A divide and conquer sorting approach which has a time-complexity of O(n log(n)).
- It is also called partition-exchange sort.
- Unlike merge sort where the main work happens while merging the subarrays, here in quick sort most of the work happens during the splitting process.
- Worst case time complexity of quick sort is  O (n^2).
- Average time complexity(Big-theta) of quick sort is O(n log n)
- Space complexity of quick sort is  O (n log n).
- Quick sort is an in-place sorting algorithm.
- The default implementation of quick sort is not stable. However any sorting algorithm can be made stable by considering indexes as comparison parameter. 

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

## [Day - 2](day-2-graph/)
### Graph
#### [Breadth First Search (BFS)](day-2-graph/graph-bfs.py) 
- Unlike trees, graphs may contain cycles, so we may come to the same node again. To avoid processing a node more than once, we use a boolean visited array in this implementation.

#### [Depth First Search (DFS)](day-2-graph/graph-dfs.py) 
- Unlike trees, graphs may contain cycles, so we may come to the same node again. To avoid processing a node more than once, we use a boolean visited array in this implementation.

#### [Dijkstra's Algorithm](day-2-graph/graph-dijkstra.py) 
- Shortest Path from source to all vertices.
- Algorithm for Dijkstra's:
>1) Create a set sptSet (shortest path tree set) that keeps track of vertices included in shortest path tree, i.e., whose minimum distance from source is calculated and finalized. Initially, this set is empty.
>2) Assign a distance value to all vertices in the input graph. Initialize all distance values as INFINITE. Assign distance value as 0 for the source vertex so that it is picked first.
>3) While sptSet doesn’t include all vertices
>	a) Pick a vertex u which is not there in sptSet and has minimum distance value.
>	b) Include u to sptSet.
>	c) Update distance value of all adjacent vertices of u. To update the distance values, iterate through all adjacent vertices. For every adjacent vertex v, if sum of distance value of u (from source) and weight of edge u-v, is less than the distance value of v, then update the distance value of v.
---

## [Day - 3](/)
### Operations on LinkedList
#### [Insertion in LinkedList](day-3-linkedlist/ll-insertion.py) 
- Given linked list,<img src="day-3-linkedlist/images/ll-insertion1.png" align="center" style="height: 64px"/>
- we have to insert 9 after 6. <img src="day-3-linkedlist/images/ll-insertion2.png" align="center" style="height: 64px"/>

#### [Deletion in LinkedList](day-3-linkedlist/ll-deletion.py) 
- 

---