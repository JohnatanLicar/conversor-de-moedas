from forex_python.converter import CurrencyRates

def converter_moeda(valor, moeda_origem, moeda_destino):
    conversor = CurrencyRates()
    resultado = conversor.convert(moeda_origem, moeda_destino, valor)
    return resultado

valor = float(input("Digite o valor a ser convertido: "))
moeda_origem = input("Digite a moeda de origem (exemplo: USD, EUR, BRL): ").upper()
moeda_destino = input("Digite a moeda de destino (exemplo: USD, EUR, BRL): ").upper()

resultado = converter_moeda(valor, moeda_origem, moeda_destino)
print(f"{valor} {moeda_origem} = {resultado} {moeda_destino}")
