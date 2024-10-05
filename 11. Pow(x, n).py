
class Solution(object):
    def myPow(self, x, n):
        # Step 1: Handle special cases
        if n == 0:
            return 1
        if n < 0:
            x = 1 / x
            n = -n
        
        # Step 2: Initialize the result
        result = 1
        
        # Step 3: Main loop
        while n > 0:
            # Step 3a: Check if n is odd
            if n % 2 == 1:
                result *= x
            
            # Step 3b: Square x
            x *= x
            
            # Step 3c: Halve n
            n //= 2
        
        # Step 4: Return the final result
        return result
