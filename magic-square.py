# checking for magic square
def check(lst):
    # check if the list given is a square; otherwise, raise a value error
    if not all(i == len(lst) for i in [len(j) for j in lst]): raise ValueError("Matrix isn't a square")
    # specifying the default sum and length of square side
    tmp, n = sum(lst[0]), len(lst[0])
    # iterating over rows and columns and compare sum of them with "tmp" value (sum of first row)
    for i in range(0, n):
        #     rows                   list of each column
        if sum(lst[i]) != tmp or sum([x[i] for x in lst]) != tmp: return False
    # returning the result of comparing obligue lines with tmp value
    return sum([lst[i][i] for i in range(0, n)]) == tmp and sum([lst[i][-i - 1] for i in range(0, n)]) == tmp

# getting user input in 3 lines (change "range(stop)" to whatever the square side is) and printing the result
print(check([list(map(int, input().split())) for _ in range(0, 5)]))