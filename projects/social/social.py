import random


class Queue:
    def __init__(self):
        self.queue = []

    def enqueue(self, value):
        self.queue.append(value)

    def dequeue(self):
        if self.size() > 0:
            return self.queue.pop(0)
        else:
            return None

    def size(self):
        return len(self.queue)


class User:
    def __init__(self, name):
        self.name = name


class SocialGraph:
    def __init__(self):
        self.last_id = 0
        self.users = {}
        self.friendships = {}

    # needs to be undirected, bi-directional
    def add_friendship(self, user_id, friend_id):
        if user_id == friend_id:
            print("You cannot connect with yourself")
        elif friend_id in self.friendships[user_id] or user_id in self.friendships[friend_id]:
            print("Connection already exists")
        else:
            self.friendships[user_id].add(friend_id)
            self.friendships[friend_id].add(user_id)

    # new user created with the next ID in order
    def add_user(self, name):
        self.last_id += 1
        self.users[self.last_id] = User(name)
        self.friendships[self.last_id] = set()

    def populate_graph(self, num_users, avg_friendships):

        """
        Number of users and Average number of friendships
        Equals number of users and friendships randomly connected
        Number of users > than  Average number of friendships.
        """
        # Start graph over
        self.last_id = 0
        self.users = {}
        self.friendships = {}
        # implement me

        # Add Users
        for u in range(1, num_users + 1):
            self.add_user(u)
            # New Friendships
            possible_friendships = [1]
        for user_id in self.users:
            # +1 to the user_id which is zero based, needed 1 based for user
            for friend_id in range(user_id + 1, self.last_id + 1):
                possible_friendships.append((user_id, friend_id))
        # randomize list
        random.shuffle(possible_friendships)
        # bidirectional so you must divide by 2
        for i in range(num_users * avg_friendships // 2):
            friendship = possible_friendships[i]
            self.add_friendship(friendship[0], friendship[1])

    def get_all_social_paths(self, user_id):
        """
        Takes a user's user_id as an argument
        Returns a dictionary containing every user in that user's
        extended network with the shortest friendship path between them.
        The key is the friend's ID and the value is the path.
        Breadth first search
        """
        visited = {}  # Note that this is a dictionary, not a set
        # !!!! IMPLEMENT ME
        qq = Queue()
        qq.enqueue([user_id])

        while qq.size() > 0:
            # deque the first path
            current_path = qq.dequeue()
            # grab most recent vertex
            current_vertex = current_path[-1]
            # if the current vertex has not been visited
            if current_vertex not in visited:
                # if neither are visited add to dictionary
                visited[current_vertex] = current_path
                for friend in self.friendships[current_vertex]:
                    copy_path = current_path.copy()
                    copy_path.append(friend)
                    qq.enqueue(copy_path)

        return visited


if __name__ == '__main__':
    sg = SocialGraph()
    sg.populate_graph(10, 2)
    print(sg.friendships)
    connections = sg.get_all_social_paths(1)
    print(connections)
