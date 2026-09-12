import pytest
from src.Funcao import Calcular_aprovacao

@pytest.fixture
def aprovacao():
    return Calcular_aprovacao(nota_minima=5, nota_aprovacao=7)

def test_aluno_reprovado(aprovacao):
    notas = [2, 3, 4]

    media = aprovacao.calcular_media(notas)

    assert aprovacao.classificar_aluno(media) == 'Reprovado'


def test_aluno_recuperacao(aprovacao):
    notas = [5, 6, 6]

    media = aprovacao.calcular_media(notas)

    assert aprovacao.classificar_aluno(media) == 'Recuperação'


def test_aluno_aprovado(aprovacao):
    notas = [7, 8, 9]

    media = aprovacao.calcular_media(notas)

    assert aprovacao.classificar_aluno(media) == 'Aprovado'
