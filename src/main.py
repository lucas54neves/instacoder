from utils import create_graph

def test_graph(graph):
    """
    Funcao que exibe as informacoes da rede
    """
    print(f'Seguidores da Helena: {graph.get_number_of_users_followers_by_user("helena42")}')
    print(f'Pessoas que a Helena segue: {graph.get_number_of_users_following_by_user("helena42")}')
    print(f'Ordem dos stories da Helena: {graph.get_order_stories("helena42")}')
    print(f'Top influences: {graph.get_top_influencers(5)}')
    print(f'Caminho de Helena até Isadora: {graph.get_path("helena42", "isadora45")}')

def main():
    """
    Funcao principal do projeto
    """
    graph = create_graph()

    test_graph(graph)

if __name__ == '__main__':
    main()