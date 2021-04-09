def multi(a, b):
    return a * b


def div(a, b):
    return a / b


def add(x, y):
    return x + y


def sub(x, y):
    return x - y


def show_menu():
    print("Wybierz opcje: ")
    print("1: Dodawanie")
    print("2: Odejmowanie")
    print("3: Dzielenie")
    print("4: Mnozenie")
    print("5: Wyjscie")


if __name__ == '__main__':
    while True:
        show_menu()
        x = input("Operation: ")
        
        if x == "5":
            print("End")
            break
        
        y1 = int(input("Number 1:"))
        y2 = int(input("Number 2:"))


        if x == "1":
            print(y1, "+", y2, "=", add(y1, y2))
        elif x == "2":
            print(y1, "-", y2, "=", sub(y1, y2))
        elif x == "3":
            print(y1, "-", y2, "/", div(y1, y2))
        elif x == "4":
            print(y1, "-", y2, "=", multi(y1, y2))

