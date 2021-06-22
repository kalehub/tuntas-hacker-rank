
def get_money_spent(keyboards, drives, b):
    most_expensive = 0
    for board in keyboards:
        for drive in drives:
            if board+drive < b:
                if most_expensive < board+drive:
                    most_expensive = board+drive
    
    if most_expensive != 0:
        return most_expensive
    else:
        return -1
def main():
    result = get_money_spent([3,1], [5,2,8], 10)
    print(result)


if __name__ == "__main__":
    main()
