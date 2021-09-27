import unittest
from main import create_graph

class GraphTests(unittest.TestCase):
    def setUp(self):
        self.graph = create_graph()
    
    def test_number_of_followers(self):
        self.assertEqual(self.graph.get_number_of_users_followers_by_user("helena42"), 18)
    
    def test_number_of_following(self):
        self.assertEqual(self.graph.get_number_of_users_following_by_user("helena42"), 16)
    
    def test_stories(self):
        stories_in_order = ['ana_julia22', 'pietro33', 'alice43', 'ana_clara30', 'calebe49', 'caua11', 'davi48', 'gustavo16', 'heloisa37', 'lavinia36','mariana5', 'matheus6', 'melissa42', 'nicolas4', 'rafael38', 'sophia31']
        
        self.assertEqual(self.graph.get_order_stories("helena42"), stories_in_order)
    
    def test_top_influences(self):
        top_influencers = {'maria_alice19': 24, 'miguel1': 22, 'isis3': 22, 'alice43': 22, 'henrique12': 21}

        self.assertEqual(self.graph.get_top_influencers(5), top_influencers)
    
    def test_path(self):
        path = 'helena42 -> ana_clara30 -> isadora45'

        self.assertEqual(self.graph.get_path("helena42", "isadora45"), path)

if __name__ == "__main__":
    unittest.main()