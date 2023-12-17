class Calculator():

    def __init__(self, nb1, nb2, sum):
        self.nb1 = nb1
        self.nb2 = nb2
        self.sum = sum

    def operator(self, op, nb1, nb2):
        if op == '+':
            sum = nb1 + nb2
            print(f"{nb1} + {nb2} = {sum}")
        elif op == '-':
            sum = nb1 - nb2
            print(f"{nb1} - {nb2} = {sum}")
        elif op == '*':
            sum = nb1 * nb2
            print(f"{nb1} * {nb2} = {sum}")
        else:
            sum = nb1 / nb2
            print(f"{nb1} / {nb2} = {sum}")


while True:
    op = input("Choose your operator: +, -, *, /: ")
    if not op in ['+', '-', '*', '/']:
        print("Choose again ¯\_( ͡❛ ͜ʖ ͡❛)_/¯")
    else:
        print("You chose:", op)
        break

while True:
    nb1 = input("Put the first number: ")
    if nb1.isdigit():
        nb1 = int(nb1)
        break
    else:
        print("Please put a number ( ͡❛ ͜ʖ ͡❛)✊")
    
while True:
    try:
        nb2 = int(input("Put your second number: "))
        break
    except ValueError:
        print("Please put a number ( ͡👁️ ͜ʖ ͡👁️)✊")

Calcul = Calculator(op, nb1, nb2)
Calcul.operator(op, nb1, nb2)