def check_invalid_id(id_str):
    invalid=False
    for block_size in range(1, len(id_str)):
        l = []
        if len(id_str) % block_size == 0:
            for j in range(0, len(id_str), block_size) :
                l.append(id_str[j:j+block_size])
            l = [l[0]==element for element in l]
            if all(l):
                invalid=True
    return invalid


def main():
    s=0
    # with open("input.txt", encoding="utf-8") as f:
    with open("input.txt", encoding="utf-8") as f:
        line = f.read()
    ranges = line.split(",")
    for range_ in ranges:
        range_ = range_.split("-")
        r1, r2 = int(range_[0]), int(range_[1])
        while r1 <= r2:
            if check_invalid_id(str(r1)):
                print(f"Invalid string:{str(r1)}")
                s+= int(r1)
            r1+=1
    print(s)
if __name__ == '__main__':
    main()