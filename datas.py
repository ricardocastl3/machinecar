
from imports import *

datas = pd.read_csv("car_prices.csv").drop(columns=["Unnamed: 0"], axis=1)
a_names = {
    "mileage_per_year":"milhas_por_ano",
    "model_year":"ano_modelo",
    "price":"preco",
    "sold":"vendido"
}
datas = datas.rename(columns=a_names)

current_year = datetime.today().year
datas["idade_modelo"] = current_year - datas.ano_modelo
datas["milhas_por_hora"] = datas.milhas_por_ano * 19094

datas = datas.drop(columns=["milhas_por_ano","ano_modelo"], axis=1)

x = datas.drop(columns=["vendido"])
y = datas.vendido
