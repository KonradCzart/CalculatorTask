def multi(a, b):
    return a * b


def div(a, b):
    return a / b

def add(x,y):
    return x + y
    
def sub(x,y):
    return x - y

def show_menu():
    print("Wybierz opcje: ")
    print("1: Dodawanie")
    print("2: Odejmowanie")
    print("3: Dzielenie")
    print("4: Mnozenie")
    print("5: Wyjscie")

if __name__ == '__main__':
    print("Hello world")
    
    while True:
        x = input("Operation: + - * /")
        
        if x == "q":
            print("End")
            break
        
        y1 = int(input("Number 1:"))
        y2 = int(input("Number 2:"))

        if x == "+":
            print(y1, "+", y2, "=", add(y1,y2))        

        elif x == "-":
            print(y1, "-", y2, "=", sub(y1,y2))
            
        elif x == "*":
            print(y1, "*", y2, "=", multi(y1,y2))

        elif x == "/":
            print(y1, "/", y2, "=", div(y1,y2))    