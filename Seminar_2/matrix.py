def trace_calculating(matrix):
    trace = 0
    for i, row in enumerate(matrix):
        for j, el in enumerate(row):
            if i == j:
                trace += el
    print(trace)

trace_calculating([[1,2,3],
                    [9,1,4],
                    [98,-8,12]])