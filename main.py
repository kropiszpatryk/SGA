import random


def random_number():
    for i in range(ile_os):
        number = random.randint(0,255)
        numer_list.append(number)

def change_binary():
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
            print("Osobniki: " + p1 + " oraz " + p2 + " krzyżują się")



def mutation():
    print("Lista przed mutacją: ", numer_list_binary)
    for q in range(len(numer_list_binary)):
        numer_list_last = []
        for o in range(len(numer_list_binary[q])):
            rand_mut = random.random()
            if rand_mut < pr_mut:
                if numer_list_binary[q][o] == '1':
                    numer_list_last.append('0')
                else:
                    numer_list_last.append('1')
            else:
                numer_list_last.append(numer_list_binary[q][o])
        numer_list_binary[q] = ''.join(numer_list_last)
        print("Lista po mutacji: ", numer_list_binary)


def change_int():
    for h in range(len(numer_list_binary)):
        numer_list[h] = int(numer_list_binary[h],2)
    print("Lista po mutacji i konwersji: ",numer_list)


def function():
    for v in range(len(numer_list)):
        fun = (a * numer_list[v]**2) + b * (numer_list[v]) + c
        function_list.append(fun)
        print("Wynik funkcji f(x) = ax2 + bx + c dla zmiennej x:", numer_list[v], "wynosi: ", fun)


def probability():
    checking = 0
    fun_sum = sum(function_list)
    for o in range(ile_os):
        propab_fun = function_list[o] / fun_sum
        selection_list.append(propab_fun)
        print("Wynik prawdopodobieństwa wynosi: ",propab_fun)
        #checking += propab_fun
    #rint(checking)

def draw():
    for x in range(len(numer_list)):
        ran = random.randint(0, ile_os-1)
        fun_draw.append(numer_list[ran])
    print("Wynik losowania wynosi", fun_draw)



def selection():
    print("selekcja")
    [float(x) for x in selection_list]
    selection_list.sort()

    print(selection_list)

    person = 0.0
    for s in range(ile_os):
        ran = random.random()
        if ran <= selection_list[0]:
            print("ran jest mniejszy od pierszego indexu")
            person = selection_list[0]
        elif ran >= selection_list[0] and ran <= selection_list[1]:
            print("ran jest w przedziale 0 i 1")
            person = selection_list[1]
        elif ran >= selection_list[1] and ran <= selection_list[2]:
            print("ran jest w przedziale 1 i 2")
            person = selection_list[2]
        elif ran >= selection_list[2] and ran <= selection_list[3]:
            print("ran jest w przedziale 2 i 3")
            person = selection_list[3]
        elif ran >= selection_list[3] and ran <= selection_list[4]:
            print("ran jest w przedziale 3 i 4")
            person = selection_list[4]
        elif ran >= selection_list[4] and ran <= selection_list[5]:
            print("ran jest w przedziale 4 i 5")
            person = selection_list[5]
        else:
            print("ran jest wiekszy od ostatniego indexu")
            person = selection_list[0]
        selection_list_finally.append(person)

    selection_list_finally.sort()

    best = selection_list_finally[5]
    f_best = (a * best**2) + b * (best) + c


    with open("esi_db.txt", "a") as f:
        print(f"best = {best} F(best) = {f_best}", file=f)
        print("", file=f)

def start():

    print("*" * 100)
    random_number()
    print("*" * 100)
    conn_pairs()
    print("*" * 100)
    mutation()
    print("*" * 100)
    change_int()
    print("*" * 100)
    function()
    print("*" * 100)
    probability()
    print("*" * 100)
    draw()
    print("*" * 100)
    selection()
    print("*" * 100)


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
    start()
