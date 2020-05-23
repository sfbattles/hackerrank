def miniMaxSum(arr):
    arr.sort()
    minsum = 0
    maxsum = 0
    for loop, value in enumerate(arr):
        if loop == len(arr) -1:
            maxsum += value
        elif loop == 0:            
            minsum += value
        else:         
            minsum += value
            maxsum += value
    print(f"{minsum} {maxsum}")
    

the_arr =[1,3,5,7,9]
miniMaxSum(the_arr)