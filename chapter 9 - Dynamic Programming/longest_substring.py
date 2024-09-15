def longest_substring():

    word_a = "fisher"
    word_b = "sherif"
    grid = [[0 for _ in range(len(word_b))] for _ in range(len(word_a))]
    largest = 0

    for i in range(len(word_a)):
        for j in range(len(word_b)):
            if word_a[i] == word_b[j]:
                grid[i][j] = grid[i - 1][j - 1] + 1
            else:
                grid[i][j] = 0
            if grid[i][j] > largest:
                largest = grid[i][j]
    print(largest)
