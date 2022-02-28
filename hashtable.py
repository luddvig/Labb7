

class Node:
    def __init__(self, key="", data=None):
        self.key = key
        self.data = data

    def __str__(self):
        return self.data


class Hashtable:
    def __init__(self, size):
        self.size = size
        self.tabell = [[] for i in range(self.size)]

    def store(self, key, data):
        new_node = Node(key, data)
        self.tabell[self.hashfunction(key) % self.size].append(new_node)

    def search(self, key):
        data = self.tabell[self.hashfunction(key) % self.size]
        found = False
        for nod in data:
            if nod.key == key:
                found = True
                true_node = nod
        if found:
            return true_node.data
        else:
            raise KeyError

    def hashfunction(self, key):
        resultat = 0
        for i in key:
            resultat = resultat * 32 + ord(i)
        return resultat

