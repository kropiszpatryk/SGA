import random
def check():
    if lb_pop * ile_os >= 150:
        print("Liczba przetworzonych w algorytmie osobników jest większa niż 150!")
        exit()

def random_number():
    for i in range(ile_os):
        number = random.randint(0,255)
        numer_list.append(number)

def change_binary():
    numer_list_binary.clear()
    for a in range(len(numer_list)):
        binary = bin(numer_list[a])
        numer_list_binary.append(binary)
    for nums in range(len(numer_list_binary)):
        numer_list_binary[nums] = numer_list_binary[nums][2:]
        numer_list_binary[nums] = ('0' * (8 - (len(numer_list_binary[nums])))) + numer_list_binary[nums]

def conn_pairs():
    random.shuffle(numer_list)
    change_binary()
    for x in range(0, len(numer_list),2):
        w_lb_psl = random.random()
        if w_lb_psl < pr_krzyz:
            pc = random.randint(1, 7)
            p1 = numer_list_binary[x + 1][:pc] + numer_list_binary[x][pc:]
            p2 = numer_list_binary[x][:pc] + numer_list_binary[x + 1][pc:]
            numer_list_binary[x] = p1
            numer_list_binary[x + 1] = p2

def mutation():
    #print("Lista przed mutacją: ", numer_list_binary)
    for q in range(len(numer_list_binary)):
        numer_list_last = []
        for o in range(len(numer_list_binary[q])):
            w_lb_psl = random.random()
            if w_lb_psl <= pr_mut:
                if numer_list_binary[q][o] == '1':
                    numer_list_last.append('0')
                else:
                    numer_list_last.append('1')
            else:
                numer_list_last.append(numer_list_binary[q][o])
        numer_list_binary[q] = ''.join(numer_list_last)
    #print("Lista po mutacji: ", numer_list_binary)


def change_int():
    for h in range(len(numer_list_binary)):
        numer_list[h] = int(numer_list_binary[h],2)
    #print("Lista po mutacji i konwersji: ",numer_list)


def function():
    function_list.clear()
    for v in range(len(numer_list)):
        fun = (a * numer_list[v]**2) + b * (numer_list[v]) + c
        function_list.append(fun)
        #print("Wynik funkcji f(x) = ax2 + bx + c dla zmiennej x:", numer_list[v], "wynosi: ", fun)
    #print(function_list)

def probability():
    selection_list.clear()
    #checking = 0
    fun_sum = sum(function_list)
    #print(fun_sum)
    for o in range(ile_os):
        propab_fun = function_list[o] / fun_sum
        selection_list.append(propab_fun)
        #print("Wynik prawdopodobieństwa wynosi: ",propab_fun)
        #checking += propab_fun
    #print(checking)


def selection():
    selection_list_finally.clear()
    #print(numer_list)
    #print(selection_list)

    for s in range(ile_os):
        f = 0
        ran = random.random()
        for x in range(len(selection_list)):
            if f < ran < selection_list[x] + f:
                selection_list_finally.append(numer_list[x])
            f += selection_list[x]
    numer_list.clear()
    for z in range(len(selection_list_finally)):
        numer_list.append(selection_list_finally[z])

def func(x):
    return (a * x**2) + (b * x) + c

def start():
    check()
    numer_list.clear()
    random_number()
    for x in range(lb_pop):
        conn_pairs()
        mutation()
        change_int()
        function()
        probability()
        selection()

    best = max(numer_list, key=lambda x: func(x))

    with open("esi_db.txt", "a") as f:
        print(f"{func(best)} {best}", file=f)
        print("", file=f)

a = 4
b = 7
c = 2
ile_wyn = 40 #liczba uruchomien porogramu
lb_pop = 10 #liczba populacji
ile_os = 6 #liczba osobników w populacji
pr_krzyz = 0.8 #prawdopodobnienstwo krzyzowania
pr_mut = 0.1 #prawdopodobnieństwo mutacji

selection_list = [] #wyniki prawdoipodobnienstwa
fun_draw = [] #lista do nkrotnego losowaniia
function_list =[] #wyniki funkcjii
numer_list = [] #wyniki po mutacji i kowersji
numer_list_binary = [] # wyniki po mutacji
selection_list_finally = [] # nowa populacja


for x in range(ile_wyn):
    x += 1
    print("Przejście pętli: ", x)
    start()
