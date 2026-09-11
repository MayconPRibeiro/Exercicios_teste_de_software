import pytest
from Calculadora_REFACTOR import calculadora_desconto

def test_compra_100_desconto_0():
    assert calculadora_desconto(100) == 100

def test_compra_101_desconto_10():
    assert calculadora_desconto(101) == 90.9

def test_compra_500_desconto_10():
    assert calculadora_desconto(500) == 450

def test_compra_501_desconto_20():
    assert calculadora_desconto(501) == 400.8

def test_compra_1000_desconto_20():
    assert calculadora_desconto(1000) == 800

def test_compra_zero():
    with pytest.raises(ValueError):
        calculadora_desconto(0)

def test_compra_negativa():
    with pytest.raises(ValueError):
        calculadora_desconto(-200)