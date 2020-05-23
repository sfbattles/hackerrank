arr = [1,1,0,-1,-1]

def plusMinus(arr):
    positive_num = 0
    negative_num = 0
    zeros_in_num = 0
    denominator = len(arr)
    for x in range(denominator):
        if arr[x] > 0:
            positive_num += 1
        elif arr[x] < 0:
            negative_num += 1
        else:
            zeros_in_num += 1
    print(f"{positive_num / denominator:.6f} ")   
    print(f"{negative_num / denominator:.6f} ")   
    print(f"{zeros_in_num / denominator:.6f} ")   

plusMinus(arr)