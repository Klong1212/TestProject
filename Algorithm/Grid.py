
def gridChallenge(grid):
    sorted_words = [''.join(sorted(word)) for word in grid]
    for word in sorted_words:
        for i in range(len(word)-1):
            # print(word[i+1], word[i])
            if word[i+1] >= word[i]:
                pass
            else:
                return 'NO'     
    return 'YES'

if __name__ == '__main__':


    t = int(input().strip())

    for t_itr in range(t):
        n = int(input().strip())

        grid = []

        for _ in range(n):
            grid_item = input()
            grid.append(grid_item)

        result = gridChallenge(grid)
