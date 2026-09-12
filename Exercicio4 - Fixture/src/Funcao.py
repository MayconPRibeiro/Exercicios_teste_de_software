class Calcular_aprovacao():
    def __init__(self, nota_minima, nota_aprovacao):
        self.nota_minima = nota_minima
        self.nota_aprovacao = nota_aprovacao

    def calcular_media(self, notas):
        return sum(notas) / len(notas)

    def classificar_aluno(self, media):
        if media < self.nota_minima:
            return 'Reprovado'
        if media >= self.nota_aprovacao:
            return 'Aprovado'
        return 'Recuperação'