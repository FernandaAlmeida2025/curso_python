from flask import Flask, request, render_template_string
import pandas as pd
import sqlite3
import plotly.express as px
import plotly.io as pio
import random

#configura o plotly para abrir os arquivos no navegador por padrão
pio.renderers.default = "browser"

#carregar o drinks.csv
df = pd.read_csv("C:/Users/noturno/Desktop/Fernanda Almeida - Python/Sistema/drinks.csv")
#df_avengers = pd.read_csv("avengers.csv")

#cria o banco de dados em sql e popular com os dados do arquivo csv
conn = sqlite3.connect("C:/Users/noturno/Desktop/Fernanda Almeida - Python/Sistema/consumo_alcool.db")
df.to_sql("drinks", conn, if_exists="replace", index=False)
#df_avengers.to_sql("Vingadores", conn, if_exists="replace", index=False)
conn.commit()
conn.close()

#incia o flask
app = Flask(__name__)

html_template = '''
    <h1>Dashboard - Consumo de Alcool</h1>
    <h2> Parte 01 </h2>
        <ul>
            <li> <a href="/grafico1"> Top 10 paises com maior consumo de alcool </a> </li>
            <li> <a href="/grafico2"> Média de consumo por tipo de bebida </a> </li>
            <li> <a href="/grafico3"> Consumo total por região </a> </li>
            <li> <a href="/grafico4"> Comparativo entre os tipos de bebidas </a> </li>
            <li> <a href="/pais?nome=Brazil"> Insight por pais (ex: Brazil) </a> </li>
        </ul>
    <h2> Parte 02 </h2>
        <ul>
            <li><a href="/comparar"> Comparar </a></li>
            <li><a href="/upload_avengers"> Upload do CSV </a></li>
            <li><a href="/apagar_avengers"> Apagar Tabela Avengers </a></li>
            <li><a href="/atribuir_paises_avengers"> Atribuir Paises </a></li>
            <li><a href="/avengers_vs_drinks"> V.A.A (Vingadores Alcolicos Anonimos) </a></li>
        </ul>

    '''

# rota inicial com o links para os graficos
@app.route('/')
def index():
    return render_template_string(html_template)

@app.route('/grafico1')
def grafico1():
    conn = sqlite3.connect("C:/Users/noturno/Desktop/Fernanda Almeida - Python/Sistema/consumo_alcool.db")
    df = pd.read_sql_query("""
    SELECT country, total_litres_of_pure_alcohol
    FROM drinks
    ORDER BY total_litres_of_pure_alcohol DESC
    LIMIT 10
    """, conn)
    conn.close()
    fig = px.bar(
        df,
        x="country",
        y="total_litres_of_pure_alcohol",
        title="Top 10 paises com maior consumo de Alcool"
    )
    return fig.to_html()

# media do consumo por tipo global
@app.route('/grafico2')
def grafico2():
    conn = sqlite3.connect("C:/Users/noturno/Desktop/Fernanda Almeida - Python/Sistema/consumo_alcool.db")
    df = pd.read_sql_query("SELECT AVG(beer_servings) AS cerveja, AVG(spirit_servings) AS destilados, AVG(wine_servings) AS vinhos FROM drinks", conn)
    conn.close()
    df_melted = df.melt(var_name="Bebidas", value_name="Média de Porções")
    fig = px.bar(df_melted, x="Bebidas", y="Média de Porções", title="Media de consumo global por tipo")
    return fig.to_html()

@app.route('/grafico3')
def grafico3():
        #define grupos de paises por região (simulando)
        regioes = {
             "Europa": ["France","Germany","Italy","Spain","portugal","UK"],
             "Asia": ["China", "Japan", "India", "Thailand"],
             "Africa": ["Angola","Nigeria","Egypt","Algeria"],
             "Americas": ["USA","Brazil","Canada","Argentina","Mexico"]
        }
        dados = []
        conn = sqlite3.connect("C:/Users/noturno/Desktop/Fernanda Almeida - Python/Sistema/consumo_alcool.db")
        for regiao, paises in regioes.items(): 
             placeholders = ",".join([f"'{p}'" for p in paises])
             query = f"""
                SELECT SUM(total_Litres_of_pure_alcohol) as total
                drinks WHERE country IN ({placeholders})
                """
             total = pd.read_sql_query(query, conn)[0] or 0
             dados.append({"Região": regiao, "Consumo Total":total})

        conn.close()
        df_regioes = pd.DataFrame(dados)
        fig = px.pie(df-regioes, names="Região", values="Consumo Total", title="Consumo Total por região do mundo")
        return fig.to_html() + "<br/><a href='/'>Voltar ao Inicio</a>"

@app.route("/grafico4")
def grafico4():
     conn = sqlite3.connect("C:/Users/noturno/Desktop/Fernanda Almeida - Python/Sistema/consumo_alcool.db")
     df = pd.read_sql_query("SELEC beer_servings, spirit_servings, wine_servings FROM drinks", conn) 
     conn.close()
     medias = df.mean().reset_index()
     medias.columns = ["Tipo", "Média"]
     fig = px.pie(medias, names="Tipo", values="Media",)
     title = ("Proporção média entre tipos de bebidas")
     return fig.to_html() + '<br><a href="/">Voltar ao inicio</a>'





# inicia o servidor flask
if __name__ == "__main__":
    app.run(debug=True)

