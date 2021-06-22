
def hurdle_race(char_height, hurdle_height):
    if char_height > max(hurdle_height):
        return 0
    else:
        return max(hurdle_height) - char_height


def main():
    result = hurdle_race(4, [1,6,3,5,2])
    print(f"Hasil: {result}")


if __name__ == "__main__":
    main()

