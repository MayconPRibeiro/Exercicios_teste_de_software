from src.Funcao import Calcular_aprovacao


def test_aluno_reprovado():
    aprovacao = Calcular_aprovacao(
        nota_minima=5,
        nota_aprovacao=7
    )

    notas = [2, 3, 4]

    media = aprovacao.calcular_media(notas)

    assert aprovacao.classificar_aluno(media) == 'Reprovado'


def test_aluno_recuperacao():
    aprovacao = Calcular_aprovacao(
        nota_minima=5,
        nota_aprovacao=7
    )

    notas = [5, 6, 6]

    media = aprovacao.calcular_media(notas)

    assert aprovacao.classificar_aluno(media) == 'Recuperação'


def test_aluno_aprovado():
    aprovacao = Calcular_aprovacao(
        nota_minima=5,
        nota_aprovacao=7
    )

    notas = [7, 8, 9]

    media = aprovacao.calcular_media(notas)

    assert aprovacao.classificar_aluno(media) == 'Aprovado'