
def circular_array_rotation(a, k, q):
    new_list = a[:]
    retuned_arr = list()
    for i in range(0, k):
        start_at = -2
        for i in range(0, len(a)):
            new_list[i] = a[start_at+1]
            start_at+=1
        a = new_list[:]
    for j in range(0, len(q)):
        retuned_arr.append(new_list[q[j]])
    
    return retuned_arr

        

def main():
    result = circular_array_rotation([1,2,3], 2, [0,1,2])
    print(f"Res : {result}")
    

if __name__ == "__main__":
    main()
