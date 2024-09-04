import numpy as np
from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score

def train_and_evaluate_model():
    # Carregar o conjunto de dados Iris
    data = load_iris()
    X = data.data  # Features
    y = data.target  # Labels
    
    # Dividir os dados em conjuntos de treinamento e teste
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=42)
    
    # Criar o classificador
    model = RandomForestClassifier(n_estimators=100, random_state=42)
    
    # Treinar o modelo
    model.fit(X_train, y_train)
    
    # Fazer previsões
    y_pred = model.predict(X_test)
    
    # Avaliar a precisão
    accuracy = accuracy_score(y_test, y_pred)
    print(f'Accuracy: {accuracy:.2f}')
    
    return model

def make_prediction(model, features):
    # Fazer uma previsão com o modelo treinado
    features = np.array(features).reshape(1, -1)
    prediction = model.predict(features)
    return prediction[0]

if __name__ == "__main__":
    model = train_and_evaluate_model()
    
    # Exemplo de uso do modelo para fazer uma previsão
    example_features = [5.1, 3.5, 1.4, 0.2]  # Exemplo de características (sepal_length, sepal_width, petal_length, petal_width)
    prediction = make_prediction(model, example_features)
    print(f'Predicted class: {prediction}')
