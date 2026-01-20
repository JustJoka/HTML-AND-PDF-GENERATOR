def gerar_html(resumo):
    html = f"""
    <html>
    <head>
        <title>Relatório Automático</title>
    </head>
    <body>
        <h1>Relatório de Vendas</h1>

        <p>Total de registros: {resumo['total_registros']}</p>
        <p>Media de registros: {resumo['media']:.2f}</p>
        <p>Máxima de registros: {resumo['maximo']}</p>
        <p>Minima de registros: {resumo['minimo']}</p>


        <h2>Gráfico<h2>

        <img src="grafico.png" width=500>
        <p><strong>Resumo Automático</strong><br>
        Observa-se variações nas vendas ao longo dos meses</p>
    </body>
    </html>
"""
    
    with open("output/relatorio.html", "w", encoding="utf-8") as f:
        f.write(html)
