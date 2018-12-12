class Search():
    # Klasse Node für die Implementierung eines Algorithmus
    class Node():
        """A node class for A* Pathfinding"""

     def __init(self, parent=None, position=None):
        self.parent = parent
        self.position = position

        self.g = 0
        self.h = 0
        self.f = 0

    def __eq__(self, other):
        return self.position == other.position

def astar(maze, start, end):
    """Returns a list of tuples as a path from the given start to the given end"""

    # Erstelle Start und End Node
    start_node = Node(None, start)
    start_node.g = start_node.h = start_node.f = 0
    end_node = Node(None, end)
    end_node.g = end_node.h = end_node.f = 0

    # Intialisiere die offene und geschlossene Liste
    open_list = []
    closed_list = []

    # Loop, bis du den Ende findest
    while len(open_list) > 0:

        #aktuellen Noder erhalten
        current_node = open_list[0]
        current_index = 0
        for index, item in enumerate(open_list):
            if item.f < current_node.f:
                current_node = item
                current_index = index

        # Pop aktuelle offene Liste und füge dies zur closed list
        open_list.pop(current_index)
        closed_list.append(current_node)

        # Finde das Ziel
        if current_node == end_node:
            path = []
            current = current_node
            while current is not None:
                path.append(current.position)
                current = current.parent
            return path[::-1]

        # Erstelle die Kinder
        children = []
        for new_position in [(0, -1), (0, 1), (-1, 0), (1, 0), (-1, -1), (-1, 1), (1, -1), (1, 1)]:  # Adjacent squares

            # Erhalte Node Position
            node_position = (current_node.position[0] + new_position[0], current_node.position[1] + new_position[1])

            # Sicherstellen, dass es in die Range passt
            if maze[node_position[0][node_position[1]]] != 0:
                continue

            # Erstelle neues Node
            new_node = Node(current_node, node_position)

            # Anhängen
            children.append(new_node)

        # Schaue dir die Children an
        for child in children:

            # Child ist in der Closed List
            for closed_child in closed_list:
                if child == closed_child:
                    continue

            # Erstelle den f,g und h Wert
            child.g = current_node.g + 1
            child.h = ((child.position[0] - end_node.position[0]) ** 2) + (
                        (child.position[1] - end_node.position[1]) ** 2)
            child.f = child.g + child.h

            # Child ist aktuell schon in der Open list
            for open_node in open_list:
                if child == open_node and child.g > open_node.g:
                    continue

            # füge Child zur open List
            open_list.append(child)


def main():
    maze = [[0, 0, 0, 0, 1, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 1, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 1, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 1, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 1, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 1, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 1, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 1, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]]

    start = (0, 0)
    end = (7, 6)

    path = astar(maze, start, end)
    print(path)


if __name__ == '__main__':
    main()