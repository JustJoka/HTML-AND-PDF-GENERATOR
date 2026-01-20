import pandas as pd

def analisar_dados(caminho):
    with open(caminho, "r", encoding="utf-8") as f:
        print(f.read())
        
    df = pd.read_csv(caminho)

    resumo = {
        "total_registros": len(df),
        "media": df["vendas"].mean(),
        "maximo": df["vendas"].max(),
        "minimo": df["vendas"].min()
    }

    return df, resumo