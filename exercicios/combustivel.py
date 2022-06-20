class BombaCombustivel:
    def __init__(self, tipo_combustivel: str, valor_litro: float, quantidade_combustivel: float):
        self.valor_litro = valor_litro
        self.tipo_combustivel = tipo_combustivel
        self.quantidade_combustivel = quantidade_combustivel

    def abastecer_por_valor(self, valor: float):
        litros_abastecidos = valor / self.valor_litro
        self.quantidade_combustivel -= litros_abastecidos
        print(f'Foram abastecidos {litros_abastecidos:.2f} Litros a um Valor de R$ {valor:.2f}')
        print(f'Sobraram na Bomba {self.quantidade_combustivel:.2f} litros')


bomba = BombaCombustivel('Gasolina', 4.59, 100.0)

# bomba.abastecer_por_valor(100)
bomba.abastecer_por_valor(4.59)
