def add(a, b):
    answer = a + b
    print(str(a) + '+' + str(b) + ' = ' + str(answer))

def sub(a, b):
    answer = a - b
    print(str(a) + '-' + str(b) + ' = ' + str(answer))

def mult(a, b):
    answer = a * b
    print(str(a) + ' x ' + str(b) + ' = ' + str(answer))

def div(a, b):
    answer = a / b
    print(str(a) + ' / ' + str(b) + ' = ' + str(answer))



print('A. Addição')
print('B. Subtração')
print('C. Multiplicação')
print('D. Divisão')
print('E. Exit')

while True:
    print('-' * 15)
    choice = str(input('Digite a sua escolha de acordo com a tabela acima: ')).upper()
    print('-' * 15)

    if choice == 'A':
        print('---Adição---')
        a = int(input('Primeiro número: '))
        b = int(input('Segundo número: '))
        add(a, b)

    elif choice == 'B':
        print('---Subtração---')
        a = int(input('Primeiro número: '))
        b = int(input('Segundo número: '))
        sub(a, b)

    elif choice == 'C':
        print('---Multiplicação---')
        a = int(input('Primeiro número: '))
        b = int(input('Segundo número: '))
        mult(a, b)

    elif choice == 'D':
        print('---Divisão---')
        a = int(input('Primeiro número: '))
        b = int(input('Segundo número: '))
        if b != 0:
            div(a, b)
        else:
            print("Não é possível dividir por zero.")

    elif choice == 'E':
        exit()
    
