import h5py
n = int(input())


def row_sum(n: int):
    prev_row: list[int] = []
    n_row: list[int] = []

    if n > 1:
        for i in range(1, n*(n-1), 2):
            prev_row.append(i)

        for i in range(prev_row[-1]+2, prev_row[-1]+(n*2)+2, 2):
            n_row.append(i)
    else:
        n_row.append(n)

    return sum(n_row)


n = row_sum(n)
print(n)

h5py.run_tests()
