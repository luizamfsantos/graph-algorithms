from collections import deque 


# SITUATION A: given an edge list, return the
# order of visited nodes in a breadth-first search

def bfs_from_edge_list(
    edge_list: list[tuple[int,int]]
) -> list[tuple[int,int]]:
    # null case
    if not edge_list:
        return []
    # create a queue for the breadth-first search
    queue = deque()
    visited = set()
    order = []
    
    # start the search at the first node in the edge list
    node = edge_list[0][0]
    visited.add(node)
    order.append(node)
    queue.append(node)

    while queue:
        # visit the next node in the queue
        node = queue.popleft()
        # loop over all edges to find the next nodes to visit
        for edge in edge_list:
            if node == edge[0] and edge[1] not in visited:
                visited.add(edge[1])
                order.append(edge[1])
                queue.append(edge[1])
    return order



if __name__ == '__main__':
    from random import randint
    # A: given an edge list, return the order of visited nodes in a breadth-first search
    edge_list = [(randint(0, 10), randint(0, 10)) for _ in range(10)]