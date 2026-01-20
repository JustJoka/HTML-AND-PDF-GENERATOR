from src.analise import analisar_dados
from src.grafico import gerar_grafico
from src.relatorio import gerar_html
from src.pdf import gerar_pdf

df, resumo = analisar_dados(
    r"C:\CODEVERSO\PYTHON PROJECTS\PDF AND HTML GENERATOR\data\dados.csv"
)

gerar_grafico(df)
gerar_html(resumo)
gerar_pdf(resumo)


print("Relatório HTML e PDF gerado com sucesso")