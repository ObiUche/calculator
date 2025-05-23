x = input("Enter number:")

y = input("Enter numeber:")

def add(x, y):
    return x + y

command = input("type your command for add, sub, mul, div:")
if command == "add":
    print(add(x,y))