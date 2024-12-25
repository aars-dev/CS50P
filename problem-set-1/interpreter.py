def calculate_expression(x, y, z):
    if y == '+':
        return x + z
    elif y == '-':
        return x - z
    elif y == '*':
        return x * z
    elif y == '/':
        return x / z

def main():
    expression = input("Expression: ")
    x, y, z = expression.split()

    x = int(x)
    z = int(z)

    result = calculate_expression(x,y, z)
    print(format(result, '.1f'))

main()
