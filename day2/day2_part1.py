
def check_invalid_id(id_str):
    s1, s2 = id_str[0:len(id_str)//2], id_str[len(id_str)//2:]
    if s1==s2:
        return True
    return False


def main():
    s=0
    # with open("input.txt", encoding="utf-8") as f:
    with open("input.txt", encoding="utf-8") as f:
        line = f.read()
    ranges = line.split(",")
    print(ranges)
    for range_ in ranges:
        range_ = range_.split("-")
        r1, r2 = int(range_[0]), int(range_[1])
        while r1 <= r2:
            if len(str(r1))%2 == 0:
                if check_invalid_id(str(r1)):
                    print(f"Invalid string:{str(r1)}")
                    s+= int(r1)
            r1+=1

    print(f"sum={s}")
if __name__ == "__main__":
    main()