# Before Leetcode

[Inspiration](https://blog.faangshui.com/p/before-leetcode)

Tracking checkboxes can be used by forking this repository and marking an X inside the appropriate brackets. Here is an example:
- [ ] Unsolved
- [X] Solved

## 1. Array Indexing
Understanding how to navigate arrays is essential. Here are ten exercises, sorted in increasing difficulty, that build upon each other:

- [X] Iterate Over an Array Write a function that prints each element in an array in order from the first to the last.

- [X] Iterate Over an Array in Reverse Modify the previous function to print the elements in reverse order, from the last to the first.

- [X] Fetch Every Second Element Write a function that accesses every other element in the array, starting from the first element.

- [X] Find the Index of a Target Element

- [X] Write a function that searches for a specific element in an array and returns its index. If the element is not found, return -1.

- [ ] Find the First Prime Number in an Array **REPEAT**


### Traverse a Two-Dimensional Array

- [X] Write a function to print all elements of a 2D array (matrix), row by row.

- [X] Traverse the Main Diagonal of a Matrix

- [ ] Traverse the Perimeter of a Matrix

- [ ] Traverse Elements in Spiral Order

- [X] Traverse the Lower Triangle of a Matrix

- [X] Print the elements below and including the main diagonal of a square matrix.


## 2. Accumulator Variables
Learn how to keep track of values during iteration. These exercises build upon each other in complexity:

- [X] Calculate the Sum of an Array. Write a function that calculates the sum of all elements in an array by accumulating the total as you iterate.

- [X] Find the Minimum and Maximum Elements. Find the smallest and largest numbers in an array by updating minimum and maximum variables during iteration.

- [X] Find the Indices of the Min and Max Elements In addition to finding the min and max values, keep track of their positions (indices) in the array.

- [X] Find the Two Smallest/Largest Elements Without Sorting Modify your approach to keep track of the two smallest and two largest elements during a single pass through the array.

- [X] Count Occurrences of a Specific Element. Count how many times a given element appears in the array by incrementing a counter whenever you encounter it.

- [X] Count Occurrences of All Elements. Use a dictionary or map to count the number of times each unique element appears in the array during a single iteration.

- [X] Find the Two Most Frequent Elements. Find the two elements that appear the most number of times in an array.

### Compute Prefix Sums

- [X] Create an array where each element at index i is the sum of all elements up to that index in the original array. We call this array prefix sums array.

- [X] Find the Sum of Elements in a Given Range.Given a range (start and end indices), write a function that calculates the sum of elements within that range by iterating from the start to the end index and accumulating the sum.

- [ ] Efficient Range Sum Queries Using Prefix Sums
After computing the prefix sums array, answer multiple range sum queries efficiently:
Instead of summing elements for each query, use the prefix sums array to compute the sum of elements between indices i and j in constant time.
Hint: The sum from index i to j can be calculated as prefix_sum[j] - prefix_sum[i - 1]. This method requires understanding how to manipulate indices and handle edge cases when i is 0.

## 3. Recursion
Get comfortable with functions that call themselves with these ten exercises:

Calculate the nth Fibonacci Number

Write a recursive function to find the nth Fibonacci number, where each number is the sum of the two preceding ones.

Sum of an Array Using Recursion

Find the sum of all elements in an array by recursively summing the first element and the sum of the rest of the array.

Find the Minimum Element in an Array Using Recursion

Find the smallest element in an array without using loops by comparing the first element with the minimum of the rest of the array.

Reverse a String Using Recursion

Reverse a given string by recursively swapping characters from the ends towards the center.

Check if a String is a Palindrome Using Recursion

Determine if a string reads the same backward as forward by comparing characters from the outside in.

Generate All Permutations of a String

Recursively generate all permutations of the characters in a string by swapping characters.

Generate All Subsets of a Set

Generate all possible subsets (the power set) of a set of numbers by including or excluding each element recursively.

Compute the Sum of Digits of a Number

Given an integer, write a recursive function to compute the sum of its digits.

Compute the Power of a Number

Write a recursive function to compute x raised to the power n (i.e., compute x^n), where n is a non-negative integer.

Count the Number of Occurrences of a Character in a String Using Recursion

Write a recursive function to count how many times a specific character appears in a string.
