
def cats_and_mouse(x,y,z):
    if abs(x-z) < abs(y-z):
        return "Cat A"
    elif abs(x-z) > abs(y-z):
        return "Cat B"
    else:
        return "Mouse C"



def main():
    assert cats_and_mouse(2,5,4), "Cat B"
    assert cats_and_mouse(1,2,3), "Cat B"
    assert cats_and_mouse(1,3,2), "Mouse C"





if __name__ == "__main__":
    main()
