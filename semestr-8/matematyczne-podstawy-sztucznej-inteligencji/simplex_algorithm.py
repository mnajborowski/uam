import numpy as np


# Generowanie tablicy numpy z wystarczającą liczbą rzędów dla każdego
# ograniczenia + funkcja obiektu i z wystarczającą liczbą kolumn dla zmiennych,
# luźnych zmiennych, M (max/min) i odpowiadających mu wartości.
def gen_matrix(var, cons):
    tab = np.zeros((cons + 1, var + cons + 2))
    return tab


# Sprawdzenie czy 1+ pivotów jest potrzebnych przez negatywny element w najdalszej prawej
# kolumnie, wykluczając dolną wartość.
def next_round_r(table):
    m = min(table[:-1, -1])
    if m >= 0:
        return False
    else:
        return True


# Sprawdzenie, czy 1+ pivotów jest potrzebnych przez negatywny element w dolnym rzędzie,
# wykluczając ostatnią wartość.
def next_round(table):
    lr = len(table[:, 0])
    m = min(table[lr - 1, :-1])
    if m >= 0:
        return False
    else:
        return True


# Szukanie negatywnego elementu w najdalszej prawej kolumnie.
def find_neg_r(table):
    lc = len(table[0, :])
    m = min(table[:-1, lc - 1])
    if m <= 0:
        n = np.where(table[:-1, lc - 1] == m)[0][0]
    else:
        n = None
    return n


# Szukanie negatywnego elementu w dolnym rzędzie.
def find_neg(table):
    lr = len(table[:, 0])
    m = min(table[lr - 1, :-1])
    if m <= 0:
        n = np.where(table[lr - 1, :-1] == m)[0][0]
    else:
        n = None
    return n


# Szukanie pivota odpowiadającego wartościom indeksów kolumn i rzędów z uwzględnieniem negatywnych elementów w
# ostatniej kolumnie i ostatnim rzędzie.
def loc_piv_r(table):
    total = []
    r = find_neg_r(table)
    row = table[r, :-1]
    m = min(row)
    c = np.where(row == m)[0][0]
    col = table[:-1, c]
    for i, b in zip(col, table[:-1, -1]):
        if i ** 2 > 0 and b / i > 0:
            total.append(b / i)
        else:
            total.append(10000)
    index = total.index(min(total))
    return [index, c]


# Funkcja zwraca konkretny elementy tablicy, na którym będzie pivotować.
def loc_piv(table):
    if next_round(table):
        total = []
        n = find_neg(table)
        for i, b in zip(table[:-1, n], table[:-1, -1]):
            if b / i > 0 and i ** 2 > 0:
                total.append(b / i)
            else:
                total.append(10000)
        index = total.index(min(total))
        return [index, n]


# Funkcja odpowiadająca za obrót tabeli wokół podanego elementu i usuwanie ujemnych wartości z ostatniej kolumny
# lub wiersza i zwracanie zaktualizowanej tabeli.
def pivot(row, col, table):
    lr = len(table[:, 0])
    lc = len(table[0, :])
    t = np.zeros((lr, lc))
    pr = table[row, :]
    if table[row, col] ** 2 > 0:
        e = 1 / table[row, col]
        r = pr * e
        for i in range(len(table[:, col])):
            k = table[i, :]
            c = table[i, col]
            if list(k) == list(pr):
                continue
            else:
                t[i, :] = list(k - r * c)
        t[row, :] = list(r)
        return t
    else:
        print('Nie można pivotować elementu.')


# Funkcja odpowiada za konwersję łańcucha znaków w zmienne typu float.
def convert(eq):
    eq = eq.split(',')
    if 'G' in eq:
        g = eq.index('G')
        del eq[g]
        eq = [float(i) * -1 for i in eq]
        return eq
    if 'L' in eq:
        l = eq.index('L')
        del eq[l]
        eq = [float(i) for i in eq]
        return eq


# Funkcja odpowiedzialna za przygotowanie tabeli do problemu minimalizacji.
def convert_min(table):
    table[-1, :-2] = [-1 * i for i in table[-1, :-2]]
    table[-1, -1] = -1 * table[-1, -1]
    return table


# Funkcja, która wygeneruje tylko wymaganą liczbę zmiennych x1, x2, xn.
def gen_var(table):
    lc = len(table[0, :])
    lr = len(table[:, 0])
    var = lc - lr - 1
    v = []
    for i in range(var):
        v.append('x' + str(i + 1))
    return v


# Funkcja sprawdzająca czy można dodac przynajmniej 1 ograniczenie do macierzy.
def add_cons(table):
    lr = len(table[:, 0])
    empty = []
    for i in range(lr):
        total = 0
        for j in table[i, :]:
            total += j ** 2
        if total == 0:
            empty.append(total)
    if len(empty) > 1:
        return True
    else:
        return False


# Funkcja, która bierze tabelę jako argument jak i równanie, które będzie przekonwertowane z wykorzystaniem powyższych
# metod, a następnie dodane do tabeli.
def constrain(table, eq):
    if add_cons(table) == True:
        lc = len(table[0, :])
        lr = len(table[:, 0])
        var = lc - lr - 1
        j = 0
        while j < lr:
            row_check = table[j, :]
            total = 0
            for i in row_check:
                total += float(i ** 2)
            if total == 0:
                row = row_check
                break
            j += 1
        eq = convert(eq)
        i = 0
        while i < len(eq) - 1:
            row[i] = eq[i]
            i += 1
        row[-1] = eq[-1]
        row[var + j] = 1
    else:
        print('Nie można dodać kolejnego ograniczenia')


# Funkcja sprawdza, czy funkcja celu może być dodana do macierzy.
def add_obj(table):
    lr = len(table[:, 0])
    empty = []
    for i in range(lr):
        total = 0
        for j in table[i, :]:
            total += j ** 2
        if total == 0:
            empty.append(total)
    if len(empty) == 1:
        return True
    else:
        return False


# Funkcja, która sprawdza, czy tabela spełnia warunki w add_obj() i jeśli tak to dodaje funkcję celu do tabeli.
def obj(table, eq):
    if add_obj(table) == True:
        eq = [float(i) for i in eq.split(',')]
        lr = len(table[:, 0])
        row = table[lr - 1, :]
        i = 0
        while i < len(eq) - 1:
            row[i] = eq[i] * -1
            i += 1
        row[-2] = 1
        row[-1] = eq[-1]
    else:
        print('Nie można dodać funkcji celu, jeżeli nie są dodane wszystkie ograniczenia.')


# Funkcja maksymalizacji - wykorzystuje pętle aby określić czy 1 + pivotów jest wymagane,
# zlokalizować pivota i kontynuuje proces aż do momentu, gdy wszystkie ujemne elementy
# zostaną usunięte z ostatniego wiersza i kolumny. Następnie zmienne będą wygenerowane
# od x1 do xn oraz przypisane wartości w zależności od ich pozycji w tablicy.
def maxz(table):
    while next_round_r(table) == True:
        table = pivot(loc_piv_r(table)[0], loc_piv_r(table)[1], table)
    while next_round(table) == True:
        table = pivot(loc_piv(table)[0], loc_piv(table)[1], table)
    lc = len(table[0, :])
    lr = len(table[:, 0])
    var = lc - lr - 1
    i = 0
    val = {}
    for i in range(var):
        col = table[:, i]
        s = sum(col)
        m = max(col)
        if float(s) == float(m):
            loc = np.where(col == m)[0][0]
            val[gen_var(table)[i]] = table[loc, -1]
        else:
            val[gen_var(table)[i]] = 0
    val['max'] = table[-1, -1]
    return val


# Funkcja minimalizacji - wykorzystuje pętle aby określić czy 1 + pivotów jest wymagane,
# zlokalizować pivota i kontynuuje proces aż do momentu, gdy wszystkie dodatnie elementy
# zostaną usunięte z ostatniego wiersza i kolumny. Następnie zmienne będą wygenerowane od
# x1 do xn oraz przypisane wartości w zależności od ich pozycji w tablicy.
def minz(table):
    table = convert_min(table)
    while next_round_r(table) == True:
        table = pivot(loc_piv_r(table)[0], loc_piv_r(table)[1], table)
    while next_round(table) == True:
        table = pivot(loc_piv(table)[0], loc_piv(table)[1], table)
    lc = len(table[0, :])
    lr = len(table[:, 0])
    var = lc - lr - 1
    i = 0
    val = {}
    for i in range(var):
        col = table[:, i]
        s = sum(col)
        m = max(col)
        if float(s) == float(m):
            loc = np.where(col == m)[0][0]
            val[gen_var(table)[i]] = table[loc, -1]
        else:
            val[gen_var(table)[i]] = 0
            val['min'] = table[-1, -1] * -1
    return val


if __name__ == "__main__":
    print("Problem maksymalizacji")
    m = gen_matrix(2, 2)
    constrain(m, '2,-1,G,10')
    constrain(m, '1,1,L,20')
    obj(m, '5,10,0')
    print(maxz(m))
    print("Problem minimalizacji")
    m = gen_matrix(2, 4)
    constrain(m, '2,5,G,30')
    constrain(m, '-3,5,G,5')
    constrain(m, '8,3,L,85')
    constrain(m, '-9,7,L,42')
    obj(m, '2,7,0')
    print(minz(m))
