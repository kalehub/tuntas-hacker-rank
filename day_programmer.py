
def day_of_programmer(year):
    full_date = ""
    julian_leap = year%4 == 0
    
    
    if julian_leap and year%10 != 0:
        days_left = 12
        full_date = f"{days_left}.09.{year}"
    else:
        days_left = 13
        full_date = f"{days_left}.09.{year}"
    
    
    return full_date




def main():
    year = 2016
    result = day_of_programmer(year)
    print(result)



if __name__ == "__main__":
    main()
