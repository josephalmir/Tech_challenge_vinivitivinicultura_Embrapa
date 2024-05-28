import requests
from io import StringIO

def clean_value(value):
    if value is None:
        return 'vazio'
    elif isinstance(value, str):
        return value.strip()
    else:
        return str(value)

def fetch_data(url):
    response = requests.get(url)
    response.raise_for_status()  # Levanta um erro se a requisição falhar

    # Lê os dados CSV da resposta
    csv_data = StringIO(response.text)

    # Extrai os cabeçalhos do CSV e divide-os
    header = next(csv_data).strip().split(';')

    # Converte os dados para uma lista de dicionários
    data = []
    for line in csv_data:
        # Dividir a linha nos pontos e vírgulas ";" e limpar os valores
        values = [clean_value(value) for value in line.strip().split(';')]
        # Ignorar linhas vazias ou com valores nulos em todas as colunas
        if any(values):
            row = dict(zip(header, values))  # Combina os valores com os cabeçalhos
            data.append(row)

    return data
