*This activity has been created as part of the 42 curriculum by llafforg, smlamali.*

# PUSH_SWAP

## Description
Push_Swap is an algorithm project that challenges to sort a list of integer using only two stacks
and a limited set of operations, with the smallest possible sequence of operations.
The goal of this project is to understand algorithmic complexity through the study of various sorting algorithms and their different time complexities

## Instructions

```txt
make
./push_swap [--simple | --medium | --complex] [--bench] <numbers>

#exemple
./push_swap --complex --bench $(shuf -i 0-100000 -n 100)
```

## Algrotihms

### **Simple Algorithm: Min Extract (O(n²))**
sort by finding the minimum element in stack A, rotates it to the top, and pushes it to stack B. Once all elements are in B (sorted in descending order), push them back to A.

It's an easy algorithm to implement and debug in a stack context, it works consistently with small numbers.

### **Medium Algorithm: Bucket Sort (O(n√n))**
sort by divides the input into (√n) buckets based on value ranges, pushes elements to stack B in bucket order, then pushes them back to A in sorted order.

We found it well suited for the project because it reduces rotations by grouping similar values together, that is ideal since we use a list of index to know in wich order we have to sort. It is also great at sorting 100-500 numbers within performance benchmarks requirements

### **Complex Algorithm: Radix (O(nlogn))**
Radix sort by replacing each number with its sorted index, then sorting bit by bit. For each pass, elements whose current bit is 0 go to B, elements with bit 1 rotate to the bottom of A. Then everything comes back from B to A. Repeat for each bit until sorted.
Radix sort fits Push Swap well because it doesn't need comparisons between elements — it just reads bits one by one. This maps naturally to the limited stack and operations.

## Resources
[Radix](https://www.geeksforgeeks.org/dsa/radix-sort/)

[bucket sort](https://fr.wikipedia.org/wiki/Tri_par_paquets)