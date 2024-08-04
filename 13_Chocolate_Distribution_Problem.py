'''
Problem:
Given an array of N integers where each value represents the number of chocolates in a packet. Each packet can have a variable number of chocolates.
There are m students, the task is to distribute chocolate packets such that: 
Each student gets one packet.
The difference between the number of chocolates in the packet with maximum chocolates and the packet with minimum chocolates given to the students is minimum.

Approach:
1) Sort the given array.
2) Initialize a variable to store the difference between the max packet and min packet with the value INT_MIN.
3) Specify the special cases (such as the number of students being more than the number of packets available / students = 0 / packets = 0)
4) Generate sub arrays from the list
5) Return the subarray that returns the least difference (diff) between the 0th and last index of the subarray.

Credits: GFG (https://www.geeksforgeeks.org/chocolate-distribution-problem/)
'''

def findMinDiff(arr, n, m):
 
    # if there are no chocolates or number
    # of students is 0
    if (m == 0 or n == 0):  #1
        return 0
 
    # Sort the given packets #2
    arr.sort()
 
    # Number of students cannot be more than #3
    # number of packets
    if (n < m):
        return -1
 
    # Largest number of chocolates #4
    min_diff = arr[n-1] - arr[0]
 
    # Find the subarray of size m such that
    # difference between last (maximum in case
    # of sorted) and first (minimum in case of
    # sorted) elements of subarray is minimum.
    for i in range(len(arr) - m + 1):
        min_diff = min(min_diff,  arr[i + m - 1] - arr[i]) #5
 
    return min_diff
 
 
# Driver Code
if __name__ == "__main__":            #6
    arr = [12, 4, 7, 9, 2, 23, 25, 41,
           30, 40, 28, 42, 30, 44, 48,
           43, 50]
    m = 7  # Number of students
    n = len(arr)
    print("Minimum difference is", findMinDiff(arr, n, m))


