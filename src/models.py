class Edge:
    """
    Classe que representa as conexoes entre os nos (aresta)
    """
    def __init__(self, weight, destiny):
        """
        Metodo construtor da classe.

        Args:
            weight (int): Peso da conexao, sendo 1 para amigo comum e 2 para
                melhores amigos
            destiny (Node): Usuario que e seguido no contexto da conexao
        """
        self.weight = weight
        self.destiny = destiny

    def __repr__(self):
        """
        Sobrescrita do metodo __repr__ que representa a classe como uma string.

        Returns:
            str: String que representa a conexao/aresta no seguinte formato
                'username do destino da conexao: peso da conexao'
        """
        return f'{self.destiny.username}: {self.weight}'

class Node:
    """
    Classe que representa os nos (usuarios da rede)
    """
    def __init__(self, name, username):
        """
        Metodo construtor da classe

        Args:
            name (str): Nome do usuario.
            username(str): Username do usuario
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

        Returns:
            str: String que representa o usuario/node no seguinte formato 'nome
                do usuario: username do usuario'
        """
        return f'{self.name}: {self.username}'
    
    @property
    def connections(self):
        """
        Metodo que retorna os usuarios que este no (usuario) segue

        Returns:
            dict: Dicionario contendo todas as conexoes/arestas do no em
                questao, sendo a chave o username do usuario seguido e o
                valor a aresta que representa a conexao
        """
        return self.following
    
    @connections.setter
    def connections(self, data):
        """
        Metodo que adiciona uma conexao com peso (1 = amigo comum, 2 = melhor
        amigo). Se a conexao ja existir, apenas atualiza o peso

        Args:
            data (int, Node): Tupla com as informacoes da conexao (peso da
                conexao e no destino da conexao)
        """
        weight, node = data

        if self.following.get(node.username):
            edge = self.following.get(node.username)

            edge.weight = weight
        else:
            self.following[node.username] = Edge(weight, node)
    
    @property
    def followers(self):
        """
        Metodo que retorna o dicionario de seguidores

        Returns:
            dict: Dicionario contendo todos os seguidores do no, sendo a chave
                o username do seguidor e o valor o proprio no seguidor
        """
        return self._followers

    @followers.setter
    def followers(self, node):
        """
        Metodo que adiciona um seguidor

        Args:
            node (Node): No seguidor
        """
        self.followers[node.username] = node
    
    def get_number_of_users_following(self):
        """
        Metodo que retorna o numero de usuarios que este no (usuario) segue

        Returns:
            int: Quantidade de usuarios que o no/usuario segue
        """
        return len(self.following)
    
    def get_number_of_users_followers(self):
        """
        Metodo que retorna o numero de usuarios seguidores deste no (usuario)

        Returns:
            int: Quantidade de usuarios seguidores do no/usuario
        """
        return len(self.followers)
    
    def get_following_by_username(self, username):
        """
        Metodo que retorna um usuario que este usuario siga a partir do username

        Args:
            username (str): Username do no/usuario que deseja buscar no
                dicionario de usuarios que o atual no/usuario segue
        
        Returns:
            Edge: A aresta que representa a conexao
        """
        return self.following.get(username)
    
    def get_followers_by_username(self, username):
        """
        Metodo que retorna um usuario que siga este usuario a partir do username

        Args:
            username (str): Username do no/usuario seguidor

        Returns:
            Node: No/Usuario seguidor
        """
        return self.followers.get(username)

class Graph:
    """
    Classe que representa o grado (rede)
    """
    def __init__(self):
        """
        Metodo construtor da classe. Dentro da classe Graph tem apenas um
        dicionario com os nos/usuarios da rede, sendo a chave o username do
        usuario e o valor o proprio no/usuario.
        """
        self.nodes = {}

    @property
    def users(self):
        """
        Metodo que retorna os usuarios.

        Returns:
            dict: Dicionario que representa os nos, sendo a chave o username do
                usuario e a chave o proprio no/username.
        """
        return self.nodes

    @users.setter
    def users(self, data):
        """
        Metodo que adiciona um usuario a rede.

        Args:
            data (str, str): Tupla com o nome e o username do usario.

        Returns:
            Node: No/Usuario adicionado.
        """
        name, username = data

        if not self.get_user_by_username(username):
            self.nodes[username] = Node(name, username)

        return self.get_user_by_username(username)

    @property
    def connections(self):
        """
        Retorna um dicionario com todas as conexoes do grafo. Sendo a chave o
        username do usuario e o valor todas as conexoes do usuario.
        
        Returns:
            dict: Dicionario com todas as conexoes do grafo. Sendo a chave o
                username do usuario e o valor todas as conexoes do usuario
        """
        return {username: user.connections for username, user in self.users.items()}
    
    @connections.setter
    def connections(self, data):
        """
        Metodo que adiciona uma conexao a rede

        Args:
            data (str, str, int): Tupla com o username do usuario que segue,
                username do usario que e seguido e peso da conexao.
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

        Returns:
            Node: Node/Usuario com o username pesquisado. 
        """
        return self.nodes.get(username)
    
    def get_number_of_users_following_by_user(self, username):
        """
        Metodo que retorna pelo username o numero de usuarios seguidos por um
        usuario

        Args:
            username (str): Username do usuario que deseja buscar a quantidade
                dos usuarios seguidos.

        Returns:
            int: Quantidade de usuarios que o usuario com username segue.
        """
        return len(self.get_user_by_username(username).connections)
    
    def get_number_of_users_followers_by_user(self, username):
        """
        Metodo que retorna pelo username o numero de usuarios seguidores de um
        usuario.

        Args:
            username (str): Username do usuario que deseja buscar a quantidade
                de usuarios seguidores.
        
        Returns:
            int: Quantidade de usuarios seguidores que segue o usuario com o
                username
        """
        return len(self.get_user_by_username(username).followers)
    
    def get_order_stories(self, username):
        """
        Metodo que retorna pelo username os stories ordenados de um usuario. A
        ordem leva em consideracao primeiro os melhores amigos e depois a ordem
        alfabetica dos usernames.

        Args:
            username (str): Username do usuario que deseja buscar a lista de
                stories.

        Returns:
            list de str: Lista com os usernames ordenados.
        """
        return [edge.destiny.username for edge in self.merge_sort('stories', username)]

    def get_top_influencers(self, k):
        """
        Metodo que retorna os k usuarios mais seguidos da rede.

        Args:
            k (int): Quantidade desejada de mais seguidos.

        Returns:
            dict: Dicionario com os usuarios mais seguidos, sendo a chave o
                username do usuario e valor a quantidade de seguidores.
        """
        return {influencer.username: influencer.get_number_of_users_followers() for influencer in self.merge_sort('top')[:k]}

    def get_path(self, username_1, username_2):
        """
        Metodo que retorna o caminho entre dois usuarios na rede

        Args:
            username_1 (str): Username do usuario de origem do caminho.
            username_2 (str): Username do usuario de destino do caminho.
        
        Returns:
            str: Caminho entre os usuarios com os usernames dos usuarios do
                caminho.
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
        Metodo que ordena os usuario a partir do Merge Sort. A ordenacao leva
        em consideracao, quando a ordecao e para os stories, os melhores amigos
        e depois a ordem alfabetica do username do usuario que e seguido. Quando
        a ordenacao e para os mais seguidos, a ordenacao leva em consideracao os
        a quantidade de seguidores.

        Args:
            method (str): Metodo que deseja ordenar ('stories' ou 'top')
            username (str, opcional): Username do usuario quando o metodo de
                ordenacao for para os stories. Por padrao, o username e None.
            list_to_sort (list, opcional): Lista para ordenar utilizada na
                recursao das sublistas da esquerda e direita. Por padrao, a
                lista e None.
        
        Returns:
            list: Lista ordenada. Se o method for 'stories', a lista sera uma
                lista de usernames. Se o method for 'top', a lista sera uma
                lista ordenada por quantidade de seguidores.
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

        left = self.merge_sort(method, list_to_sort[:middle], username)
        
        right = self.merge_sort(method, list_to_sort[middle:], username)

        return self.merge(method, username, left, right)

    def merge(self, method, left, right, username=None):
        """
        Metodo auxiliar do Merge Sort que une as sublistas. A ordenacao leva
        em consideracao, quando a ordecao e para os stories, os melhores amigos
        e depois a ordem alfabetica do username do usuario que e seguido. Quando
        a ordenacao e para os mais seguidos, a ordenacao leva em consideracao os
        a quantidade de seguidores.

        Args:
            method (str): Metodo que deseja ordenar. Sendo 'stories' para os
                stories e 'top' para os usuarios mais seguidos.
            left (list): Sublista da esquerda.
            right (list): Sublista da direita.
            username (str, opcional): Username do usuario que deseja os stories
                ordenados. 
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
    
    def breadth_first_search(self, username_1, username_2):
        """
        Metodo que faz a Busca em Largura para encontrar o caminho entre dois
        usuarios.

        Args:
            username_1 (str): Username do usuario de origem do caminho.
            username_2 (str): Username do usuario de destino do caminho.
        """
        root = self.get_user_by_username(username_1)

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

                if adjacent.username == username_2:
                    queue = []
            
            node.color = 'black'