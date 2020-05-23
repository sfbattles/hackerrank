a = [[11, 2, 4],      #0,0      0,1      0,2     
     [4, 5, 6],       #1,0      1,1      1,2     
     [10, 8, -12]],    #2,0      2,1      2,2       

def diagonalDifference(arr):
    r_to_l_diagonal = 0
    l_to_r_diagonal = 0     
    for i in range(len(arr)):
        for j in range(len(arr[i])):
            if i == j:
                l_to_r_diagonal += arr[i][j]
            if i + j == len(arr) - 1:   #sum of indecies = len(matrix - 1)
                r_to_l_diagonal += arr[i][j]
    return abs(l_to_r_diagonal - r_to_l_diagonal)