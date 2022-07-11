def Square_Diff(n):
     

    l = (n * (n + 1) * (2 * n + 1)) / 6
    k = (n * (n + 1)) / 2
    k = k ** 2
    m = abs(l - k)
    return m

print(Square_Diff(10))