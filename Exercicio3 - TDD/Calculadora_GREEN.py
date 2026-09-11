#teste até 100, sem desconto
def calculadora_desconto(venda):
    if venda <= 100:
        return venda

#teste desconto entre 100 e 500
def calculadora_desconto(venda):
    if venda > 100 and venda <= 500:
        return venda*0.90
    elif venda <= 100:
        return venda

#teste desconto acima de 500
def calculadora_desconto(venda):
    if venda <= 100:
        return venda
    elif venda > 100 and venda <= 500:
        return venda*0.90   
    elif venda > 500:
        return venda*0.80

#teste valores negativos ou zeros
def calculadora_desconto(venda):
    if venda <= 0:
        raise ValueError()
    elif venda <= 100:
        return venda
    elif venda > 100 and venda <= 500:
        return venda*0.90   
    elif venda > 500:
        return venda*0.80