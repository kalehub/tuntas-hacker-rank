from collections import Counter



def sales_merchant(n : int, ar : int) -> int:
    item_counter = dict(Counter(ar))
    pair_of_shocks = 0

    for key, value in item_counter.items():
        if value != 0:
            if value % 2 != 0:
                pair_of_shocks += (value-1)/2
            else:
                pair_of_shocks += value/2
    
    return int(pair_of_shocks)
def main():
    n = 9
    ar = [10,20,20,10,10,30,50,10,20]
    result = sales_merchant(n,ar)
    print(result)


if __name__ == "__main__":
    main()

