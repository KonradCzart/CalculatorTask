def add(x,y):
    return x + y
    
def sub(x,y):
    return x - y

if __name__ == '__main__':
    print("Hello world")
    
    while True:
        x = input("Operation: + - * /")
        
        if x == "q":
            print("End")
            break
        
        y1 = input("Number 1:")
        y2 = input("Number 2:")

        if x == "+":
            print(y1, "+", y2, "=", add(y1,y2))        

        elif x == "-":
            print(y1, "-", y2, "=", sub(y1,y2))