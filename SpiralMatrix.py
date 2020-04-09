import numpy as np
class Solution(object):
    def spiralOrder(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: List[int]
        """
        matrix=np.array(matrix)
        n,m=matrix.shape
        output=[]
        for i in range(n):
            if len(list(matrix[i][i:m-i][:]))!=0:
                output.append(matrix[i][i:m-i][:])
            else:
                return np.concatenate( output, axis=0 )
            if len(list(matrix[i+1:m-i-1,n-i-1][:]))!=0:
                output.append(matrix[i+1:m-i,n-i-1][:])
            else:
                return np.concatenate( output, axis=0 )
            if len(list(matrix[:][n-1][:m-i-1][::-1]))!=0:
                output.append(matrix[:][n-1][:m-i-1][::-1])
            else:
                return np.concatenate( output, axis=0 )
            if len(list(matrix[i+1:m-i,i][::-1]))!=0:
                output.append(matrix[i+1:m-i-2,i][::-1])
            else:
                return np.concatenate( output, axis=0 )
            if i==int((m)/2):
                return output
        return output
        
input=[
  [1, 2, 3, 4],
  [5, 6, 7, 8],
  [9,10,11,12]
]
input2=[
 [ 1, 2, 3 ],
 [ 4, 5, 6 ],
 [ 7, 8, 9 ]
]
s=Solution()
print(s.spiralOrder(input) )
print(s.spiralOrder(input2))
