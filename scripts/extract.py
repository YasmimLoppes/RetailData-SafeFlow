import pandas as pd
import os

def extrair_dados():
    # Criando dados fictícios com os erros que sua limpeza resolve (duplicados e preços negativos)
    dados = {
        'ID_Pedido': [101, 102, 102, 103, 104],
        'Produto': ['Calça Jeans', 'Camisa Polo', 'Camisa Polo', 'Tênis', 'Short'],
        'Preco_Venda': [150.00, 89.90, 89.90, -10.00, None] # Erros para o seu transform.py tratar
    }
    
    df = pd.DataFrame(dados)
    
    # Garante que a pasta data existe
    if not os.path.exists('data'):
        os.makedirs('data')
        
    df.to_csv('data/vendas_brutas.csv', index=False)
    print("Extração concluída: Arquivo 'vendas_brutas.csv' criado em data/")

if __name__ == "__main__":
    extrair_dados()