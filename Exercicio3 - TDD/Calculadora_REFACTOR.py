def calculadora_desconto(venda):
    if venda <= 0:
        raise ValueError()
    if venda <= 100:
        return venda
    if venda <= 500:
        return venda*0.90
    return venda*0.80