def createArray(n, val):
    return [val for i in range(n)]


def inArray(array, item):
    for i in array:
        if item == i:
            return True
    return False


def createMatrix(n, m, val):
    return [[val for j in range(m)] for i in range(n)]


def printMatrix(matrix):
    for row in matrix:
        for item in row:
            # print("{:4d}".format(item), end="")
            print("{:.2f}".format(item), end="  ")
        print()


x = 3
rangeX = range(x)
p = 3
rangeP = range(p)
indicators = [1, 3, 5, 7, 9]

movies = ['Маленькие женщины', 'Тайное общество младших монарших особ', 'Кошмар на улице Вязов']
print("Фильмы:")
for i in rangeX:
    print(str(i + 1) + " - " + movies[i])
print()

criteria = ['Сюжет', 'Игра актеров', 'Спецэффекты']
print("Критерии:")
for i in rangeP:
    print(str(i + 1) + " - " + criteria[i])
print()

A = [createMatrix(x, x, 0) for k in rangeP]
u = createMatrix(x, p, 0)

for k in rangeP:
    print("Парное сравнение фильмов по отношению к критерию '" + criteria[k] + "':")
    print("Укажите кто над кем имеет преимущество и насколько в формате ")
    print(
        "[номер фильма, который имеет преимущество][номер фильма, над которым имеется преимущество]-[показатель преимущества(1, 3, 5, 7 или 9)]")
    print("Пример: 12-3")
    str1 = input()
    while not (
            len(str1) == 4 and inArray(rangeX, int(str1[0]) - 1) and inArray(rangeX, int(str1[1]) - 1) and
            str1[0] != str1[1] and str1[2] == '-' and inArray(indicators, int(str1[3]))
    ):
        print('Введенное вами не соответстует форме! Введите еще раз')
        str1 = input()
    A[k][int(str1[0]) - 1][int(str1[1]) - 1] = int(str1[3])
    A[k][int(str1[1]) - 1][int(str1[0]) - 1] = 1 / int(str1[3])
    print("Укажите еще раз кто над кем имеет преимущество и насколько в формате ")
    print(
        "[номер фильма, который имеет преимущество][номер фильма, над которым имеется преимущество]-[показатель преимущества(1, 3, 5, 7 или 9)]")
    print("Важно, чтобы только один из номеров фильмов совпал!")
    str2 = input()
    while not (
            len(str2) == 4 and inArray(rangeX, int(str2[0]) - 1) and inArray(rangeX, int(str2[1]) - 1) and
            str2[0] != str2[1] and str2[2] == '-' and inArray(indicators, int(str2[3])) and (
                    (str1[0] == str2[0] and str1[1] != str2[1]) or (str1[0] == str2[1] and str1[1] != str2[0]) or
                    (str1[1] == str2[0] and str1[0] != str2[1]) or (str1[1] == str2[1] and str1[0] != str2[0])
            )
    ):
        print('Введенное вами не соответстует форме! Введите еще раз')
        str2 = input()
    A[k][int(str2[0]) - 1][int(str2[1]) - 1] = int(str2[3])
    A[k][int(str2[1]) - 1][int(str2[0]) - 1] = 1 / int(str2[3])

    for i in rangeX:
        for j in rangeX:
            if i == j:
                A[k][i][j] = 1
            elif A[k][i][j] == 0:
                if (i == 0 and j == 1) or (i == 1 and j == 0):
                    A[k][i][j] = A[k][2][j] / A[k][2][i]
                elif (i == 0 and j == 2) or (i == 2 and j == 0):
                    A[k][i][j] = A[k][1][j] / A[k][1][i]
                else:
                    A[k][i][j] = A[k][0][j] / A[k][0][i]
            elif inArray(indicators, A[k][i][j]):
                A[k][j][i] = 1 / A[k][i][j]
    print("Матрица парных сравнений по критерию '" + criteria[k] + "':")
    printMatrix(A[k])
    print()

    for rx in rangeX:
        s = 0
        for i in rangeX:
            s += A[k][i][rx]
        u[rx][k] = 1 / s
print("Матрица степеней принадлежности:")
printMatrix(u)
print()

C_rav = createArray(x, 1)

print("Результат:")
for i in rangeX:
    for j in rangeP:
        if u[i][j] < C_rav[i]:
            C_rav[i] = u[i][j]
    print(str(round(C_rav[i], 2)))
print()

res_rav = createArray(x, 0)
res_n_rav = createArray(x, 0)

srtd = sorted(C_rav, reverse=True)
print("При равновесных критериях:")
for i in rangeX:
    for j in rangeX:
        if C_rav[j] == srtd[i]:
            res_rav[i] = j
            res_n_rav[i] = j
            print(str(i + 1) + " место - " + movies[j])
print()

B = createMatrix(p, p, 0)

print("Парное сравнение критериев по степени важности:")
print("Укажите кто над кем имеет преимущество и насколько в формате ")
print(
    "[номер критерия, который имеет преимущество][номер критерия, над которым имеется преимущество]-[показатель преимущества(1, 3, 5, 7 или 9)]")
print("Пример: 12-3")
str1 = input()
while not (
        len(str1) == 4 and inArray(rangeP, int(str1[0]) - 1) and inArray(rangeP, int(str1[1]) - 1) and
        str1[0] != str1[1] and str1[2] == '-' and inArray(indicators, int(str1[3]))
):
    print('Введенное вами не соответстует форме! Введите еще раз')
    str1 = input()
B[int(str1[0]) - 1][int(str1[1]) - 1] = int(str1[3])
B[int(str1[1]) - 1][int(str1[0]) - 1] = 1 / int(str1[3])
print("Укажите еще раз кто над кем имеет преимущество и насколько в формате ")
print(
    "[номер критерия, который имеет преимущество][номер критерия, над которым имеется преимущество]-[показатель преимущества(1, 3, 5, 7 или 9)]")
print("Важно, чтобы только один из номеров критериев совпал!")
str2 = input()
while not (
        len(str2) == 4 and inArray(rangeP, int(str2[0]) - 1) and inArray(rangeP, int(str2[1]) - 1) and
        str2[0] != str2[1] and str2[2] == '-' and inArray(indicators, int(str2[3])) and (
                (str1[0] == str2[0] and str1[1] != str2[1]) or (str1[0] == str2[1] and str1[1] != str2[0]) or
                (str1[1] == str2[0] and str1[0] != str2[1]) or (str1[1] == str2[1] and str1[0] != str2[0])
        )
):
    print('Введенное вами не соответстует форме! Введите еще раз')
    str2 = input()
B[int(str2[0]) - 1][int(str2[1]) - 1] = int(str2[3])
B[int(str2[1]) - 1][int(str2[0]) - 1] = 1 / int(str2[3])
for i in rangeP:
    for j in rangeP:
        if i == j:
            B[i][j] = 1
        elif B[i][j] == 0:
            B[i][j] = B[0][j] / B[0][i]
        elif inArray(indicators, B[i][j]):
            B[j][i] = 1 / B[i][j]
print("Матрица парных сравнений по степени важности:")
printMatrix(B)
print()

b = createArray(p, 0)

print("Массив значений степеней принадлежности:")
for i in rangeP:
    s = 0
    for j in rangeP:
        s += B[j][i]
    b[i] = 1 / s
    print(str(round(b[i], 2)))
print()

C_nerav = createArray(x, 1)

print("Результат:")
for i in rangeX:
    for j in rangeP:
        if pow(u[i][j], b[j]) < C_nerav[i]:
            C_nerav[i] = pow(u[i][j], b[j])
    print(str(round(C_nerav[i], 2)))
print()

res_nerav = createArray(x, 0)
res_n_nerav = createArray(x, 0)

srtd = sorted(C_nerav, reverse=True)
print("При неравновесных критериях:")
for i in rangeX:
    for j in rangeX:
        if C_nerav[j] == srtd[i]:
            res_nerav[i] = j
            res_n_nerav[i] = j
            print(str(i + 1) + " место - " + movies[j])
print()

movie_n_rav = res_rav[1]
crit_n_rav = -1

for i in rangeP:
    if C_rav[movie_n_rav] == u[movie_n_rav][i]:
        crit_n_rav = i

A_n_rav = createMatrix(x, x, 0)
for i in rangeX:
    for j in rangeX:
        if i == j:
            A_n_rav[i][j] = 1
        elif inArray(indicators, A[crit_n_rav][i][j]):
            A_n_rav[i][j] = A[crit_n_rav][i][j]

while res_n_rav[0] != movie_n_rav:
    for i in rangeX:
        for j in rangeX:
            if not inArray(indicators, A[crit_n_rav][i][j]):
                A_n_rav[i][j] = 0
    u_n_rav = createArray(x, 0)
    C_n_rav = createArray(x, 1)
    if A_n_rav[res_rav[0]][movie_n_rav] > 0:
        if A_n_rav[res_rav[0]][movie_n_rav] == 1:
            print("Улучшение не возможно")
            print()
            break
        else:
            A_n_rav[res_rav[0]][movie_n_rav] -= 2
            A_n_rav[movie_n_rav][res_rav[0]] = 1 / A_n_rav[res_rav[0]][movie_n_rav]
            for i in rangeX:
                for j in rangeX:
                    if A_n_rav[i][j] == 0:
                        if (i == 0 and j == 1) or (i == 1 and j == 0):
                            A_n_rav[i][j] = A_n_rav[2][j] / A_n_rav[2][i]
                        elif (i == 0 and j == 2) or (i == 2 and j == 0):
                            A_n_rav[i][j] = A_n_rav[1][j] / A_n_rav[1][i]
                        else:
                            A_n_rav[i][j] = A_n_rav[0][j] / A_n_rav[0][i]
                    elif inArray(indicators, A_n_rav[i][j]):
                        A_n_rav[j][i] = 1 / A_n_rav[i][j]
            print("Новая матрица парных сравнений по критерию '" + criteria[crit_n_rav] + "':")
            printMatrix(A_n_rav)
            print()

            print("Массив степеней принадлежности критерию '" + criteria[crit_n_rav] + "':")
            for rx in rangeX:
                s = 0
                for i in rangeX:
                    s += A_n_rav[i][rx]
                u_n_rav[rx] = 1 / s
                print(str(round(u_n_rav[rx], 2)))
            print()

            print("Новый результат:")
            for i in rangeX:
                for j in rangeP:
                    if j == crit_n_rav:
                        if u_n_rav[i] < C_n_rav[i]:
                            C_n_rav[i] = u_n_rav[i]
                    else:
                        if u[i][j] < C_n_rav[i]:
                            C_n_rav[i] = u[i][j]
                print(str(round(C_n_rav[i], 2)))
            print()

            srtd = sorted(C_n_rav, reverse=True)
            print("При равновесных критериях после пересмотрения:")
            for i in rangeX:
                for j in rangeX:
                    if C_n_rav[j] == srtd[i]:
                        res_n_rav[i] = j
                        print(str(i + 1) + " место - " + movies[j])
            print()
    else:
        if A_n_rav[movie_n_rav][res_rav[0]] == 9:
            print("Улучшение не возможно")
            print()
            break
        else:
            A_n_rav[movie_n_rav][res_rav[0]] += 2
            A_n_rav[res_rav[0]][movie_n_rav] = 1 / A_n_rav[movie_n_rav][res_rav[0]]
            for i in rangeX:
                for j in rangeX:
                    if A_n_rav[i][j] == 0:
                        if (i == 0 and j == 1) or (i == 1 and j == 0):
                            A_n_rav[i][j] = A_n_rav[2][j] / A_n_rav[2][i]
                        elif (i == 0 and j == 2) or (i == 2 and j == 0):
                            A_n_rav[i][j] = A_n_rav[1][j] / A_n_rav[1][i]
                        else:
                            A_n_rav[i][j] = A_n_rav[0][j] / A_n_rav[0][i]
                    elif inArray(indicators, A_n_rav[i][j]):
                        A_n_rav[j][i] = 1 / A_n_rav[i][j]
            print("Новая матрица парных сравнений по критерию '" + criteria[crit_n_rav] + "':")
            printMatrix(A_n_rav)
            print()

            print("Массив степеней принадлежности критерию '" + criteria[crit_n_rav] + "':")
            for rx in rangeX:
                s = 0
                for i in rangeX:
                    s += A_n_rav[i][rx]
                u_n_rav[rx] = 1 / s
                print(u_n_rav[rx])
            print()

            print("Новый результат:")
            for i in rangeX:
                for j in rangeP:
                    if j == crit_n_rav:
                        if u_n_rav[i] < C_n_rav[i]:
                            C_n_rav[i] = u_n_rav[i]
                    else:
                        if u[i][j] < C_n_rav[i]:
                            C_n_rav[i] = u[i][j]
                print(C_n_rav[i])
            print()

            srtd = sorted(C_n_rav, reverse=True)
            print("При равновесных критериях после пересмотрения:")
            for i in rangeX:
                for j in rangeX:
                    if C_n_rav[j] == srtd[i]:
                        res_n_rav[i] = j
                        print(str(i + 1) + " место - " + movies[j])
            print()

movie_n_nerav = res_nerav[1]
crit_n_nerav = -1

for i in rangeP:
    if C_nerav[movie_n_nerav] == pow(u[movie_n_nerav][i], b[i]):
        crit_n_nerav = i

A_n_nerav = createMatrix(x, x, 0)
for i in rangeX:
    for j in rangeX:
        if i == j:
            A_n_nerav[i][j] = 1
        elif inArray(indicators, A[crit_n_nerav][i][j]):
            A_n_nerav[i][j] = A[crit_n_nerav][i][j]

while res_n_nerav[0] != movie_n_nerav:
    for i in rangeX:
        for j in rangeX:
            if not inArray(indicators, A[crit_n_nerav][i][j]):
                A_n_nerav[i][j] = 0
    u_n_nerav = createArray(x, 0)
    C_n_nerav = createArray(x, 1)
    if A_n_nerav[res_nerav[0]][movie_n_nerav] > 0:
        if A_n_nerav[res_nerav[0]][movie_n_nerav] == 1:
            print("Улучшение не возможно")
            print()
            break
        else:
            A_n_nerav[res_nerav[0]][movie_n_nerav] -= 2
            A_n_nerav[movie_n_nerav][res_nerav[0]] = 1 / A_n_nerav[res_nerav[0]][movie_n_nerav]
            for i in rangeX:
                for j in rangeX:
                    if A_n_nerav[i][j] == 0:
                        if (i == 0 and j == 1) or (i == 1 and j == 0):
                            A_n_nerav[i][j] = A_n_nerav[2][j] / A_n_nerav[2][i]
                        elif (i == 0 and j == 2) or (i == 2 and j == 0):
                            A_n_nerav[i][j] = A_n_nerav[1][j] / A_n_nerav[1][i]
                        else:
                            A_n_nerav[i][j] = A_n_nerav[0][j] / A_n_nerav[0][i]
                    elif inArray(indicators, A_n_nerav[i][j]):
                        A_n_nerav[j][i] = 1 / A_n_nerav[i][j]
            print("Новая матрица парных сравнений по критерию '" + criteria[crit_n_nerav] + "':")
            printMatrix(A_n_nerav)
            print()

            print("Массив степеней принадлежности критерию '" + criteria[crit_n_nerav] + "':")
            for rx in rangeX:
                s = 0
                for i in rangeX:
                    s += A_n_nerav[i][rx]
                u_n_nerav[rx] = 1 / s
                print(str(round(u_n_nerav[rx], 2)))
            print()

            print("Новый результат:")
            for i in rangeX:
                for j in rangeP:
                    if j == crit_n_nerav:
                        if pow(u_n_nerav[i], b[j]) < C_n_nerav[i]:
                            C_n_nerav[i] = pow(u_n_nerav[i], b[j])
                    else:
                        if pow(u[i][j], b[j]) < C_n_nerav[i]:
                            C_n_nerav[i] = pow(u[i][j], b[j])
                print(str(round(C_n_nerav[i], 2)))
            print()

            srtd = sorted(C_n_nerav, reverse=True)
            print("При неравновесных критериях после пересмотрения:")
            for i in rangeX:
                for j in rangeX:
                    if C_n_nerav[j] == srtd[i]:
                        res_n_nerav[i] = j
                        print(str(i + 1) + " место - " + movies[j])
            print()
    else:
        if A_n_nerav[movie_n_nerav][res_nerav[0]] == 9:
            print("Улучшение не возможно")
            print()
            break
        else:
            A_n_nerav[movie_n_nerav][res_nerav[0]] += 2
            A_n_nerav[res_nerav[0]][movie_n_nerav] = 1 / A_n_nerav[movie_n_nerav][res_nerav[0]]
            for i in rangeX:
                for j in rangeX:
                    if A_n_nerav[i][j] == 0:
                        if (i == 0 and j == 1) or (i == 1 and j == 0):
                            A_n_nerav[i][j] = A_n_nerav[2][j] / A_n_nerav[2][i]
                        elif (i == 0 and j == 2) or (i == 2 and j == 0):
                            A_n_nerav[i][j] = A_n_nerav[1][j] / A_n_nerav[1][i]
                        else:
                            A_n_nerav[i][j] = A_n_nerav[0][j] / A_n_nerav[0][i]
                    elif inArray(indicators, A_n_nerav[i][j]):
                        A_n_nerav[j][i] = 1 / A_n_nerav[i][j]
            print("Новая матрица парных сравнений по критерию '" + criteria[crit_n_nerav] + "':")
            printMatrix(A_n_nerav)
            print()

            print("Массив степеней принадлежности критерию '" + criteria[crit_n_nerav] + "':")
            for rx in rangeX:
                s = 0
                for i in rangeX:
                    s += A_n_nerav[i][rx]
                u_n_nerav[rx] = 1 / s
                print(str(round(u_n_nerav[rx], 2)))
            print()

            print("Новый результат:")
            for i in rangeX:
                for j in rangeP:
                    if j == crit_n_nerav:
                        if pow(u_n_nerav[i], b[j]) < C_n_nerav[i]:
                            C_n_nerav[i] = pow(u_n_nerav[i], b[j])
                    else:
                        if pow(u[i][j], b[j]) < C_n_nerav[i]:
                            C_n_nerav[i] = pow(u[i][j], b[j])
                print(str(round(C_n_nerav[i], 2)))
            print()

            srtd = sorted(C_n_nerav, reverse=True)
            print("При неравновесных критериях после пересмотрения:")
            for i in rangeX:
                for j in rangeX:
                    if C_n_nerav[j] == srtd[i]:
                        res_n_nerav[i] = j
                        print(str(i + 1) + " место - " + movies[j])
            print()
