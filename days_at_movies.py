
def to_reverse(num):
    reversed_number = str(num)[::-1]
    
    return int(reversed_number)



def days_at_movies(start_ , end_ , beauty):
    beautiful_count = 0
    numbered_days = [x for x in range(start_, end_+1)]

    for number in numbered_days:
        reversed_number = int(str(number)[::-1])
        if abs(number - reversed_number)%beauty == 0:
            beautiful_count+=1
        else:
            continue

    
    return beautiful_count

def main():
    result = days_at_movies(20,23,6)
    print(f"Hasil: {result}")


if __name__ == "__main__":
    main()
