import pandas as pd

def carregar_dados(caminho_limpo):
    try:
        df = pd.read_csv(caminho_limpo)
        # Aqui simulamos a carga final (ex: salvando a versão "Gold" para o BI)
        print(f"Carregando {len(df)} registros limpos para a camada final...")
        print(df.head())
        print("Carga finalizada com sucesso!")
    except FileNotFoundError:
        print("Erro: O arquivo limpo não foi encontrado. Rode o transform.py primeiro.")

if __name__ == "__main__":
    carregar_dados('data/vendas_limpas.csv')