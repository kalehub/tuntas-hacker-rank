
def jumping_on_the_cloud(cloud_arr, jump_dist):
    curr = 0
    on_start = False
    energy_left = 100

    while not on_start:
        energy_left -= 1
        curr = (curr+jump_dist) % len(cloud_arr)
        if cloud_arr[curr] == 1:
            energy_left -= 2
        if curr == 0:
            on_start = True
    
    return energy_left    



        




def main():
    result = jumping_on_the_cloud([0,0,1,0], 2)
    print(f"Hasil : {result}")



if __name__ == "__main__":
    main()
