
def prisioner_to_be_warned(number_of_prisoner, amount_of_candies, start_chair):
    prisoner_array = [ i for i in range(1, number_of_prisoner+1) ]
    start_point = start_chair-1
    start_count = 0
    warned_prisoner = 0

    while start_count != amount_of_candies:
        if start_point == len(prisoner_array)-1:
            print(prisoner_array[start_point])
            start_point = 0
        else:
            print(prisoner_array[start_point])
            start_point+=1
        start_count+=1
    return prisoner_array[start_point-1]

        


def main():
    prisioner_num = prisioner_to_be_warned(5352926151,2380324688,294730870)
    print(f"Result: {prisioner_num}")


if __name__ == "__main__":
    main()
