
n=6
kk = input("enter your name(some letters)-:")
ml = int(input("base symbol multiply enter number [0 to 10](recommended=5 or 6) "))
if kk == '':
    print('nothing is enterd')
    exit()
sym = input('enter any symbol or emoji for pattern')
if sym == '':
    sym = '⭐'

if len(kk) == 4 or len(kk) == 9:
    print('\033[31m give one spaces after your name else star will bend \n \033[0m')
if len(kk) == 3:
    print('\033[31m give one spaces after your name else star will bend \n \033[0m')
if len(kk) < 6:
    gh=sym+' '
    kkk = (kk, '  ')
    kkkk = ''.join(kkk)
    print(f"      {sym} ") ###remove this line if you dont want
    for i in range(n):
        for j in range(-n, -i):
            print(" ", end='')
        for k in range(1):
            print(sym, end='')
            if i == 5:
                for n in range(1):
                    print(f' {kkkk}',
                          end=f'  {sym}                                                                                           ')
        for z in range(i * 2):
            print(" ", end='')
        for x in range(1):
            print(sym, end='')
        print()
    print(sym, end=" ")
    print(gh*ml) ###base symbol

if len(kk) == 6:
    hhh=sym+' '
    print(f"       {sym} ")###remove this line if you dont want
    n = 6
    for i in range(n):
        for j in range(-n, -i):
            print(" ", end='')
        for k in range(1):
            print(sym, end='')
            if i == 5:
                for n in range(1):
                    print(' ',kk,
                          end=f'  {sym}                                                                                                           ')
        for z in range(i * 2):
            print(" ", end='')
        for x in range(1):
            print(sym, end='')
        print()
    print(hhh * ml, end='')###base symbol

if len(kk) == 8:
    print(f"       {sym} ")###remove this line if you dont want
    hhh=sym+' '
    for i in range(n):
        for j in range(-n, -i):
            print(" ", end='')
        for k in range(1):
            print(sym, end='')
            if i == 5:
                for n in range(1):
                    print(f' {kk}',
                          end=f' {sym}                                                                                                           ')
        for z in range(i * 2):
            print(" ", end='')
        for x in range(1):
            print(sym, end='')

        print()
    print(sym, end=' ')
    print(hhh*ml)

if len(kk) == 7:
    print(f"       {sym} ")###remove this line if you dont want
    hhh=sym+' '
    for i in range(n):
        for j in range(-n, -i):
            print(" ", end='')
        for k in range(1):
            print(sym, end='')
            if i == 5:
                for n in range(1):
                    print(f' {kk} ',
                          end=f' {sym}                                                                                                        ')
        for z in range(i * 2):
            print(" ", end='')
        for x in range(1):
            print(sym, end='')
        print()
    print(sym, end=" ")
    print(hhh * ml, end='')

if len(kk)>=9 :
    print(f"       {sym} ")###remove this line if you dont want
    hh=sym+' '
    for i in range(n):
        for j in range(-n, -i):
            print(" ", end='')
        for k in range(1):
            print(sym, end='')
            if i == 5:
                for n in range(1):
                    print(kk,
                          end=f'{sym}                                                                                                                   ')
        for z in range(i * 2):
            print(" ", end='')
        for x in range(1):
            print(sym, end='')
            print()
    print(sym, end=' ')
    print(hh * ml, end='')
