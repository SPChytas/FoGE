import numpy as np 


def node_count(graph, graph_path):

    num_nodes = graph['num_nodes']

    return [{'path': graph_path,
             'question': 'How many nodes are in this hypergraph?',
             'answer': '%d' %(num_nodes)}]


def node_degree(graph, graph_path):

    num_nodes = graph['num_nodes']

    tasks = []

    for node_id in range(num_nodes):

        deg = 0
        for e, nodes in graph.items():
            if (e == 'num_nodes'):
                continue
            if (node_id in nodes):
                deg += 1

        tasks.append({'path': graph_path,
                      'question': 'What is the degree of node %s?' %(node_id),
                      'answer': '%d' %(deg)})

    return tasks


def edge_count(graph, graph_path):

    num_edges = len(graph) - 1

    return [{'path': graph_path,
             'question': 'How many hyperedges are in this hypergraph?',
             'answer': '%d' %(num_edges)}]


def edge_existence(graph, graph_path):

    tasks = []

    num_nodes = graph['num_nodes']

    for s in range(num_nodes):
        for t in range(num_nodes):

            answer = 'No'
            for e, nodes in graph.items():
                if (e == 'num_nodes'):
                    continue
                if (s in nodes and t in nodes):
                    answer = 'Yes'
                    break

            tasks.append({'path': graph_path,
                          'question': 'Is node %d connected to node %d?' %(s, t),
                          'answer': '%s' %(answer)})

    return tasks


