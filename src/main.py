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

def test_graph(graph):
    print(f'Seguidores da Helena: {graph.get_number_of_users_followers_by_user("helena42")}')
    print(f'Pessoas que a Helena segue: {graph.get_number_of_users_following_by_user("helena42")}')
    print(f'Ordem dos stories da Helena: {graph.get_order_stories("helena42")}')
    print(f'Top influences: {graph.get_top_influencers(5)}')
    print(f'Caminho de Helena até Isadora: {graph.get_path("helena42", "isadora45")}')

def main():
    graph = create_graph()

    test_graph(graph)

if __name__ == '__main__':
    main()