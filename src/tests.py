import unittest
from main import create_graph

class GraphTests(unittest.TestCase):
    """
    Classe de testes da classe Graph
    """
    def setUp(self):
        """
        Metodo construtor da classe de teste. Cria o grafo a partir da funcao
        que faz a leitura dos arquivos csv's e cria o grafo a partir dele.
        """
        self.graph = create_graph()
    
    def test_number_of_followers(self):
        """
        Teste da quantidade de seguidores de um usuario
        """
        self.assertEqual(self.graph.get_number_of_users_followers_by_user("helena42"), 18)
    
    def test_number_of_following(self):
        """
        Teste do numero de usuarios sendo seguidos por um usuario
        """
        self.assertEqual(self.graph.get_number_of_users_following_by_user("helena42"), 16)
    
    def test_stories(self):
        """
        Teste dos stories ordenados de um usuario
        """
        stories_in_order = ['ana_julia22', 'pietro33', 'alice43', 'ana_clara30', 'calebe49', 'caua11', 'davi48', 'gustavo16', 'heloisa37', 'lavinia36','mariana5', 'matheus6', 'melissa42', 'nicolas4', 'rafael38', 'sophia31']
        
        self.assertEqual(self.graph.get_order_stories("helena42"), stories_in_order)
    
    def test_top_influences(self):
        """
        Teste dos usuarios mais seguidos
        """
        top_influencers = {'maria_alice19': 24, 'miguel1': 22, 'isis3': 22, 'alice43': 22, 'henrique12': 21}

        self.assertEqual(self.graph.get_top_influencers(5), top_influencers)
    
    def test_path(self):
        """
        Teste do caminho entre dois usuarios
        """
        path = 'helena42 -> ana_clara30 -> isadora45'

        self.assertEqual(self.graph.get_path("helena42", "isadora45"), path)

if __name__ == "__main__":
    unittest.main()