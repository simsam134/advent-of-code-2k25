

def main():
    current_value = 50
    tot_times_at_0=0
    with open("input.txt", encoding="utf-8") as f:
        for line in f:
            line = line.rstrip()
            direction = line[0]
            lenght = int(line[1:])
            lenght = lenght%100
            print(current_value)
            if direction=="L":
                current_value-=lenght
                if current_value < 0:
                    current_value = 100-abs(current_value)
            elif direction=="R":
                current_value+=lenght
                if current_value > 99:
                    current_value = current_value-100
            if current_value==0:
                tot_times_at_0+=1

    print(f"Total times at 0:{tot_times_at_0}")
    return


if __name__ == "__main__":
    main()