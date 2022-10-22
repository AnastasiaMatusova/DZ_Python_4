#Даны два файла, в каждом из которых находится запись многочлена. 
# Задача - сформировать файл, содержащий сумму многочленов.

from random import randint
 
def write_file(name,st):
    with open(name, 'w') as data:
        data.write(st)

def create_list(k):
    list = []
    for i in range(k + 1):
        list.append(randint(0, 101))    
    return list

def create_str(sp):
    list = sp[::-1]
    wr = ''
    if len(list) < 1:
        wr = 'x = 0'
    else:
        for i in range(len(list)):
            if i != len(list) - 1 and list[i] != 0 and i != len(list) - 2:
                wr += f'{list[i]}x^{len(list) - i - 1}'
                if list [i + 1] != 0:
                    wr += ' + '
            elif i == len(list) - 2 and list[i] != 0:
                wr += f'{list[i]}x'
                if list[i + 1] != 0:
                    wr += ' + '
            elif i == len(list) - 1 and list[i] != 0:
                wr += f'{list[i]} = 0'
            elif i == len(list) - 1 and list[i] == 0:
                wr += ' = 0'
    return wr

def sq_mn(k):
    if 'x^' in k:
        i = k.find('^')
        num = int(k[i+1:])
    elif ('x' in k) and ('^' not in k):
        num = 1
    else:
        num = -1
    return num


def k_mn(k):
    if 'x' in k:
        i = k.find('x')
        num = int(k[:i])
    return num

def calc_mn(st):
    st = st[0].replace(' ', '').split('=')
    st = st[0].split('+')
    lst = []
    l = len(st)
    k = 0
    if sq_mn(st[-1]) == -1:
        lst.append(int(st[-1]))
        l -= 1
        k = 1
    i = 1 
    j = l-1 
    while j >= 0:
        if sq_mn(st[j]) != -1 and sq_mn(st[j]) == i:
            lst.append(k_mn(st[j]))
            j -= 1
            i += 1
        else:
            lst.append(0)
            i += 1
    return lst
    

k1 = int(input("Введите натуральную степень для первого файла k = "))
k2 = int(input("Введите натуральную степень для второго файла k = "))
koef1 = create_list(k1)
koef2 = create_list(k2)
write_file("Task_5.1.txt", create_str(koef1))
write_file("Task_5.2.txt", create_str(koef2))


with open('Task_5.1.txt', 'r') as data:
    st1 = data.readlines()
with open('Task_5.2.txt', 'r') as data:
    st2 = data.readlines()
print(f"Первый многочлен {st1}")
print(f"Второй многочлен {st2}")
lst1 = calc_mn(st1)
lst2 = calc_mn(st2)
ll = len(lst1)
if len(lst1) > len(lst2):
    ll = len(lst2)
lst_new = [lst1[i] + lst2[i] for i in range(ll)]
if len(lst1) > len(lst2):
    mm = len(lst1)
    for i in range(ll,mm):
        lst_new.append(lst1[i])
else:
    mm = len(lst2)
    for i in range(ll,mm):
        lst_new.append(lst2[i])
write_file("Task_5result.txt", create_str(lst_new))
with open('Task_5result.txt', 'r') as data:
    st3 = data.readlines()
print(f"Сумма многочленов {st3}")

# Решение 1 части следует из 4 задачи. Здесь подробно разобрали на семинаре.
# Решение 2 части было Очень сложным. Здесь помогли разобраться.