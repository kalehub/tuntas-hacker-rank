
def decrypt_password(pw):
    decrypted_text  = ""
    k = 0

    for i in range(k, len(pw)):
        print(k)
        if (i <= len(pw)):
            if (pw[i].lower() and pw[(i+1)%len(pw)].isupper()):
                decrypted_text = decrypted_text+pw[(i+1)%len(pw)]+pw[i]+"*"
                k+=2
            elif(pw[i].isnumeric()):
                decrypted_text = decrypted_text+"0"
                decrypted_text = pw[i]+decrypted_text
            else:
                decrypted_text+=pw[i]
        else:
            break

def main():
    ori_string = "aP1pL5e"
    decrypted = decrypt_password(ori_string)
    print(decrypted)
    


if __name__ == "__main__":
    main()
