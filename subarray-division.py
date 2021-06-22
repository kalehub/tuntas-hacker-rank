
def birthday(arr,target_of_sum,length_of_sum):
    already_used = [ False for ar in arr]
    for i in range(0, len(arr)):
        for j in range(0, len(arr)):
            if j != i and already_used[j] == False and already_used[i]==False:
                if arr[i] + arr[j] == target_of_sum:
                    print(arr[i], arr[j])
                    already_used[j] = True
                    already_used[i] = True








def main():
    s = [2, 2, 1, 3, 2] 
    d = 4
    m = 2

    result = birthday(s,d,m)
    print(result)




if __name__ == "__main__":
    main()
