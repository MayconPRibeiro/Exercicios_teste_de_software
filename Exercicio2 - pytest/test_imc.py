import pytest
from imc import calcular_imc

def test_altura_TypeError():
    with pytest.raises(TypeError):
        calcular_imc('b', 50, 'João')

def test_peso_TypeError():
    with pytest.raises(TypeError):
        calcular_imc(1.60, 'abc', 'Maria')

def test_peso_normal():
    assert calcular_imc(1.68, 55, 'Maycon') == 'Olá Maycon, a classificação do seu imc é Peso normal'

def test_abaixo_do_peso():
    assert calcular_imc(1.70, 50, 'Ana') == 'Olá Ana, a classificação do seu imc é Abaixo do peso'

def test_sobrepeso():
    assert calcular_imc(1.70, 78, 'Carlos') == 'Olá Carlos, a classificação do seu imc é Sobrepeso'

def test_obesidade_grau_1():
    assert calcular_imc(1.70, 93, 'Pedro') == 'Olá Pedro, a classificação do seu imc é Obesidade grau I'

def test_obesidade_grau_2():
    assert calcular_imc(1.70, 107, 'Lucas') == 'Olá Lucas, a classificação do seu imc é Obesidade grau II'

def test_obesidade_grau_3():
    assert calcular_imc(1.70, 120, 'Bruno') == 'Olá Bruno, a classificação do seu imc é Obesidade grau III'