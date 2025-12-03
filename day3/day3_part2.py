def get_max_val(number_str):
    n = 12
    nbrs=[0]*n
    cur_idx=0
    cur_max=0
    for j in range(n):
        for i in range(cur_idx, len(number_str)-n+j+1):
            if int(number_str[i]) > cur_max:
                cur_max=int(number_str[i])
                cur_idx=i+1
        nbrs[j] = str(cur_max)
        cur_max=0
    ans = "".join(nbrs)
    return int(ans)

def main():
    s=0
    with open("input.txt", encoding="utf-8") as f:
        i=1
        for line in f:
            line = line.rstrip()
            val = get_max_val(line)
            print(f"{i}: {val}")
            s+=val
            i+=1
    print(s)

if __name__=='__main__':
    main()