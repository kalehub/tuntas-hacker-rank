def predict_height(tree_height, num_of_cycle):
    i = 0
    isSpring = True
    isSummer = False

    while i < num_of_cycle:
        if isSpring:
            tree_height *= 2
            isSpring = False
            isSummer = True
        elif isSummer:
            tree_height += 1
            isSummer = False
            isSpring = True
        i+=1
    else:
        return tree_height


def main():
    result = predict_height(3, 2)
    print(f"Hasil: {result}")


if __name__ == "__main__":
    main()

