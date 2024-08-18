/*

is more predictable in terms of performance and is stable,.
It’s particularly useful when stability is a requirement or when working with linked lists.

Algorithm Type: Comparison-based, divide-and-conquer.
Approach:

    Dividing: Merge Sort divides the array into two halves until each sub-array contains a single element.
    Merging: It then merges these sub-arrays to produce sorted arrays.

Time Complexity:

    All Cases: O(n log n) (Merge Sort has consistent performance regardless of the input data)

Space Complexity: O(n) due to the need for temporary arrays used during merging.
Stability: Stable. Equal elements retain their relative order.
Not In-Place: Merge Sort requires additional space proportional to the size of the array.

Applications:
Data Analysis: Applied in sorting large-scale data for statistical analysis and data processing tasks.
Computational Geometry: Used in algorithms for tasks like finding intersections and ordering geometric objects.
Multithreaded Sorting: Beneficial for parallel processing and multithreaded environments due to its divide-and-conquer 
approach that can be efficiently parallelized.

*/

public class MergeSort {

    // Main function to sort an array using merge sort
    public static void mergeSort(int[] array) {
        if (array.length < 2) {
            return;
        }
        int mid = array.length / 2;
        int[] left = new int[mid];
        int[] right = new int[array.length - mid];

        // Copy data to temporary arrays
        System.arraycopy(array, 0, left, 0, mid);
        System.arraycopy(array, mid, right, 0, right.length);

        // Recursively sort both halves
        mergeSort(left);
        mergeSort(right);

        // Merge sorted halves
        merge(array, left, right);
    }

    // Merge two sorted arrays into a single sorted array
    private static void merge(int[] array, int[] left, int[] right) {
        int leftIndex = 0, rightIndex = 0, arrayIndex = 0;

        // Merge the arrays while both halves have elements
        while (leftIndex < left.length && rightIndex < right.length) {
            if (left[leftIndex] <= right[rightIndex]) {
                array[arrayIndex++] = left[leftIndex++];
            } else {
                array[arrayIndex++] = right[rightIndex++];
            }
        }

        // Copy remaining elements of left half, if any
        while (leftIndex < left.length) {
            array[arrayIndex++] = left[leftIndex++];
        }

        // Copy remaining elements of right half, if any
        while (rightIndex < right.length) {
            array[arrayIndex++] = right[rightIndex++];
        }
    }

    // Main method to test merge sort
    public static void main(String[] args) {
        int[] array = {5, 2, 1, 4};
        System.out.println("Original array:");
        for (int num : array) {
            System.out.print(num + " ");
        }

        mergeSort(array);

        System.out.println("\nSorted array:");
        for (int num : array) {
            System.out.print(num + " ");
        }
    }
}
