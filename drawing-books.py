
def page_count(n,p):
    book_page = list()
    for i in range(1, n+1):
        book_page.append(i)
    
    # making the sub list
    sub_list = [[1]]
    for i in range(1, len(book_page), 2):
        sub_list.append(book_page[i:i+2])

    page_count = -1
    page_found = False
    page_back = -1
    # finding P
    for sub in sub_list:
        if page_found:
            break
        else:
            page_count+=1
            if p in sub:
                page_found = True
            # check dari page terakhir
    page_found = False
    
    for i in range(len(sub_list)-1, -1, -1):
        if page_found:
            break
        else:
            page_back+=1
            if p in sub_list[i]:
                page_found = True
    
    if page_count < page_back:
        return page_count
    else:
        return page_back

        




        




def main():
    result = page_count(5,4)
    print(result)




if __name__ == "__main__":
    main()
