from collections import OrderedDict
class Tree:
    def __init__(self, parent=None, key="main", value="node"):
        self.parent = parent
        self.store = OrderedDict()
        self.store[key] = value
        self.child = []
        self.child_count = 0 

    def insert_key_value(self, key, value=0,Type="int",definition=True):
        self.store[key] = [value,Type,definition]

    def is_present(self, key):
        if key in self.store:
            return True
        return False

    def add_child(self, children):
        self.child_count += 1
        self.child.append(children)

    def get_parent(self):
        return self.parent

    def child_len(self):
        return len(self.child)

    def get_child(self, key):
        return self.child[key]

    def get_dict(self):
        return self.store

    def get_value(self, key):
        return self.store[key]

    def rm_key(self, key):
        del self.store[key]

    def decrement_count(self):
        self.child_count -= 1

    def get_count(self):
        return self.child_count

root = Tree()
curr = root