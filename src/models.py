class Edge:
    def __init__(self, weight, destiny):
        self.weight = weight
        self.destiny = destiny

    def __repr__(self):
        return f'{self.destiny.username}: {self.weight}'

class Node:
    def __init__(self, name, username):
        self.name = name
        self.username = username
        self.following = {}
        self.followers = {}
        self.color = 'white'
        self.parent = None
    
    def __repr__(self):
        return f'{self.name}: {self.username}'
    
    def add_following(self, weight, node):
        if self.following.get(node.username):
            edge = self.following.get(node.username)

            edge.weight = weight
        else:
            self.following[node.username] = Edge(weight, node)

    def add_followers(self, node):
        self.followers[node.username] = node
    
    def get_following(self):
        return self.following
    
    def get_followers(self):
        return self.followers
    
    def get_number_of_users_following(self):
        return len(self.following)
    
    def get_number_of_users_followers(self):
        return len(self.followers)
    
    # Retorna um usuario que este usuario siga a partir do username 
    def get_following_by_username(self, username):
        return self.following.get(username)
    
    # Retorna um usuario que siga este usuario a partir do username 
    def get_followers_by_username(self, username):
        return self.followers.get(username)

class Graph:
    def __init__(self):
        self.nodes = {}
    
    def add_user(self, name, username):
        if not self.get_user_by_username(username):
            self.nodes[username] = Node(name, username)

        return self.get_user_by_username(username)
    
    def add_connection(self, origin_username, destiny_username, weight):
        if self.get_user_by_username(origin_username) and self.get_user_by_username(destiny_username):
            origin = self.get_user_by_username(origin_username)

            destiny = self.get_user_by_username(destiny_username)

            origin.add_following(weight, destiny)

            destiny.add_followers(origin)
    
    def get_user_by_username(self, username):
        return self.nodes.get(username)
    
    def get_number_of_users_following_by_user(self, username):
        return len(self.get_user_by_username(username).get_following())
    
    def get_number_of_users_followers_by_user(self, username):
        return len(self.get_user_by_username(username).get_followers())
    
    def get_order_stories(self, username):
        return [edge.destiny.username for edge in self.merge_sort('stories', username)]

    def get_top_influencers(self, k):
        return {influencer.username: influencer.get_number_of_users_followers() for influencer in self.merge_sort('top')[:k]}

    def get_path(self, username_1, username_2):
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
        if not list_to_sort:
            if method == 'stories':
                user = self.get_user_by_username(username)

                following = user.get_following()

                list_to_sort = list(following.values())
            else:
                list_to_sort = list(self.nodes.values())

        if len(list_to_sort) == 1:
            return list_to_sort
        
        middle = len(list_to_sort) // 2

        left = self.merge_sort(method, username, list_to_sort[:middle])
        
        right = self.merge_sort(method, username, list_to_sort[middle:])

        return self.merge(method, username, left, right)

    def merge(self, method, username, left, right):
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
        root = self.get_user_by_username(username1)

        root.color = 'gray'

        queue = [root]

        while queue:
            node = queue.pop(0)

            list_of_adjacent = [edge.destiny for edge in list(node.get_following().values())]

            for adjacent in list_of_adjacent:
                if adjacent.color == 'white':
                    adjacent.color = 'gray'
                    adjacent.parent = node
                    queue.append(adjacent)

                if adjacent.username == username2:
                    queue = []
            
            node.color = 'black'