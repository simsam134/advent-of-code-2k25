

def get_max_val(number_str):
    max_val = 0
    second_max_val = 0
    max_val_index=0
    second_max_val_index=0

    for i in range(len(number_str)):
        if int(number_str[i]) > max_val and i < len(number_str)-1:
            max_val=int(number_str[i])
            max_val_index=i
            # print(second_max_val_index)
            # print(max_val_index)
            if second_max_val_index < max_val_index:
                second_max_val=0
                # second_max_val=int(number_str[i+1])
                # second_max_val_index=i+1
            continue
        # print("####")
        # print(f"number str = {number_str}")
        # print(f"second_max_val = {second_max_val}")
        # print(f"i = {i}")
        # print(f"max_val_index = {max_val_index}")
        # print("####")
        if int(number_str[i]) >= second_max_val and i > max_val_index:
            second_max_val=int(number_str[i])
            second_max_val_index=i
            continue
    # print(max_val)    
    # print(second_max_val)
    # print("######\n")
    # print(int(max_val+second_max_val))
    # print(int(str(max_val)+str(str(second_max_val))))
    return int(str(max_val)+str(second_max_val))
        # if number_str[i] > max_val_1:
        #     max_val_1=number_str[i]
        


def main():
    s=0
    with open("input.txt", encoding="utf-8") as f:
        i=1
        for line in f:
            line = line.rstrip()
            # print(repr(line))

            val = get_max_val(line)
            print(f"{i}: {val}")
            s+=val
            i+=1
    print(s)




if __name__=='__main__':
    main()