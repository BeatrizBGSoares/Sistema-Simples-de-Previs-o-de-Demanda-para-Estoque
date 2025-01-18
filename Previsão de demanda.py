import numpy as np
import random
import datetime

class PrevisaoDemanda:
    def __init__(self):
        self.vendas_historicas = self.gerar_dados_historicos()
        
    def gerar_dados_historicos(self):

        vendas = [random.randint(100, 500) for _ in range(12)]
        print(f'Dados históricos de vendas: {vendas}')
        return vendas

    def calcular_media_movel(self, periodo=3):
        """
        Calcula a média móvel para a previsão de demanda, considerando o período fornecido.
        """
        if len(self.vendas_historicas) < periodo:
            raise ValueError("O período de previsão não pode ser maior que o número de dados históricos.")
        
        ultima_media = np.mean(self.vendas_historicas[-periodo:])
        return round(ultima_media)

    def prever_demanda_futura(self, meses=3):
        """
        Faz previsões de demanda para os próximos meses com base na média móvel.
        """
        previsoes = []
        for _ in range(meses):
            previsao = self.calcular_media_movel(periodo=3)
            previsoes.append(previsao)
            self.vendas_historicas.append(previsao)  # Simula que a previsão foi realizada
        return previsoes

    def exibir_previsao(self, meses=3):
        previsoes = self.prever_demanda_futura(meses)
        print(f'\nPrevisões de demanda para os próximos {meses} meses:')
        for i, previsao in enumerate(previsoes, 1):
            print(f'Mês {i}: {previsao} unidades')

def main():
    print("Bem-vindo ao sistema de previsão de demanda!")
    
    sistema = PrevisaoDemanda()
    
    while True:
        print("\nSelecione uma opção:")
        print("1 - Ver previsões de demanda")
        print("2 - Sair")
        
        opcao = input("Digite a opção: ")
        
        if opcao == "1":
            try:
                meses = int(input("Quantos meses deseja prever (ex: 3): "))
                sistema.exibir_previsao(meses)
            except ValueError:
                print("Por favor, insira um número válido de meses.")
        elif opcao == "2":
            print("Saindo...")
            break
        else:
            print("Opção inválida. Tente novamente.")

if __name__ == "__main__":
    main()
