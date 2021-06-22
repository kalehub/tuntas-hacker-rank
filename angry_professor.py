def angry_professor(treshold, arrival_time):
    on_time = list(filter(lambda x: x <= 0, arrival_time))
    if len(on_time) >= treshold:
        return "NO"
    else:
        return "YES"

def main():
    result = angry_professor(3, [-1,-3,4,2])
    print(f"hasil: {result}")


if __name__ == "__main__":
    main()
