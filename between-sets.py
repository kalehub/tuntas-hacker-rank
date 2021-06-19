
def get_total(a,b):
    value_list = list()
    full_list = a+b

    for i in range(a[1], b[0], a[1]):
        habis_dibagi = False
        for full in full_list:
            print(i)
            if i % full == 0:
                habis_dibagi = True
                print(i, full)
        if habis_dibagi :
            value_list.append(i)
    
    value_list.append(b[0])
    
    # double check
    

def main():
    arr = [2,4]
    arr2 = [16,32,96]

    result = get_total(arr, arr2)



if __name__ == "__main__":
    main()
