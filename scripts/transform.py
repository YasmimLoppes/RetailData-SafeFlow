import pandas as pd

def limpar_dados_vendas(caminho_bruto, caminho_limpo):
    # Carregando os dados
    df = pd.read_csv(caminho_bruto)
    
    print(f"--- Iniciando Transformação. Registros originais: {len(df)} ---")

    # 1. Removendo duplicatas (aquelas 'duas calças jeans iguais' do quiz)
    df_limpo = df.drop_duplicates().copy()
    print(f"Removido duplicatas. Registros restantes: {len(df_limpo)}")
    
    # 2. Corrigindo preços: removendo negativos e preenchendo vazios com a média
    # ANTES DE LIMPAR, VAMOS TESTAR SE HÁ ERROS (Robustez!)
    precos_negativos = df_limpo[df_limpo['Preco_Venda'] < 0]
    if len(precos_negativos) > 0:
        print(f"⚠️ Alerta: Encontrados {len(precos_negativos)} preços negativos. Tratando...")
    
    precos_vazios = df_limpo['Preco_Venda'].isna().sum()
    if precos_vazios > 0:
        print(f"⚠️ Alerta: Encontrados {precos_vazios} preços vazios. Preenchendo com a média...")

    # Aplicação da limpeza
    df_limpo = df_limpo[df_limpo['Preco_Venda'] > 0].copy()
    media_preco = df_limpo['Preco_Venda'].mean()
    df_limpo['Preco_Venda'] = df_limpo['Preco_Venda'].fillna(media_preco)
    
    # --- VALIDAÇÃO FINAL (ROBUSTEZ SÊNIOR!) ---
    # Teste 1: Preço é sempre positivo?
    assert (df_limpo['Preco_Venda'] > 0).all(), "❌ ERRO DE DADOS: Ainda existem preços negativos!"
    
    # Teste 2: O ID do Pedido é Único (já que tiramos duplicatas de registro inteiro, talvez haja IDs iguais com produtos diferentes?)
    contagem_ids = df_limpo['ID_Pedido'].value_counts()
    if contagem_ids.max() > 1:
        print(f"⚠️ Alerta: Existem IDs de Pedido duplicados ({contagem_ids[contagem_ids > 1].index.tolist()}). Verifique a integridade.")

    # Salvando o resultado para a próxima etapa do pipeline
    df_limpo.to_csv(caminho_limpo, index=False)
    print(f"✅ Sucesso! Dados limpos e validados salvos em: {caminho_limpo}")
    print(f"--- Transformação concluída. Registros finais: {len(df_limpo)} ---")

if __name__ == "__main__":
    limpar_dados_vendas('data/vendas_brutas.csv', 'data/vendas_limpas.csv')