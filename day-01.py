

def main():
    arr = [ [11,2,4],[4,5,6],[10,8,-12]]
    left_diagonal = 0
    right_diagonal = 0
    abs_diff = 0

    k = len(arr)-1
    for i in range(0, len(arr)):
        left_diagonal+=arr[i][i]
        right_diagonal+=arr[i][k]
        k = k-1
    
    abs_diff = abs(left_diagonal - right_diagonal)
    print(abs_diff)
        
    
    



if __name__ == "__main__":
    main()
