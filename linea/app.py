# calcua las coodenadas de una linea
def calcular_y(x, m, b):
    '''
    Calcula el valor de y en una linea recta
    x: el valor de x
    m: pendiente
    b: interseccion en y
    regresa el valor de y
    '''
    return m*x + b
def main():
    m=2
    b=3
    x=5
    y = calcular_y(x, m, b)
    print(f'Para x={x}, y ={y}')

if __name__ == '__main__':
    main()