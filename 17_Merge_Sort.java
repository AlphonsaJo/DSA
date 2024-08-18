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
