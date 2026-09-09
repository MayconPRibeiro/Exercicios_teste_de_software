TIPOS = [int, float]

def multiplicar(a, b):
    if type(a) not in TIPOS or type(b) not in TIPOS:
        raise TypeError(f'Os argumentos precisam ser do tipo int ou float')
    elif a <= 0 or b <= 0:
        raise ValueError(f'Não é possível multiplicar por zero ou negativo')
    elif type(a) in TIPOS and type(b) in TIPOS:
        return a * b