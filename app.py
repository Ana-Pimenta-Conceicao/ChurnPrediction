from flask import Flask, render_template, request
import plotly.express as px
import plotly.io as pio
import pandas as pd
import numpy as np

app = Flask(__name__)

# Gerar dados de exemplo
np.random.seed(42)
num_clients = 100
data = {
    'idade': np.random.randint(18, 70, num_clients),
    'salario': np.random.randint(1000, 5000, num_clients),
    'tempo': np.random.randint(1, 10, num_clients),
    'gasto': np.random.randint(100, 1000, num_clients),
    'churn': np.random.randint(0, 2, num_clients)
}
df = pd.DataFrame(data)

@app.route('/', methods=['GET', 'POST'])
def index():
    # Criar gráficos
    idade_bins = [0, 25, 35, 45, 55, 65, 75]
    idade_labels = ['<25', '25-34', '35-44', '45-54', '55-64', '65+']
    df['idade_group'] = pd.cut(df['idade'], bins=idade_bins, labels=idade_labels)
    idade_churn = df.groupby('idade_group')['churn'].mean().reset_index()
    fig_idade = px.bar(idade_churn, x='idade_group', y='churn', title='Porcentagem de Churn por Faixa Etária')

    salario_bins = [0, 2000, 3000, 4000, 5000]
    salario_labels = ['<2000', '2000-2999', '3000-3999', '4000-4999']
    df['salario_group'] = pd.cut(df['salario'], bins=salario_bins, labels=salario_labels)
    salary_lifetime = df.groupby('salario_group')['tempo'].mean().reset_index()
    fig_salario = px.bar(salary_lifetime, x='salario_group', y='tempo', title='Tempo Médio como Cliente por Faixa Salarial')

    gasto_bins = [0, 200, 400, 600, 800, 1000]
    gasto_labels = ['<200', '200-399', '400-599', '600-799', '800+']
    df['gasto_group'] = pd.cut(df['gasto'], bins=gasto_bins, labels=gasto_labels)
    gasto_churn = df.groupby('gasto_group')['churn'].mean().reset_index()
    fig_gasto = px.bar(gasto_churn, x='gasto_group', y='churn', title='Porcentagem de Churn por Faixa de Gasto')

    # Converte gráficos para HTML
    graficos_html = pio.to_html(fig_idade, full_html=False) + pio.to_html(fig_salario, full_html=False) + pio.to_html(fig_gasto, full_html=False)

    # Tabela de dados
    table_html = df.to_html(classes='table-auto w-ful l bg-white shadow-md rounded-lg text-center', index=False)

    resultado = ''  # Inicializa resultado como uma string vazia
    if request.method == 'POST':
        # Coletar dados do formulário
        idade = float(request.form['idade'])
        salario = float(request.form['salario'])
        tempo = float(request.form['tempo'])
        gasto = float(request.form['gasto'])
        
        # Lógica para previsão de churn (exemplo simples)
        churn_prob = (idade * 0.01 + salario * 0.001 + tempo * 0.02 + gasto * 0.005) % 1
        
        resultado = f'Probabilidade de churn: {churn_prob:.2%}'

    # Renderizar página
    return render_template('index.html', graficos_html=graficos_html, table_html=table_html, resultado=resultado)

if __name__ == '__main__':
    app.run(debug=True)