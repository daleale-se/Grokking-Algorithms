def longest_subsequence():

    word_a = "fisherman"
    word_b = "fooman"
    grid = [[0 for _ in range(len(word_b))] for _ in range(len(word_a))]

    for i in range(len(word_a)):
        for j in range(len(word_b)):
            if word_a[i] == word_b[j]:
                grid[i][j] = grid[i - 1][j - 1] + 1
            else:
                grid[i][j] = max(grid[i-1][j], grid[i][j-1])
    print(grid[-1][-1])
