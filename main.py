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
    print(function_list)
def probability():
    checking = 0
    fun_sum = sum(function_list)
    for o in range(ile_os):
        propab_fun = function_list[o] / fun_sum
        selection_list.append(propab_fun)
        print("Wynik prawdopodobieństwa wynosi: ",propab_fun)
    print(selection_list)
        #checking += propab_fun
    #rint(checking)

def draw():
    print("losowanie")
    num_rand = random.randint(0, ile_os)
    for num_rand in range(len(numer_list)):
        fun_draw.append(function_list[num_rand])

    print(fun_draw)
def selection():
    print("selekcja")


a = 4
b = 7
c = 2
ile_wyn = 40 #liczba uruchomien porogramu
lb_pop = 10 #liczba populacji
ile_os = 6 #liczba osobników w populacji
pr_krzyz = 0.8 #prawdopodobnienstwo krzyzowania
pr_mut = 0.1 #prawdopodobnieństwo mutacji

selection_list = []
fun_draw = []
function_list =[]
numer_list = []
numer_list_binary = []

random_number()
conn_pairs()
print("====================================================")
mutation()
print("====================================================")
change_int()
print("====================================================")
function()
print("====================================================")
probability()
print("====================================================")
draw()
print("====================================================")
selection()
print("====================================================")