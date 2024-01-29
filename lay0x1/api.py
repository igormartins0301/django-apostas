from ninja import Router, Query
from transform.feature_engineering import feature_engineering
import pandas as pd
import os
import pickle

current_directory = os.path.dirname(os.path.realpath(__file__))
root_directory = os.path.dirname(current_directory)
model_path_1 = os.path.join(root_directory, 'model', 'modelo_lgbm.pkl')
model_path_2 = os.path.join(root_directory, 'model', 'modelo_1x0.pkl')
model_path_1

router = Router()


#Já utiliza validação de tipagem com pydantic
@router.get("/")
def predict(
    request,
    Odd_H: float = Query(..., description='Odd_H description'),
    Odd_D: float = Query(..., description='Odd_D description'),
    Odd_A: float = Query(..., description='Odd_A description'),
    Odd_Over25: float = Query(..., description='Odd_Over25 description'),
    Odd_Under25: float = Query(..., description='Odd_Under25 description')
):
    # Crie um DataFrame temporário com os dados de entrada
    input_data = pd.DataFrame(
        [[Odd_H, Odd_D, Odd_A, Odd_Over25, Odd_Under25]],
        columns=["Odd_H", "Odd_D", "Odd_A", "Odd_Over25", "Odd_Under25"],
    )

    # Realize a engenharia de recursos
    input_data = feature_engineering(input_data)

    # Carregue o modelo
    with open(model_path_1, "rb") as file:
        model = pickle.load(file)

    # Selecione as características necessárias para a previsão
    features = input_data.columns

    # Faça a previsão
    prediction = model.predict_proba(input_data)[:, 1][0]

    if prediction < 0.2:
        mensagem = "Jogo validado: Entrar Lay 0x1"
    else:
        mensagem = "Jogo inválido: não faça nada!"

    return {"prediction": prediction,
            "mensagem" : mensagem}
