class Node:
    def __init__(self, name):
        self.children = []
        self.name = name

    def addChild(self, name):
        self.children.append(name)

    # Time: O(v + e) | Space: O(v)
    def breadthFirstSearch(self, array):
        queque = [self]
        while len(queque) > 0:
            current = queque.pop()
            array.append(current.name)
            for child in current.children:
                queque.append(child)

        return array
