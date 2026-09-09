

TIPOS = [int, float]
def calcular_imc(altura, peso, nome):
    if type(altura) not in TIPOS or type(peso) not in TIPOS:
        raise TypeError()

    imc = peso / (altura*altura)

    if imc < 18.5:
        classificação = 'Abaixo do peso'
    elif imc >= 18.5 and imc <= 24.9:
        classificação = 'Peso normal'
    elif imc >= 25 and imc <= 29.9:
        classificação = 'Sobrepeso'
    elif imc >= 30 and imc <= 34.9:
        classificação = 'Obesidade grau I'
    elif imc >= 35 and imc <= 39.9:
        classificação = 'Obesidade grau II'
    elif imc >= 40:
        classificação = 'Obesidade grau III'

    return f'Olá {nome}, a classificação do seu imc é {classificação}'