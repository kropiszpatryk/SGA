import random
#sssss
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
        if w_lb_psl > pr_krzyz:
            print("osobniki sie nie krzyzuja")
        else:
            print("Krzyzuja sie")
            print(numer_list[x], numer_list[x+1])
            pc = random.randint(1,7)
            p1  = numer_list_binary[x+1][:pc] + numer_list_binary[x][pc:]
            p2  = numer_list_binary[x][:pc] + numer_list_binary[x+1][pc:]
            print(p1, p2)


a = 4
b = 7
c = 2
ile_wyn = 40 #liczba uruchomien porogramu
lb_pop = 10 #liczba populacji
ile_os = 6 #liczba osobników w populacji
pr_krzyz = 0.8 #prawdopodobnienstwo krzyzowania
pr_mut = 25 #prawdopodobnieństwo mutacji

numer_list = []
numer_list_binary = []
random_number()
conn_pairs()
print(numer_list)
print(numer_list_binary)
