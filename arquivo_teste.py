import pandas as pd

def carregar_dados():
    # Simulando carregamento de um CSV ou Banco de Dados
    data = {
        'id_venda': [101, 102, 103, 104, 105],
        'data': ['2023-01-15', '2023-01-16', '2023-01-16', '2023-01-17', '2023-01-17'],
        'produto': ['Notebook', 'Mouse', 'Teclado', 'Notebook', 'Monitor'],
        'quantidade': [1, 5, 2, 1, 2],
        'valor_unitario': [3500.00, 50.00, 120.00, 3500.00, 800.00]
    }
    return pd.DataFrame(data)

def transformar_dados(df):
    # Cria coluna de valor total
    df['valor_total'] = df['quantidade'] * df['valor_unitario']
    return df

def analise_faturamento(df):
    faturamento = df['valor_total'].sum()
    print(f"--- Relatório de Vendas ---")
    print(f"Faturamento Total: R$ {faturamento:.2f}")
    # print(f"Faruramento calculado com sucesso.")
    # print(f"-----------FIM-----------")
    
    # Exercicio futuro: Adicionar média por produto aqui
    return faturamento

if __name__ == "__main__":
    df_raw = carregar_dados()
    df_clean = transformar_dados(df_raw)
    analise_faturamento(df_clean)