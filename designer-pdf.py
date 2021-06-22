from string import ascii_lowercase
def design_pdf_viewer(char_height, word):
    word = word.lower()
    list_of_words = list()

    # dictionary to know the alphabet
    ALPHABET = {letter: str(index) for index, letter in enumerate(ascii_lowercase, start=0)}
    numbers = [ALPHABET[w] for w in word if w in ALPHABET] 

    for n in numbers:
        list_of_words.append(char_height[int(n)])
    
    return max(list_of_words)*len(word)
    



def main():
    # result = design_pdf_viewer([1,3,1,3,1,4,1,3,2,5,5,5,5,1,1,5,5,1,5,2,5,5,5,5,5,5], "torn")
    result = design_pdf_viewer([1,3,1,3,1,4,1,3,2,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5], "abc")
    print(f"Hasil: {result}")

if __name__ == "__main__":
    main()
