from flask_restful import Resource
from flask import jsonify
from .utils import fetch_data, clean_value
from .auth import token_required
import requests
from io import StringIO

class Producao(Resource):
    #@token_required
    def get(self):
        data = fetch_data('http://vitibrasil.cnpuv.embrapa.br/download/Producao.csv')
        return jsonify(data)

class Processamento(Resource):
    #@token_required
    def get(self):
        response = requests.get('http://vitibrasil.cnpuv.embrapa.br/download/ProcessaViniferas.csv')
        response.raise_for_status()  # Levanta um erro se a requisição falhar

        # Lê os dados CSV da resposta
        csv_data = StringIO(response.text)

        # Extrai os cabeçalhos do CSV e divide-os
        header = next(csv_data).strip().split('\t')

        # Converte os dados para uma lista de dicionários
        data = []
        for line in csv_data:
            # Dividir a linha nos pontos e vírgulas ";" e limpar os valores
            values = [clean_value(value) for value in line.strip().split('\t')]
            # Ignorar linhas vazias ou com valores nulos em todas as colunas
            if any(values):
                row = dict(zip(header, values))  # Combina os valores com os cabeçalhos
                data.append(row)

        return jsonify(data)

class Comercializacao(Resource):
    #@token_required
    def get(self):
        data = fetch_data('http://vitibrasil.cnpuv.embrapa.br/download/Comercio.csv')
        return jsonify(data)

class Importacao(Resource):
    #@token_required
    def get(self):
        data = fetch_data('http://vitibrasil.cnpuv.embrapa.br/download/ImpVinhos.csv')
        return jsonify(data)

class Exportacao(Resource):
    #@token_required
    def get(self):
        data = fetch_data('http://vitibrasil.cnpuv.embrapa.br/download/ExpVinho.csv')
        return jsonify(data)

def register_routes(api):
    api.add_resource(Producao, '/producao')
    api.add_resource(Processamento, '/processamento')
    api.add_resource(Comercializacao, '/comercializacao')
    api.add_resource(Importacao, '/importacao')
    api.add_resource(Exportacao, '/exportacao')
