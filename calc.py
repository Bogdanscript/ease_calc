print("@@@@@@@  @@@ @@  @@@@  @@@@@@")
print("@@    @@ @@@ @@ @@  @@ @@   @@")
print("@@    @@     @@@@      @@   @@")
print("@@    @@ @@@ @@@       @@   @@")
print("@@@@@@@  @@@ @@        @@   @@")
print("@@    @@ @@@ @@        @@   @@")
print("@@    @@ @@@ @@        @@   @@")
print("@@    @@ @@@ @@        @@   @@")
print("@@@@@@@  @@@ @@        @@@@@@")
name = input("как тебя зовут?: ")
print("привет " + name + " я калькулятор BirD")
print("Ноль в качестве знака операции завершит работу программы")
while True:
    s = input("Знак (+,-,*,/): ")
    if s == '0': break
    if s in ('+','-','*','/'):
        x = float(input("x="))
        y = float(input("y="))
        if s == '+':
            print("%.2f" % (x+y))
        elif s == '-':
            print("%.2f" % (x-y))
        elif s == '*':
            print("%.2f" % (x*y))
        elif s == '/':
            if y != 0:
                print("%.2f" % (x/y))
            else:
                print("Деление на ноль!")
    else:
        print("Неверный знак операции!")