

def calculate_square_area(side):
    area = side * side
    return area


def calculate_rectangle_area(length, width):
    area = length * width
    return area


def calculate_triangle_area(base, height):
    area = (base * height) / 2
    return area


def calculate_circle_area(radius):
    pi = 3.14
    area = pi * (radius ** 2)
    return area


def solve_square():
    side = number_validation('Digite o valor do lado: ')
    area = calculate_square_area(side)
    print(f'A área do quadrado é {area}')


def solve_rectangle():
    length = number_validation('Digite o valor do comprimento: ')
    width = number_validation('Digite o valor da largura: ')
    area = calculate_rectangle_area(length, width)
    print(f'A área do retângulo é {area}')


def solve_triangle():
    base = number_validation('Digite o valor da base: ')
    height = number_validation('Digite o valor da altura: ')
    area = calculate_triangle_area(base, height)
    print(f'A área do triângulo é {area}')


def solve_circle():
    radius = number_validation('Digite o valor do raio: ')
    area = calculate_circle_area(radius)
    print(f'A área do círculo é {area}')


def number_validation(prompt):
    while True:
        try:
            number = float(input(prompt))
            if number <= 0:
                print('O número deve ser maior que 0')
                continue
            else:
                return number
        except ValueError:
            print('Invalid input')
            continue


def option_validation(prompt):
    while True:
        option = int(input(prompt))
        if option < 1 or option > 5:
            print('Opção inválida')
            continue
        else:
            return option


def menu():
    print('1 - Calcular área do quadrado')
    print('2 - Calcular área do retângulo')
    print('3 - Calcular área do triângulo')
    print('4 - Calcular área do círculo')
    print('5 - Sair')


def main():
    print('Calculadora de áreas')

    op = 0
    while (op != 5):
        menu()
        op = option_validation('Escolha uma opção: ')

        if op == 1:
            solve_square()
        elif op == 2:
            solve_rectangle()
        elif op == 3:
            solve_triangle()
        elif op == 4:
            solve_circle()
        else:
            print('Programa encerrado')


if __name__ == '__main__':
    main()
