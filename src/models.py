class Edge:
    """
    Classe que representa as conexoes entre os nos (aresta)
    """
    def __init__(self, weight, destiny):
        """
        Metodo construtor da classe
        """
        self.weight = weight
        self.destiny = destiny

    def __repr__(self):
        """
        Sobrescrita do metodo __repr__ que representa a classe como uma string
        """
        return f'{self.destiny.username}: {self.weight}'

class Node:
    """
    Classe que representa os nos (usuarios da rede)
    """
    def __init__(self, name, username):
        """
        Metodo construtor da classe
        """
        self.name = name
        self.username = username
        self.following = {}
        self._followers = {}
        self.color = 'white'
        self.parent = None
    
    def __repr__(self):
        """
        Sobrescrita do metodo __repr__ que representa a classe como uma string
        """
        return f'{self.name}: {self.username}'
    
    @property
    def connections(self):
        """
        Metodo que retorna os usuarios que este no (usuario) segue
        """
        return self.following
    
    @connections.setter
    def connections(self, data):
        """
        Metodo que adiciona uma conexao com peso (1 = amigo comum, 2 = melhor amigo). Se a conexao ja existir, apenas atualiza o peso
        """
        weight, node = data

        if self.following.get(node.username):
            edge = self.following.get(node.username)

            edge.weight = weight
        else:
            self.following[node.username] = Edge(weight, node)
    
    @property
    def followers(self):
        return self._followers

    @followers.setter
    def followers(self, node):
        """
        Metodo que adiciona um seguidor
        """
        self.followers[node.username] = node
    
    def get_number_of_users_following(self):
        """
        Metodo que retorna o numero de usuarios que este no (usuario) segue
        """
        return len(self.following)
    
    def get_number_of_users_followers(self):
        """
        Metodo que retorna o numero de usuarios seguidores deste no (usuario)
        """
        return len(self.followers)
    
    def get_following_by_username(self, username):
        """
        Metodo que retorna um usuario que este usuario siga a partir do username 
        """
        return self.following.get(username)
    
    def get_followers_by_username(self, username):
        """
        Metodo que retorna um usuario que siga este usuario a partir do username
        """
        return self.followers.get(username)

class Graph:
    """
    Classe que representa o grado (rede)
    """
    def __init__(self):
        """
        Metodo construtor da classe
        """
        self.nodes = {}


    @property
    def users(self):
        """
        Metodo que retorna os usuarios
        """
        return self.nodes

    @users.setter
    def users(self, data):
        """
        Metodo que adiciona um usuario a rede
        """
        name, username = data

        if not self.get_user_by_username(username):
            self.nodes[username] = Node(name, username)

        return self.get_user_by_username(username)

    @property
    def connections(self):
        return {username: user.connections for username, user in self.users.items()}
    
    @connections.setter
    def connections(self, data):
        """
        Metodo que adiciona uma conexao a rede
        """
        origin_username, destiny_username, weight = data

        if self.get_user_by_username(origin_username) and self.get_user_by_username(destiny_username):
            origin = self.get_user_by_username(origin_username)

            destiny = self.get_user_by_username(destiny_username)

            origin.connections = weight, destiny

            destiny.followers = origin
    
    def get_user_by_username(self, username):
        """
        Metodo que retorna o usuario pelo username
        """
        return self.nodes.get(username)
    
    def get_number_of_users_following_by_user(self, username):
        """
        Metodo que retorna pelo username o numero de usuarios seguidos por um usuario
        """
        return len(self.get_user_by_username(username).connections)
    
    def get_number_of_users_followers_by_user(self, username):
        """
        Metodo que retorna pelo username o numero de usuarios seguidores de um usuario
        """
        return len(self.get_user_by_username(username).followers)
    
    def get_order_stories(self, username):
        """
        Metodo que retorna pelo username os stories ordenados de um usuario
        """
        return [edge.destiny.username for edge in self.merge_sort('stories', username)]

    def get_top_influencers(self, k):
        """
        Metodo que retorna os k usuarios mais seguidos da rede
        """
        return {influencer.username: influencer.get_number_of_users_followers() for influencer in self.merge_sort('top')[:k]}

    def get_path(self, username_1, username_2):
        """
        Metodo que retorna o caminho entre dois usuarios na rede
        """
        self.breadth_first_search(username_1, username_2)

        path = ''

        node = self.get_user_by_username(username_2)

        while node:
            if not path:
                path = node.username
            else:
                path = f'{node.username} -> {path}'

            node = node.parent
        
        return path

    def merge_sort(self, method, username=None, list_to_sort=None):
        """
        Metodo que ordena os usuario a partir do Merge Sort
        """
        if not list_to_sort:
            if method == 'stories':
                user = self.get_user_by_username(username)

                following = user.connections

                list_to_sort = list(following.values())
            else:
                # method == 'top'
                list_to_sort = list(self.nodes.values())

        if len(list_to_sort) == 1:
            return list_to_sort
        
        middle = len(list_to_sort) // 2

        left = self.merge_sort(method, username, list_to_sort[:middle])
        
        right = self.merge_sort(method, username, list_to_sort[middle:])

        return self.merge(method, username, left, right)

    def merge(self, method, username, left, right):
        """
        Metodo auxiliar do Merge Sort que une as sublistas
        """
        user = self.get_user_by_username(username)

        list_sorted = []

        while len(left) > 0 and len(right) > 0:
            if method == 'stories':
                user_left = user.get_following_by_username(left[0].destiny.username)

                user_right = user.get_following_by_username(right[0].destiny.username)

                weight_left = user_left.weight

                weight_right = user_right.weight
            
                # left: best friend
                # right: friend
                if weight_left > weight_right:
                    list_sorted.append(left.pop(0))
                elif weight_left == weight_right:
                    if left[0].destiny.username < right[0].destiny.username:
                        list_sorted.append(left.pop(0))
                    else:
                        list_sorted.append(right.pop(0))
                else:
                    list_sorted.append(right.pop(0))
            else:
                # method: 'top'
                number_of_users_followers_left = self.get_number_of_users_followers_by_user(left[0].username)

                number_of_users_followers_right = self.get_number_of_users_followers_by_user(right[0].username)

                if number_of_users_followers_left > number_of_users_followers_right:
                    list_sorted.append(left.pop(0))
                else:
                    list_sorted.append(right.pop(0))
        
        while len(left) > 0:
            list_sorted.append(left.pop(0))
        
        while len(right) > 0:
            list_sorted.append(right.pop(0))

        return list_sorted
    
    def breadth_first_search(self, username1, username2):
        """
        Metodo que faz a Busca em Largura para encontrar o caminho entre dois usuarios
        """
        root = self.get_user_by_username(username1)

        root.color = 'gray'

        queue = [root]

        while queue:
            node = queue.pop(0)

            list_of_adjacent = [edge.destiny for edge in list(node.connections.values())]

            for adjacent in list_of_adjacent:
                if adjacent.color == 'white':
                    adjacent.color = 'gray'
                    adjacent.parent = node
                    queue.append(adjacent)

                if adjacent.username == username2:
                    queue = []
            
            node.color = 'black'