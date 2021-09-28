import csv
from models import Graph

def create_graph():
    """
    Funcao que faz a leitura dos arquivos csv's e cria o grafo a partir desses dados
    """
    graph = Graph()

    with open('data/usuarios.csv') as csvfile:
        reader = csv.reader(csvfile)

        for name, username in reader:
            graph.users = name, username
    
    with open('data/conexoes.csv') as csvfile:
        reader = csv.reader(csvfile)

        for username, following, weight in reader:
            graph.connections = username, following, weight
    
    return graph