public class QuickSort {

    // Function to perform quicksort on an array
    public static void quicksort(int[] arr, int low, int high) {
        if (low < high) {
            // Partition the array and get the pivot index
            int pivotIndex = partition(arr, low, high);

            // Recursively sort the elements before and after partition
            quicksort(arr, low, pivotIndex - 1);
            quicksort(arr, pivotIndex + 1, high);
        }
    }

    // Function to partition the array around the pivot
    public static int partition(int[] arr, int low, int high) {
        // Choose the rightmost element as pivot
        int pivot = arr[high];

        int i = low - 1; // Index of the smaller element

        for (int j = low; j < high; j++) {
            // If the current element is smaller than or equal to the pivot
            if (arr[j] <= pivot) {
                i++;

                // Swap arr[i] and arr[j]
                int temp = arr[i];
                arr[i] = arr[j];
                arr[j] = temp;
            }
        }

        // Swap arr[i+1] with the pivot
        int temp = arr[i + 1];
        arr[i + 1] = arr[high];
        arr[high] = temp;

        // Return the index of the pivot
        return i + 1;
    }

    // Utility function to print the array
    public static void printArray(int[] arr) {
        for (int num : arr) {
            System.out.print(num + " ");
        }
        System.out.println();
    }

    public static void main(String[] args) {
        // Example array to sort
        int[] arr = {10, 7, 8, 9, 1, 5};
        int n = arr.length;

        // Print the original array
        System.out.println("Original array:");
        printArray(arr);

        // Perform quicksort on the array
        quicksort(arr, 0, n - 1);

        // Print the sorted array
        System.out.println("Sorted array:");
        printArray(arr);
    }
}

