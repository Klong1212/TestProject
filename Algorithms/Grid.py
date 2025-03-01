def Grid_challenge(grid):
    sorted_words = [''.join(sorted(word)) for word in grid]
    sorted_words = [''.join(word) for word in list(zip(*sorted_words))]
    for word in sorted_words:
        for i in range(len(word)-1):
            # print(word[i+1], word[i])
            if word[i+1] >= word[i]:
                pass
            else:
                return 'NO'     
    return 'YES'