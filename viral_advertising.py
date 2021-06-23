

def viral_advertising(number_of_days):
    i = 0
    shared_count = 5
    cumulative_count = 0
    liked_count = 0
    while i < number_of_days:
        if i == 0:
            shared_count = 5
        else:
            shared_count = liked_count*3
        liked_count = shared_count//2
        cumulative_count+=liked_count
        i+=1
    
    return cumulative_count



def main():
    result = viral_advertising(5)
    print(f"Result: {result}")




if __name__ == "__main__":
    main()

