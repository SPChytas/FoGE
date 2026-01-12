import networkx as nx
import numpy as np 




'''
Graph labels generation.

The graph is assumed to be an instance of networkx graph.
'''

def node_count(graph, graph_path):

    num_nodes = graph.number_of_nodes()

    return [{'path': graph_path,
             'question': 'How many nodes are in this graph?',
             'answer': '%d' %(num_nodes)}]


def node_degree(graph, graph_path):

    tasks = []

    degrees = list(graph.degree)
    for node_id, deg in degrees:

        tasks.append({'path': graph_path,
                      'question': 'What is the degree of node %s?' %(node_id),
                      'answer': '%d' %(deg)})

    return tasks


def edge_count(graph, graph_path):

    num_edges = graph.number_of_edges()

    return [{'path': graph_path,
             'question': 'How many edges are in this graph?',
             'answer': '%d' %(num_edges)}]


def edge_existence(graph, graph_path):

    tasks = []

    num_nodes = graph.number_of_nodes()

    for s in range(num_nodes):
        for t in range(num_nodes):

            if ((str(s), str(t)) in graph.edges() or (str(t), str(s)) in graph.edges()):
                answer = 'Yes'
            else:
                answer = 'No'

            tasks.append({'path': graph_path,
                          'question': 'Is node %d connected to node %d?' %(s, t),
                          'answer': '%s' %(answer)})

    return tasks


def cycle(graph, graph_path):

    try:
        nx.find_cycle(graph)
        answer = 'Yes'
    except nx.NetworkXNoCycle:
        answer = 'No'

    return [{'path': graph_path,
             'question': 'Is there a cycle in this graph?',
             'answer': '%s' %(answer)}]


def triangles(graph, graph_path):

    num_triangles = int(np.sum(list(nx.triangles(graph).values())) / 3)
    
    return [{'path': graph_path,
             'question': 'How many triangles are in this graph?',
             'answer': '%d' %(num_triangles)}]



'''
Graphs label generation for GraphLLM dataset
'''

def substructure_count(graph, graph_path):

    answer = nx.get_node_attributes(graph, 'label')['0']
    
    return [{'path': graph_path,
             'question': 'How many carbon-carbon-oxygen triangles containing Atom #1 are in the molecule?',
             'answer': '%s' %(answer)}]


def maximum_triplet_sum(graph, graph_path):

    answer = nx.get_node_attributes(graph, 'label')['0']
    
    return [{'path': graph_path,
             'question': 'What is the maximum sum of age of a triplet composed of person 0, their friends and friends of friends?',
             'answer': '%s' %(answer)}]


def maximum_triplet_sum_named(graph, graph_path):

    answer = nx.get_node_attributes(graph, 'label')['0']
    name = nx.get_node_attributes(graph, 'name')['0']
    
    return [{'path': graph_path,
             'question': 'What is the maximum sum of age of a triplet composed of person %s, their friends and friends of friends?' %(name),
             'answer': '%s' %(answer)}]


def shortest_path(graph, graph_path):

    answer = nx.get_node_attributes(graph, 'label')['0']
    
    return [{'path': graph_path,
             'question': 'Starting from wormhole #1, how much dark matter do you need at minimum to reach wormhole #2?',
             'answer': '%s' %(answer)}]


def bipartite_graph_matching(graph, graph_path):

    answer = nx.get_node_attributes(graph, 'label')['0']
    
    return [{'path': graph_path,
             'question': 'For most how many applicants can find the job they are interested in?',
             'answer': '%s' %(answer)}]