import tkinter as tk
from tkinter import messagebox
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
import numpy as np

# Criar um conjunto de dados fictício
data = {
    'Idade': [25, 45, 35, 50, 23, 60, 33, 42, 39, 27],
    'Salario': [50000, 80000, 60000, 100000, 45000, 120000, 55000, 75000, 65000, 47000],
    'TempoComoCliente': [1, 5, 3, 10, 1, 7, 4, 6, 5, 2],
    'TotalGasto': [2000, 6000, 3000, 10000, 1500, 8000, 3500, 5500, 4000, 2000],
    'Cancelou': [0, 0, 1, 0, 1, 0, 1, 0, 0, 1]  # 0 = Não cancelou, 1 = Cancelou
}

df = pd.DataFrame(data)

# Dividir o conjunto de dados em características e rótulos
X = df[['Idade', 'Salario', 'TempoComoCliente', 'TotalGasto']]
y = df['Cancelou']

# Dividir os dados em conjuntos de treinamento e teste
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=42)

# Criar e treinar o modelo
model = RandomForestClassifier(n_estimators=100, random_state=42)
model.fit(X_train, y_train)

# Função para prever o churn
def prever_churn():
    idade = int(entry_idade.get())
    salario = float(entry_salario.get())
    tempo_como_cliente = int(entry_tempo.get())
    total_gasto = float(entry_gasto.get())
    
    exemplo = np.array([[idade, salario, tempo_como_cliente, total_gasto]])
    previsao = model.predict(exemplo)
    
    if previsao[0] == 1:
        resultado = "O cliente está propenso a cancelar."
    else:
        resultado = "O cliente não está propenso a cancelar."
    
    messagebox.showinfo("Resultado da Previsão", resultado)

# Criar a interface gráfica
root = tk.Tk()
root.title("Previsão de Churn")

tk.Label(root, text="Idade:").grid(row=0, column=0)
entry_idade = tk.Entry(root)
entry_idade.grid(row=0, column=1)

tk.Label(root, text="Salário:").grid(row=1, column=0)
entry_salario = tk.Entry(root)
entry_salario.grid(row=1, column=1)

tk.Label(root, text="Tempo Como Cliente (anos):").grid(row=2, column=0)
entry_tempo = tk.Entry(root)
entry_tempo.grid(row=2, column=1)

tk.Label(root, text="Total Gasto:").grid(row=3, column=0)
entry_gasto = tk.Entry(root)
entry_gasto.grid(row=3, column=1)

tk.Button(root, text="Prever Churn", command=prever_churn).grid(row=4, columnspan=2)

root.mainloop()
