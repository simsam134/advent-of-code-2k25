

def main():
    current_value = 50
    tot_times_at_0=0
    with open("input.txt", encoding="utf-8") as f:
        for line in f:
            line = line.rstrip()
            direction = line[0]
            lenght = int(line[1:])
            num_whole_laps = lenght//100
            tot_times_at_0 +=num_whole_laps
            lenght = lenght%100
            old_value=current_value
            if direction=="L":
                current_value-=lenght
                # if current_value-lenght==0:

                if current_value < 0:
                    current_value = 100-abs(current_value)
                    if old_value!=0:
                        tot_times_at_0+=1
                elif current_value==0 and lenght!=0:
                    tot_times_at_0+=1
            elif direction=="R":
                current_value+=lenght
                if current_value > 99:
                    current_value = current_value-100
                    tot_times_at_0+=1
            print(f"Current value = {current_value}")
            print(f"total times through zero: {tot_times_at_0}\n")
            # if current_value==0:
            #     tot_times_at_0+=1

    print(f"Total times at 0:{tot_times_at_0}")
    return


if __name__ == "__main__":
    main()