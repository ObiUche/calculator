x = 0

y = 0


first_input = input("Enter number:")

second_input = input("Enter number:")

x = float(first_input)
y = float(second_input)

command = input("type your command for add, sub, mul, div:")

match command:
    case 'add':
          print(x + y)
    case 'sub':
          print(x - y)
    case 'mul':
          print(x * y)
    case 'div':
          print(x / y)
    case _ :
          print("Command not found")
            
            
          


