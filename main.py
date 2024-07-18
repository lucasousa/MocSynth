import json
from src.gerador import Gerador
from datetime import datetime as dt, timedelta as td


# Abertura do arquivo contendo os provedores e microsserviços
with open("resultDataEdit.json", "r", encoding="utf-8") as data_file:
    app = json.load(data_file)

# Criação de datas
hoje = dt.now()
tresMeses = hoje + td(days=15)

# Criação do objeto Gerador
gerador = Gerador(
    result=app[0],
    date_initial=hoje,
    date_final=tresMeses,
    intervalo=10,
    case=4,
    # ms_selecionados=[0,3]
    requisitos_selecionados=[2,3]
)

# Geração de dados
gerador.iniciar()

# Casos:
#       Caso 1: Melhor caso taxa de disponibilidade, custo e tempo de resposta estão sendo atendidas por absolutamente todos os fornecedores
#       Caso 2: Caso oposto ao 1.
#       Caso 3: Gerados aleatóriamente.
#       Caso 4: Selecionar 1 ou mais requisitos (disponibilidade, custo e tempo de resposta) que não serão atendidos
#       Caso 5: Selecionar 1 ou mais microsseviços que não serão atendidos