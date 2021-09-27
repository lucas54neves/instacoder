from models import Graph
import csv

def create_graph():
    graph = Graph()

    with open('data/usuarios.csv') as csvfile:
        reader = csv.reader(csvfile)

        for name, username in reader:
            graph.add_user(name, username)
    
    with open('data/conexoes.csv') as csvfile:
        reader = csv.reader(csvfile)

        for username, following, weight in reader:
            graph.add_connection(username, following, weight)
    
    return graph
'''
quantidade_seguidores('helena42')
    --> Seguidores da Helena: 18
quantidade_seguindo('helena42')
    --> Pessoas que a Helena segue: 16
stories('helena42')
    --> Ordem dos stories da Helena: ['ana_julia22', 'pietro33', 'alice43', 'ana_clara30', 'calebe49', 'caua11', 'davi48', 'gustavo16', 'heloisa37', 'lavinia36','mariana5', 'matheus6', 'melissa42', 'nicolas4', 'rafael38', 'sophia31']
top_influencers(5)
    --> Top influences: {'maria_alice19': 24, 'henrique12': 22, 'miguel1': 22, 'isis3': 22, 'alice43': 22}
encontra_caminho('helena42', 'isadora45')
    --> Caminho de Helena até Isadora: helena42 -> ana_clara30 -> isadora45
'''
def test_graph(graph):
    print(f'Seguidores da Helena: {graph.get_number_of_users_followers_by_user("helena42")}')
    print(f'Pessoas que a Helena segue: {graph.get_number_of_users_following_by_user("helena42")}')
    print(f'Ordem dos stories da Helena: {graph.get_order_stories("helena42")}')
    print(f'Top influences: {graph.get_top_influencers(5)}')
    print(f'Caminho de Helena até Isadora: {graph.get_path("helena42", "isadora45")}')

def main():
    graph = create_graph()

    test_graph(graph)

main()