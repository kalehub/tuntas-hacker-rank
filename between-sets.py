
def get_total(a,b):
    a_index= a[0]
    b_index = max(b)
    hasil = list()

    while a_index <= b_index:
        count_a = 0
        count_b = 0
        for element in a:
            if a_index%element == 0:
                count_a+=1
        if count_a == len(a):
            for temp in b:
                if temp%a_index == 0:
                    count_b+=1
            if count_b == len(b):
                hasil.append(a_index)


        a_index+=a[0]
    print(hasil)
    return len(hasil)
         




    

def main():
    result = get_total([1], [100])
    print(result)



if __name__ == "__main__":
    main()
