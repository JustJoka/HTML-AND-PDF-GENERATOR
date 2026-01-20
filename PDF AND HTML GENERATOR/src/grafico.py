import matplotlib.pyplot as plt


def gerar_grafico(df):
    plt.figure()
    plt.plot(df["mes"], df["vendas"])
    plt.title("Vendas do mês")
    plt.xlabel("Mês")
    plt.ylabel("Vendas")
    plt.tight_layout()
    plt.savefig("output/grafico.png")
    plt.close()