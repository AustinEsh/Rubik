import rubik

class Queue():
    def __init__(self):
        self.list = []
    def IsEmpty(self):
        return len(self.list) == 0
    def Add(self, item):
        self.list.append(item)
    def Remove(self):
        return self.list.pop(0)

class Node():
    def __init__(self, permutation, parent = None):
        self.permutation = permutation
        self.parent = parent
        self.children = []

def path(perm1: Node, perm2: Node) -> list:
    path1 = []
    path2 = []
    while perm1.parent is not None:
        path1.append(perm1.permutation)
        perm1 = perm1.parent
    path1.reverse()
    while perm2 is not None:
        path2.append(perm2.permutation)
        perm2 = perm2.parent
    return path1 + path2

def shortest_path(start: tuple, end: tuple) -> list:
    """
    Using 2-way BFS, finds the shortest path from start_position to
    end_position. Returns a list of moves. 

    You can use the rubik.quarter_twists move set.
    Each move can be applied using rubik.perm_apply
    """
    if start == end:
        return []
    visited1 = []
    visited2 = []
    queue1 = Queue()
    queue2 = Queue()
    root1 = Node(start)
    root2 = Node(end)
    queue1.Add(root1)
    queue2.Add(root2)
    while not queue1.IsEmpty() and not queue2.IsEmpty():
        if not queue1.IsEmpty():
            perm1 = queue1.Remove()
            visited1.append(perm1)
            for move in rubik.quarter_twists:
                nextPerm1 = rubik.perm_apply(move, perm1.permutation)
                if nextPerm1 not in [i.permutation for i in visited1] and nextPerm1 not in queue1.list:
                    if nextPerm1 in [i.permutation for i in visited2]:
                        for i in visited2:
                            if i.permutation == nextPerm1:
                                perm2 = i
                                break
                        return path(perm1, perm2)
                    queue1.Add(Node(nextPerm1, perm1))
        if not queue2.IsEmpty():
            perm2 = queue2.Remove()
            visited2.append(perm2)
            for move in rubik.quarter_twists:
                nextPerm2 = rubik.perm_apply(move, perm2.permutation)
                if nextPerm2 not in [i.permutation for i in visited2] and nextPerm2 not in queue2.list:
                    if nextPerm2 in [i.permutation for i in visited1]:
                        for i in visited1:
                            if i.permutation == nextPerm2:
                                perm1 = i
                                break
                        return path(perm1, perm2)
                    queue2.Add(Node(nextPerm2, perm2))
    return None