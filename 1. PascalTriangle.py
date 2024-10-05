class Solution(object):
    def Pascal_Triangle(self, RowNos):
        triangle = []
        
        for i in range(RowNos):
            row = [None] * (i + 1) 
            #Above we have initialized a row of length i+1 with values 'None'
            row[0], row[-1] = 1, 1 
            #Above we are intializing elements at the extreme ends to be 1
            for j in range(1, len(row) - 1):
            # Below, Element j is found by the summation of elements from previous row (i-1) at positions j-1 and j
                row[j] = triangle[i - 1][j - 1] + triangle[i - 1][j]
            triangle.append(row) #the obtained row is added to the triangle
        
        return triangle
