import random

def rand():
    c = []
    while (len(c) < 8):
        number = random.randint(1, 8)
        if number in c:
            continue
        else:
            c.append(number)

    return c


count = 0
number = 0
while number < 8:
    c = rand()
    for i in range(len(c)):
        row = c[i]
        column = i + 1
        list_recur = [row, column]
        for j in range(len(c)):
            if (i == j):
                pass
            else:
                count = 0
                row1 = c[j]
                column1 = j + 1
                if count == 0:
                    while (row1 > 0 and column1 > 0):
                        list_check = [row1, column1]
                        if list_recur == list_check:
                            count = -1
                            break
                        else:
                            row1 -= 1
                            column1 -= 1
                row1 = c[j]
                column1 = j + 1
                if count == 0:
                    while (row1 < 9 and column1 < 9):
                        list_check = [row1, column1]
                        if list_recur == list_check:
                            count = -1
                            break
                        else:
                            row1 += 1
                            column1 += 1
                row1 = c[j]
                column1 = j + 1
                if count == 0:
                    while (row1 < 9 and column1 > 0):
                        list_check = [row1, column1]
                        if list_recur == list_check:
                            count = -1
                            break
                        else:
                            row1 += 1
                            column1 -= 1
                row1 = c[j]
                column1 = j + 1
                if count == 0:
                    while (row1 > 0 and column1 < 9):
                        list_check = [row1, column1]
                        if list_recur == list_check:
                            count = -1
                            break
                        else:
                            row1 -= 1
                            column1 += 1
            if count == -1:
                break
        if count != -1:
            number += 1
        else:
            number = 0

print(c)
chess = [""] * 8
for i in range(len(c)):
    a = c[i]
    chess[a - 1] = "Q"
    for j in range(len(chess)):
        if (chess[j] == ""):
            print("|", (chess[j]), end="")
        else:
            print("|", chess[j], sep="", end="")
        if (j == 7):
            print("|", end="")
    print()
    chess = [""] * 8