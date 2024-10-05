class Solution(object):
    def pascal_triangle(n):
    a = []  

    for i in range(n + 1):  
        row = []  # Create a new row to populate with values for pascal_triangle to avoid Index out of bounds error
        for j in range(i + 1):  
            if j == 0 or j == i:
                current_value = 1  
            else:
                current_value = a[i-1][j-1] + a[i-1][j]  
            row.append(current_value)  
        
        a.append(row) 

  
        for value in row:
            print(value, end=' ')
        print()  # New line after each row

n = 5
pascal_triangle(n)

