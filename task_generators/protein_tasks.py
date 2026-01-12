import networkx as nx
import numpy as np 




def node_count(graph, graph_path):

    num_nodes = graph.number_of_nodes()

    return [{'path': graph_path,
             'question': 'How many amino acids are in this protein?',
             'answer': '%d' %(num_nodes)}]


def node_type(graph, graph_path):

    tasks = []

    type_dict = nx.get_node_attributes(graph, 'type')

    for node_id, node_type in type_dict.items():

        tasks.append({'path': graph_path,
                      'question': 'What is the type of amino acid %s?' %(node_id),
                      'answer': '%s' %(node_type)})

    return tasks


def edge_count(graph, graph_path):

    num_edges = graph.number_of_edges()

    return [{'path': graph_path,
             'question': 'How many links are in this protein?',
             'answer': '%d' %(num_edges)}]



