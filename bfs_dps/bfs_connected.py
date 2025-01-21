from collections import deque 


# SITUATION A: given an edge list, return the
# order of visited nodes in a breadth-first search
def create_adjacency_dict_from_edge_list(
    edge_list: list[tuple[int,int]]
) -> dict[int, list[int]]:
    adjacency_dict = {}
    for node1, node2 in edge_list:
        if node1 not in adjacency_dict:
            adjacency_dict[node1] = []
        if node2 not in adjacency_dict:
            adjacency_dict[node2] = []
        adjacency_dict[node1].append(node2)
        adjacency_dict[node2].append(node1)
    return adjacency_dict

def bfs_from_edge_list(
    edge_list: list[tuple[int,int]]
) -> list[tuple[int,int]]:
    # null case
    if not edge_list:
        return []

    # convert the edge list to an adjacency dictionary
    adjacency_dict = create_adjacency_dict_from_edge_list(edge_list)
    
    # start the search at the first node in the edge list
    node = edge_list[0][0]
    visited = {node}
    order = [node]
    queue = deque([node])

    while queue:
        # visit the next node in the queue
        node = queue.popleft()
        # look at all the neighbors of the node
        for neighbor in adjacency_dict[node]:
            # if the neighbor has not been visited
            if neighbor not in visited:
                visited.add(neighbor)
                order.append(neighbor)
                queue.append(neighbor)

    return order



if __name__ == '__main__':
    from random import randint
    # A: given an edge list, return the order of visited nodes in a breadth-first search
    edge_list = [(randint(0, 10), randint(0, 10)) for _ in range(20)]
    print(edge_list)
    order = bfs_from_edge_list(edge_list)
    print(order)