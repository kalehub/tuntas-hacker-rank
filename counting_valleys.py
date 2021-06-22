
def counting_valleys(steps : int, path : str):
    height = 0
    prev_height = 0
    cnt = 0

    for i in range(len(path)):
        if path[i] == "U":
            height+=1
        elif path[i] == "D":
            height-=1
        if height == 0 and prev_height < 0:
            cnt+=1
        prev_height = height
    
    print(cnt)






def main():
    result = counting_valleys(10, "UDUUUDUDDD")
    print(f"Result : {result}")




if __name__ == "__main__":
    main()
