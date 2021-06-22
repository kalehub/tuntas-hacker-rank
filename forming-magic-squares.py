
def forming_magic_squares(s):
    available_target = list()
    target_calc = list()
    # check kemungkinan nilai magic
    for element in s:
        if sum(element) not in available_target:
            available_target.append(sum(element))
    
    # check baris dan kolom
    for target in available_target:
        print(target)
        counter_target = 0
        for i in range(0, len(s)):
            if sum(s[i]) != target:
                print(s[i])
                add_by = abs(target - sum(s[i]))
                counter_target+=add_by
        target_calc.append(counter_target) 
    
    return min(target_calc)                
            
   




def main():
    result = forming_magic_squares([[4,9,2],[3,5,7],[8,1,5]])
    print(result)


if __name__ == "__main__":
    main()

