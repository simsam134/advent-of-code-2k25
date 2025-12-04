
def check_adj_rolls(grid, x, y):
    nbr_rolls = 0
    # Check row above
    if y > 0:
        nbr_rolls +=int(grid[y-1][x]=="@")
        if x > 0:
            nbr_rolls += int(grid[y-1][x-1]=="@")
        if x < len(grid[0])-1:
            nbr_rolls +=int(grid[y-1][x+1]=="@")
    # Check same row
    if x > 0:
        nbr_rolls +=int(grid[y][x-1]=="@")
    if x < len(grid[0])-1:
        nbr_rolls +=int(grid[y][x+1]=="@")
    # Check row below
    if y < len(grid)-1:
        nbr_rolls +=int(grid[y+1][x]=="@")
        if x > 0:
            nbr_rolls += int(grid[y+1][x-1]=="@")
        if x < len(grid[0])-1:
            nbr_rolls +=int(grid[y+1][x+1]=="@")
    return nbr_rolls

def main():
    s=0
    grid = []
    with open("input.txt", encoding="utf-8") as f:
        for line in f:
            line = list(line.rstrip())
            grid.append(line)
    while True:
        has_updated=False
        for y in range(len(grid)):
            for x in range(len(grid[0])):
                if check_adj_rolls(grid, x, y) < 4 and grid[y][x]=="@":
                    grid[y][x]="."
                    s+=1 
                    has_updated=True
        if not has_updated:
            break
    print(s)


if __name__=='__main__':
    main()